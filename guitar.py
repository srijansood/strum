import json

def isstring(c):
    return (15 <= c.y_pos_mm <= 60)

def isfret(c):
    return (71 <= c.y_pos_mm <= 116)

def play(s, f):
    return "\"|sox -n -p synth 1 pl " + s + "  vol " + str(f) + "\""

def strings(c):
    stringPlayed = ""
    if (15 <= c.y_pos_mm < 22.5):
        stringPlayed = "E"
    elif (22.5 <= c.y_pos_mm < 30):
        stringPlayed = "A"
    elif (30 <= c.y_pos_mm < 37.5):
        stringPlayed = "D"
    elif (37.5 <= c.y_pos_mm < 45):
        stringPlayed = "G"
    elif (45 <= c.y_pos_mm < 52.5):
        stringPlayed = "B"
    elif (52.5 <= c.y_pos_mm < 61):
        stringPlayed = "E2"
    else:
        stringPlayed = "none"
    return stringPlayed

def fretFor(c):
    fretFor = ""
    if (70 <= c.y_pos_mm < 77.5):
        fretFor = "E"
    elif (77.5 <= c.y_pos_mm < 85):
        fretFor = "A"
    elif (85 <= c.y_pos_mm < 92.5):
        fretFor = "D"
    elif (92.5 <= c.y_pos_mm < 100):
        fretFor = "G"
    elif (100 <= c.y_pos_mm < 107.5):
        fretFor = "B"
    elif (107.5 <= c.y_pos_mm < 116):
        fretFor = "E2"
    else:
        fretFor = "none"
    return fretFor

def fretNumber(c):
    fretNum = 0
    if (isstring(c)):
        fretNum = 0
    elif (5 <= c.x_pos_mm < 20):
        fretNum = 20
    elif (20 <= c.x_pos_mm < 35):
        fretNum = 19
    elif (35 <= c.x_pos_mm < 48):
        fretNum = 18
    elif (48 <= c.x_pos_mm < 61):
        fretNum = 17
    elif (61 <= c.x_pos_mm < 73):
        fretNum = 16
    elif (73 <= c.x_pos_mm < 85):
        fretNum = 15
    elif (85 <= c.x_pos_mm < 97):
        fretNum = 14
    elif (97 <= c.x_pos_mm < 107):
        fretNum = 13
    elif (107 <= c.x_pos_mm < 116):
        fretNum = 12
    elif (116 <= c.x_pos_mm < 125):
        fretNum = 11
    elif (125 <= c.x_pos_mm < 134):
        fretNum = 10
    elif (134 <= c.x_pos_mm < 143):
        fretNum = 9
    elif (143 <= c.x_pos_mm < 152):
        fretNum = 8
    elif (152 <= c.x_pos_mm < 161):
        fretNum = 7
    elif (161 <= c.x_pos_mm < 170):
        fretNum = 6
    elif (170 <= c.x_pos_mm < 179):
        fretNum = 5
    elif (179 <= c.x_pos_mm < 188):
        fretNum = 4
    elif (188 <= c.x_pos_mm < 197):
        fretNum = 3
    elif (197 <= c.x_pos_mm < 206):
        fretNum = 2
    elif (206 <= c.x_pos_mm < 216):
        fretNum = 1
    return fretNum

def forceConvert(c):
    if (c.total_force < 300):
        return 1
    elif (c.total_force < 600):
        return 2
    elif (c.total_force < 900):
        return 2.4
    elif (c.total_force < 1200):
        return 2.8
    elif (c.total_force < 2500):
        return 3.4
    elif (c.total_force < 3000):
        return 3.8
    elif (c.total_force >= 3000):
        return 4.5
    return 1

def note(string, fret):
    with open('noteMap.json') as data_file:
        data = json.load(data_file)
    return data[string][str(fret)];
