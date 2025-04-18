#!/usr/bin/python3
import mido as mido
import musicMaker as mm
import noteData
import drumbeats as b
beat="rock"
snare=40
kick=35
ride=53
crash=55
rest=None
_=None

bass=37
ODgtr=94
DSgtr=86

drumvol=0.75
bassvol=0.5
rhythmvol=0.75
leadvol=0.80

mm.new()
mm.setName("song1")
mm.setKeySignature("E", 'minor')
progression=[0,3,6,4]
mm.setTempo(158)
mm.setTimeSignature(4, 4)
mm.addTrack("Drums", 0, drum=True)
mm.addTrack("Bass", bass)
mm.addTrack("Rhythm", DSgtr)
mm.addTrack("Lead", ODgtr)
mm.setRootNote("Drums", 0)
mm.setRootNote("Bass", noteData.getNote('E1'))
mm.setRootNote("Rhythm", noteData.getNote('E3'))
mm.setRootNote("Lead", noteData.getNote('E4'))

mm.addToPhrase(0, "Drums", "arpeggio", 0, interval=[kick, _, _, _, kick, kick, _, _], time=2, volume=drumvol)

mm.addToPhrase(1, "Drums", "arpeggio", 0, interval=[[kick,snare], _, _, _, kick, kick, _, _], time=2, volume=drumvol)

mm.copyToPhrase(2, "Drums", 1)
mm.addToPhrase(2, "Bass", "arpeggio", 0, interval=[0, _, 0, _, 0, 1, 2, _], time=2, volume=bassvol)

mm.copyToPhrase(3, "Drums", 1)
mm.addToPhrase(3, "Bass", "arpeggio", 0, interval=[0, _, 0, 4], time=2, volume=bassvol)
mm.addToPhrase(3, "Rhythm", "arpeggio", 0, interval=[[2], _, [0], _, [0,2], _, [0,2], _], time=2, volume=rhythmvol)

mm.addToPhrase(4, "Drums", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=2, volume=drumvol)
mm.copyToPhrase(4, "Bass", 3, dup=4)
mm.copyToPhrase(4, "Rhythm", 3, dup=4)
mm.addToPhrase(4, "Lead", "arpeggio", 0, interval=[0, 6], time=[7, 1], volume=leadvol)

mm.copyToPhrase(5, "Drums", 4)
mm.copyToPhrase(5, "Bass", 3, dup=4)
mm.copyToPhrase(5, "Rhythm", 3, dup=4)
mm.addToPhrase(5, "Lead", "arpeggio", 0, interval=[0, 2, 4, 6, 5, 6, 4], time=[2, .5, .5, .5, 2, .5, 1], volume=leadvol)

mm.addToPhrase(6, "Drums", "arpeggio", 0, interval=b.rhythm['2bass']["beat"], time=b.rhythm['2bass']["time"], dup=2, volume=drumvol)
mm.addToPhrase(6, "Bass", "arpeggio", 0, interval=[0, 2, 4, 7], time=2, dup=2, volume=bassvol)
mm.addToPhrase(6, "Rhythm", "arpeggio", 0, interval=[[0,2], _, [2,4], _, [4,6], _, [7,9], _], time=2, dup=2, volume=rhythmvol)

mm.addToPhrase(7, "Drums", "arpeggio", 0, interval=b.rhythm['2bass']["beat"], time=b.rhythm['2bass']["time"], dup=2, volume=drumvol)
mm.copyToPhrase(7, "Bass", 6)
mm.copyToPhrase(7, "Rhythm", 6)
mm.addToPhrase(7, "Lead", "arpeggio", 0, interval=[0, 2, 4, 7], time=1, dup=4,volume=leadvol)

mm.addToPhraseGroup(0, [0, 0, 1, 1], noteoffset=0)
mm.addToPhraseGroup(1, [2, 2], noteoffset=progression)
mm.addToPhraseGroup(2, [3, 3, 3, 3], noteoffset=progression)
mm.addToPhraseGroup(3, [4], noteoffset=progression)
mm.addToPhraseGroup(4, [5], noteoffset=progression)
mm.addToPhraseGroup(5, [2], noteoffset=0)
mm.addToPhraseGroup(6, [6], noteoffset=progression)#[0,2,4,7])
mm.addToPhraseGroup(7, [7], noteoffset=[4,2,3,-2])
mm.addToPhraseGroup(7, [7], noteoffset=[0,2,4,7])

mm.addToSentence(1, [0, 2])
mm.addToSentence(2, [1])
mm.addToSentence(3, [3, 4, 3])
mm.addToSentence(4, [2, 3, 2])
mm.addToSentence(5, [1, 5])
mm.addToSentence(6, 6)
mm.addToSentence(7, 7)

mm.addToVerse('intro', 1)
mm.addToVerse('bridge', 2)
mm.addToVerse('chorus', 3)
mm.addToVerse('solo', [6,7,6])
mm.addToVerse('finale', 5)

mm.save(None, ['intro', 'bridge', 'chorus', 'bridge', 'chorus', 'bridge', 'solo', 'chorus', 'finale'])
#mm.save(None, ['bridge', 'solo', 'bridge'])
print(mm.song["name"]+".mid has been written.")

