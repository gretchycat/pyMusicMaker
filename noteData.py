interval =  { "P1":0, "d2":0,           #perfect unison, diminished second 
              "S":1, "m2":1, "A1":1,    #semitone, minor second, augmented unison
              "T":2, "M2":2,            #tone, major second
              "m3":3, "A2":3,           #minor third, augmented second
              "M3":4, "d4":4,           #major third, diminished tourth
              "P4":5, "A3":5,           #perfect fourth, augmented third
              "d5":6, "A4":6, "TT":6,   #diminished fifth, augmented fourth, tritone
              "P5":7, "d6":7,           #perfect fifth, diminished sixth
              "m6":8, "A5":8,           #minor sixth, augmented fifth
              "M6":9, "d7":9,           #major sixth, diminished seventh
              "m7":10, "A6":10,         #minor seventh, augmented sixth
              "M7":11, "d8":11,         #major seventh, diminished eighth
              "P8":12, "A7":12, "O":12  #perfect octave/perfect eighth, augmented seventh, octave
            }
i = interval

modePriority =['majorpentatonic', 'minorpentatonic', 'major', 'minor', 'harmonicminor', 'melodicminor']

modes = {   #intervals from rootnote to make the modes
            "major":            [ i["P1"], i["M2"], i["M3"], i["P4"], i["P5"], i["M6"], i["M7"] ],   
            "minor":            [ i["P1"], i["M2"], i["m3"], i["P4"], i["P5"], i["m6"], i["m7"] ],            
            "harmonicminor":    [ i["P1"], i["M2"], i["m3"], i["P4"], i["P5"], i["m6"], i["M7"] ],
            "melodicminor":     [ i["P1"], i["M2"], i["m3"], i["P4"], i["P5"], i["M6"], i["M7"] ],
            "dorian":           [ i["P1"], i["M2"], i["m3"], i["P4"], i["P5"], i["M6"], i["m7"] ],
            "phrygian":         [ i["P1"], i["m2"], i["m3"], i["P4"], i["P5"], i["m6"], i["m7"] ],
            "lydian":           [ i["P1"], i["M2"], i["M3"], i["d5"], i["P5"], i["M6"], i["M7"] ],
            "mixolydian":       [ i["P1"], i["M2"], i["M3"], i["P4"], i["P5"], i["M6"], i["m7"] ],
            "aeolian":          [ i["P1"], i["M2"], i["m3"], i["P4"], i["P5"], i["m6"], i["m7"] ],
            "ionian":           [ i["P1"], i["M2"], i["M3"], i["P4"], i["P5"], i["M6"], i["M7"] ],
            "locrian":          [ i["P1"], i["m2"], i["m3"], i["P4"], i["d5"], i["m6"], i["m7"] ],
            "majorpentatonic":  [ i["P1"], i["M2"], i["M3"], i["P5"], i["M6"] ],
            "minorpentatonic":  [ i["P1"], i["m3"], i["P4"], i["P5"], i["m7"] ],
            "chromatic":        [ 0,1,2,3,4,5,6,7,8,9,10,11 ]
        }

keyNames = [ "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B" ]

def getKey(note): #which key is a midi note?
    return keyNames[note%12]
    
def getOctave(note): #which octave is a midi note?
        return int((note/12)-1)

def getNote(key, octave=None): #get midi note from Note strinh (ie C#-1)
    if(type(octave)==int):
        if(key.upper() in keyNames):
            return (octave+1)*12+keyNames.index(key.upper())
        return (octave+1)*12
    else:
        keyAndOctave=key.upper()
        if(keyAndOctave[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G']):
            key=keyAndOctave[0]
            if(len(key)>1):
                if(keyAndOctave[1]=='#'):
                    key=key+'#'
        if(key in keyNames):
            ostr=""
            for chr in keyAndOctave:
                neg=0
                if(chr=='-'):
                    neg=1
                if(chr in [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]):
                    ostr+=chr
            if(neg==1):
                ostr="-"+ostr
            if(ostr==""):
                ostr="0"
            return getNote(key, int(ostr))
    return 0

def getRelNote(mode='major', note=0):   #returns number of half-steps from the root of the mode
    scale=modes[mode]
    noteoffset=0
    if(note<0):
        while(note<0):
            noteoffset=noteoffset-12
            note=note+(len(scale))
        return noteoffset+scale[note]
    else: 
        if(note>=len(scale)):
            while(note>=len(scale)):
                noteoffset=noteoffset+12
                note=note-(len(scale))
            return noteoffset+scale[note]
    return scale[note]


def getNoteName(note): #get note string from midi note
    return getKey(note)+str(getOctave(note))

def checkKeySignature(notelist, key, mode): #do the notes in notelist fit in the key/mode?
    modeNotes=[]
    offset=getNote(key)%12
    if mode in modes:
        modeNotes=modes[mode]
    else:
        print("Unknown mode: ", mode)
        return False
    notes=[]
    for n in notelist:  #normalize notes
        if(((n+offset)%12) not in notes):
            notes.append((n+offset)%12)
    if(len(notes)==0):  #no notes? return false
        return False
    for n in notes:     #do the notes fit in the mode?
        if n not in modeNotes:
            return False
    return True

def findKeySignature(notelist): #return a list of key/mode pairs that fit the notelist
    keyFit=[]
    for mode in modePriority:
        for key in keyNames:
            if(checkKeySignature(notelist, key, mode)):
                keyFit.append([key, mode])
    return keyFit
