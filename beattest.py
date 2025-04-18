#!/usr/local/bin/python
import musicMaker as mm
import drumbeats as b

mm.new()
mm.setName("beattest")
mm.setKeySignature("E", 'major')
mm.setTempo(100)
mm.setTimeSignature(4, 4)
mm.addTrack("drum", 0, drum=True)
mm.setRootNote("drum", 0)

beat="thing"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=4)
beat="rock"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=4)
beat="swing"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=4)
beat="reggae"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=4)
beat="hiphop"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=4)
beat="funk"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=4)
beat="ska"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=4)
beat="disco"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=4)
beat="2bass"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=4)
beat="2bass6"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=4)
beat="2bassv"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=4)
beat="ballad"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=4)
beat="pop"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=4)
beat="punk"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=4)
beat="2line"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=4)
beat="country"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=4)
beat="latin"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"], dup=4)
beat="blues"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"]/2, dup=4)
beat="shuffle"
mm.addToPhrase(0, "drum", "arpeggio", 0, interval=b.rhythm[beat]["beat"], time=b.rhythm[beat]["time"]/2, dup=4)
        
mm.addToPhraseGroup(1, 0, noteoffset=0)

mm.addToSentence(1, [1])

mm.addToVerse('drum', 1)

mm.save(None, ['drum'])
print(mm.song["name"]+".mid has been written.")


