#!/usr/bin/python3
import rtmidi as rtmidi
import mido as mido
import musicMaker as mm
import noteData
import drumbeats as b
import instruments as i
_=None
drumvol=0.75
leadvol=0.80
bassvol=0.75
mm.new()
mm.setName("song2")
mm.setKeySignature("C", 'minor')
progression=[0,-1, 2, 1]
mm.setTempo(133)
mm.setTimeSignature(4, 4)
mm.addTrack("Drums", 0, drum=True)
mm.addTrack("Lead",i.pad_6_metallic)
mm.addTrack("Bass",i.slap_bass_2)
mm.setRootNote("Drums", 0)
mm.setRootNote("Lead", noteData.getNote('C3'))
mm.setRootNote("Bass", noteData.getNote('C2'))

mm.addToPhrase(0, "Drums", "arpeggio", 0, interval=b.rhythm["ballad"]['beat'], time=b.rhythm['ballad']['time'], volume=drumvol, dup=1)
mm.addToPhrase(0, 'Lead', "arpeggio", 0, interval=[0, 4, 0, -1, 0, 4, 0, _], time=4, volume=leadvol, dup=2)
mm.addToPhrase(0, 'Bass', "arpeggio", 0, interval=[0,4,_], time=[1/2,1.5,2], volume=bassvol, dup=2)

mm.addToPhrase(1, "Drums", "arpeggio", 0, interval=b.rhythm["ballad"]['beat'], time=b.rhythm['ballad']['time'], volume=drumvol, dup=1)
mm.addToPhrase(1, 'Lead', "arpeggio", 0, interval=[0, 2, 0, 4, 0, 2, 0, _], time=4, volume=leadvol, dup=2)
mm.addToPhrase(1, 'Bass', "arpeggio", 0, interval=[0,2,_], time=[0.5,1.5,2], volume=bassvol, dup=2)
mm.addToPhraseGroup(0, [0,1], noteoffset=progression)

mm.addToSentence(0, [0,0,0,0,0,0,0,0,0])

mm.addToVerse('intro', 0)

mm.save(None, ['intro'])
print(mm.song["name"]+".mid has been written.")

