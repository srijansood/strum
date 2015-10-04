from __future__ import print_function
from keyboard_reader import *
import sensel
from guitar import strings, isfret, isstring, fretFor, fretNumber

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

    while not exit_requested:
        contacts = sensel_device.readContacts()

        if len(contacts) == 0:
            continue

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

            if isstring(c):
                print("~~ String: %s" %(strings(c)), end="\r\n")
            elif isfret(c):
                print("~~ Fret: %s%d" %(fretFor(c), fretNumber(c)), end="\r\n")

            print("Contact ID %d, event=%s, mm coord: (%f, %f), force=%d, "
                  "major=%f, minor=%f, orientation=%f" %
                  (c.id, event, c.x_pos_mm, c.y_pos_mm, c.total_force,
                   c.major_axis_mm, c.minor_axis_mm, c.orientation_degrees), end="\r\n")

        if len(contacts) > 0:
            print("****", end="\r\n");

    sensel_device.stopScanning();
    sensel_device.closeConnection();
    keyboardReadThreadStop()

if __name__ == "__main__":
    openSensorReadContacts()
