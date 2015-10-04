from __future__ import print_function
from keyboard_reader import *
import sensel
from subprocess import Popen, PIPE
from guitar import *
import os


exit_requested = False;

def keypress_handler(ch):
    global exit_requested

    if ch == 0x51 or ch == 0x71: #'Q' or 'q'
        print("Exiting Example...", end="\r\n");
        exit_requested = True;


def openSensorReadContacts():
    sensel_device = sensel.SenselDevice()

    if not sensel_device.openConnection():
        print("Unable to open Sensel sensor!", end="\r\n")
        exit()

    keyboardReadThreadStart(keypress_handler)

    #Enable contact sending
    sensel_device.setFrameContentControl(sensel.SENSEL_FRAME_CONTACTS_FLAG)

    #Enable scanning
    sensel_device.startScanning()

    print("\r\nStart strumming!", end="\r\n")

    # fretsBool = (False, ) * 20 #start at none pressed
    # numFrets = 0
    while not exit_requested:
        contacts = sensel_device.readContacts()

        if len(contacts) == 0:
            continue

        fretsPressed = []
        fretCombo = []
        stringsStrummed = []
        forces = []
        toStrum = False
        stringToStrum = "none"
        for c in contacts:
            event = ""
            if c.type == sensel.SENSEL_EVENT_CONTACT_INVALID:
                event = "invalid";
            elif c.type == sensel.SENSEL_EVENT_CONTACT_START:
                sensel_device.setLEDBrightness(c.id, 100) #Turn on LED
                event = "start"
            elif c.type == sensel.SENSEL_EVENT_CONTACT_MOVE:
                event = "move";
            elif c.type == sensel.SENSEL_EVENT_CONTACT_END:
                sensel_device.setLEDBrightness(c.id, 0) #Turn off LED
                event = "end";
            else:
                event = "error";

            # if isstring(c):
            #     print("~~ String: %s" %(strings(c)), end="\r\n")

            #which frets are pressed
            if isfret(c):
                fretnum = fretNumber(c)
                fretisfor = fretFor(c)
                if fretnum != 0:
                    fretsPressed.append(fretnum)
                    fretCombo.append(fretisfor + "-" + str(fretnum))

            #which string
            if isstring(c):
                stringToStrum = strings(c)
                if stringToStrum != "none":
                    toStrum = True
                    force = forceConvert(c)
                    # stringsStrummed.append(strn)
                    # forces.append(forceConvert(c))

        print ("Frets: ", fretCombo, end="\r\n")
        if toStrum:
            # if isfret(c) & fretNumber(c)!=0:
            #     fretCombo = fretFor(c) + str(fretNumber(c))
            # else:
            #     fretCombo = strings(c)

            notesToPlay = []

            #frets being pressed
            for f in fretsPressed:
                notesToPlay.append(note(stringToStrum, f))
            #just strings
            if len(fretsPressed) == 0:
                notesToPlay.append(note(stringToStrum, 0))


            for someNote in notesToPlay:
                print ("Strumming: %s" %(stringToStrum), end="\r\n")
                print ("Note To Play: %s" %(someNote), end="\r\n")
                FNULL = open(os.devnull, 'w')
                retcode = Popen("play " + play(someNote, force), shell=True, stdin=PIPE, stdout=PIPE, stderr=FNULL)

        #     notesToPlay = []
        # else :
        #     continue


                #print("Command is play ", play(noteToPlay, force))

                # if event != "end":
                #     FNULL = open(os.devnull, 'w')
                #     retcode = Popen("play " + play(noteToPlay, force), shell=True, stdin=PIPE, stdout=FNULL, stderr=FNULL)

                    #retcode = Popen("play " + play(noteToPlay, force), shell=True, stdin=PIPE, stdout=PIPE)

            # print("Contact ID %d, event=%s, mm coord: (%f, %f), force=%d, "
            #       "major=%f, minor=%f, orientation=%f" %
            #       (c.id, event, c.x_pos_mm, c.y_pos_mm, c.total_force,
            #        c.major_axis_mm, c.minor_axis_mm, c.orientation_degrees), end="\r\n")
    sensel_device.stopScanning();
    sensel_device.closeConnection();
    keyboardReadThreadStop()

if __name__ == "__main__":
    openSensorReadContacts()
