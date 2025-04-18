#!/usr/local/bin/python
import musicMaker as mm
import noteData

mm.new()
mm.setName("test")
mm.setKeySignature("E", 'minor')
mm.setTempo(150)
mm.setTimeSignature(4, 4)
mm.addTrack("Cello", 42)
mm.addTrack("Drums", 0, drum=True)
mm.setRootNote("Cello", noteData.getNote('E2'))
mm.setRootNote("Drums", 0)


#def addToPhrase(trackidx, trackname, notetype, note, interval, time, timesignature=None):   #notetype is note, rest, chord or arpeggio        
mm.addToPhrase(0, "Cello", "arpeggio", 0, interval=[0,2,4,7], time=1)
mm.addToPhrase(0, "Drums", "arpeggio", 35, interval=[[1, 3], None, 3, 3], time=1)
mm.addToPhraseGroup(1, [0, 0, 0, 0], noteoffset=0)
mm.addToPhraseGroup(1, [0, 0, 0, 0], noteoffset=4)
mm.addToPhraseGroup(1, [0, 0, 0, 0], noteoffset=5)
mm.addToPhraseGroup(1, [0, 0, 0, 0], noteoffset=3)

mm.addToPhrase(1, "Cello", "arpeggio", 4, interval=[None,2,4,7,5,3,1], time=[1, 1, 2, 1, .5, 1, .5])
mm.addToPhrase(2, "Cello", "arpeggio", 3, interval=[0,1,None,2,3,None,4,5,None,6,7,None], time=4)
mm.addToPhrase(3, "Cello", "arpeggio", 0, interval=[0,2,4], time=1)
mm.addToPhraseGroup(2, [1,2,3], noteoffset=0) 
mm.addToPhraseGroup(2, [1,2,3], noteoffset=4) 
mm.addToPhraseGroup(3, [1,2,3], noteoffset=5) 
mm.addToPhraseGroup(3, [1,2,3], noteoffset=3) 
mm.addToPhraseGroup(3, [3], noteoffset=1) 

mm.addToSentence(1, [1])
mm.addToSentence(2, [2,2])
mm.addToSentence(2, [3,2])
mm.addToSentence(2, [3,3])

mm.addToVerse('arpeggio', 1)
mm.addToVerse('rawr', 2)

mm.save(None, ['arpeggio', 'rawr', 'arpeggio'])
print(mm.song["name"]+".mid has been written.")


