def isstring(c):
    return (15 <= c.y_pos_mm <= 60)

def isfret(c):
    return (71 <= c.y_pos_mm <= 116)

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
        stringPlayed = "E"
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
        fretFor = "E"
    else:
        fretFor = "none"
    return fretFor
