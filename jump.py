#!/usr/local/bin/python
import musicMaker as mm

mm.new()
mm.setName("jump")
mm.setKeySignature("E", 'major')
mm.setTempo(150)
mm.setTimeSignature(4, 4)
mm.addTrack("FX", 80)
mm.setRootNote("FX", mm.getNote('E4'))

#def addToPhrase(trackidx, trackname, notetype, note, interval, time, timesignature=None):   #notetype is note, rest, chord or arpeggio        
mm.addToPhrase(0, "FX", "arpeggio", 0, interval=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], time=.5)
mm.addToPhraseGroup(1, 0, noteoffset=0)

mm.addToSentence(1, [1])

mm.addToVerse('jump', 1)

mm.save(None, ['jump'])
print(mm.song["name"]+".mid has been written.")


