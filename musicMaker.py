import mido
import math
import noteData as nd
song={ "program":0, 'nextChannel':0 }
clocks_per_click = 24
trackidx=0
#interval names
def playNote(trackname, note=0, time=0.0, restOffset=0.0, volume=1.0):
    td=song['tracks'][trackname]
    track=td["track"]
    time=float(time)
    channel=td['channel']
    if(type(note)==int):
        if(restOffset != 0.0):
            td['restOffset']=restOffset
        track.append(mido.Message('note_on', note=note, channel=channel, velocity=int(127*volume), time=int(td['restOffset']*song['beatLength'])))
        track.append(mido.Message('note_off', note=note, channel=channel, velocity=int(127*volume), time=int(time*song["beatLength"])))
        td['restOffset']=0.0
    else:
        td['restOffset']+=time

def playRelNote(trackname, mode=None, note=0, time=0.0, restOffset=0.0, volume=1.0):
    td=song['tracks'][trackname]
    track=td["track"]
    time=float(time)
    if(restOffset != 0.0):
        td['restOffset']=restOffset

    rootnote=song["tracks"][trackname]['rootnote']
    if(mode==None):
        mode=song["mode"]
    if(type(note)==int):
        playNote(trackname, rootnote+nd.getRelNote(mode=mode, note=note), time, restOffset, volume) 
    else:
        td['restOffset']+=time

def playChord(trackname, mode=None, note=0, interval=[0,2,4], time=0.0, restOffset=0.0, volume=1.0):
    td=song['tracks'][trackname]
    track=td["track"]
    rootnote=td['rootnote']
    time=float(time)
    channel=td['channel']
    if(restOffset != 0.0):
        td['restOffset']=restOffset
    if(mode==None):
        mode=song["mode"]
    restOffsetoff=td['restOffset']
    for i in interval:
        if(type(i)==int):
            nt=nd.getRelNote(mode, i+note)        
            track.append(mido.Message('note_on', note=rootnote+nt, channel=channel, velocity=int(127*volume), time=int(td['restOffset']*song['beatLength'])))
            td['restOffset']=0.0
    for i in interval:
        if(type(i)==int):
            nt=nd.getRelNote(mode, i+note)
            track.append(mido.Message('note_off', note=rootnote+nt, channel=channel, velocity=int(127*volume), time=int(time*song["beatLength"])))
            restOffsetoff=0.0
            time=0.0
       
def playArpeggio(trackname, mode=None, note=0, interval=[0,2,4], time=0.0, restOffset=0.0, volume=1.0):
    td=song['tracks'][trackname]
    track=td["track"]
    rootnote=td['rootnote']
    if(mode==None):
        mode=song["mode"]
    if(restOffset != 0.0):
        td['restOffset']=restOffset
    ct=0
    for i in interval:
        tm=0.0
        if(type(time)==int):
            time=float(time)
        if(type(time)==float):
            tm=time/len(interval)
        if(type(time)==list):
            tm=time[ct%len(time)]
            ct=ct+1
        if(type(i)==int):
            playRelNote(trackname, mode=mode, note=note+i, time=tm, volume=volume)
        else:
            if(type(i)==list):
                playChord(trackname, mode=mode, note=note, interval=i, time=tm, restOffset=restOffset, volume=volume)
            else:
                td['restOffset']+=tm

def setName(name):
    song["name"]=name

def setText(text, time=0.0):
    tt=song["tracks"][""]
    t=tt["track"]
    tm=int(song['beatLength']*(tt['restOffset']+time))
    tt['restOffset']=0.0
    t.append(mido.MetaMessage('text', text=text, time=tm))

def setTempo(bpm, time=0):
    song["bpm"]=bpm
    tt=song["tracks"][""]
    t=tt["track"]
    song["tempo"]=mido.bpm2tempo(bpm)
    song["beatLength"]=clocks_per_click*20#(song["tempo"]*4)/1000
    tm=int(song['beatLength']*(tt['restOffset']+time))
    tt['restOffset']=0.0
    t.append(mido.MetaMessage('set_tempo', tempo=song['tempo'], time=tm))

def setTimeSignature(n=4, d=4, time=0.0): #starting time signature
    song["time_n"]=n
    song["time_d"]=d
    tt=song["tracks"][""]
    t=tt["track"]
    tm=int(song['beatLength']*(tt['restOffset']+time))
    tt['restOffset']=0.0
    t.append(mido.MetaMessage('time_signature', 
        numerator=song['time_n'], denominator=song['time_d'], 
        clocks_per_click=clocks_per_click, 
        notated_32nd_notes_per_beat=8, time=tm))

def setKeySignature(key, mode, time=0.0):
    song["mode"]=mode
    song["key"]=key
    t=song["tracks"][""]["track"]
    ks=key
    if(mode=='minor'):
        ks=key+'m'
    t.append(mido.MetaMessage('key_signature', key=ks, time=int(time*song['beatLength'])))

def changeProgram(trackname, prg):
    track=song['tracks'][trackname]['track']
    channel=song['tracks'][trackname]['channel']
    if(type(prg)==int):
        print(track.name+", "+str(prg))
        track.append(mido.Message('program_change', channel=channel, program=prg, time=0))


def addTrack(label, program=None, drum=False):
    track=mido.MidiTrack()
    track.name=label
    song["tracks"][label]={ 'drum':drum }    #place to save track info
    if(drum):
        song['tracks'][label]['channel']=9
    else:
        song['tracks'][label]['channel']=song["nextChannel"]
        song["nextChannel"]+=1
        if(song["nextChannel"]==9):
            song["nextChannel"]+=1

    song["tracks"][label]["track"]=track
    
    song["tracks"][label]["phrase"]=[]          #phrases are made of N full measures. any time missing will be rests.
    song["tracks"][label]["program"]=program

    song['tracks'][label]['restOffset']=0.0      #pads measure with rests if needed when rendering phrase
    song["midi"].tracks.append(track)
    if(program != None):
        changeProgram(label, program)
    return track

def new():
    song["midi"]=mido.MidiFile(type=1)
    song["tracks"]={}    
    song["beatLength"]=clocks_per_click*2
    addTrack("", None)

    song["phraseGroup"]=[]      #phraseGroups are groups 1..N phrases with basenote
    song["sentence"]=[]         #sentences are made of 1..N phrase groups
    song["verse"]={}            #verses are made of 1..N sentences
                                #all tracks should have synchronized verses 
    return song

def setRootNote(trackname, note):
    song['tracks'][trackname]["rootnote"] = note

def getMeasureLength():
    return song['time_n']

def getTrackPhraseLength(trackname, phraseIDX):
    t=song['tracks'][trackname]
    phraseLength=0.0
    if(phraseIDX<len(t['phrase'])):
        for nt in t['phrase'][phraseIDX]:
            if(type(nt['time'])==list):
                for i in nt['time']:
                    phraseLength+=i
            else:
                phraseLength+=nt['time']
    return phraseLength
    
def getPhraseLength(phraseIDX):
    totalPhraseLength=0.0
    for tn in song["tracks"]:
        phraseLength=getTrackPhraseLength(tn, phraseIDX)
        if(phraseLength>totalPhraseLength):
            totalPhraseLength=phraseLength
    return totalPhraseLength

def copyToPhrase(phraseIDX, trackname, phraseIDX_S, note=0, mode=None, dup=1):
    t=song["tracks"][trackname]    
    while(len(t["phrase"])<=phraseIDX):
        t['phrase'].append([])
    if(type(phraseIDX_S)==int):
        phraseIDX_S=[phraseIDX_S]
    while(dup>=1):
        for sidx in phraseIDX_S:
            if(sidx!=phraseIDX):
                for p in t["phrase"][sidx]:
                    phrase={ "notetype":p['notetype'], "mode":mode, "note":note, "interval":p['interval'], "time":p['time'],"volume" :p['volume']}
                    t['phrase'][phraseIDX].append(phrase)
        dup-=1

def addToPhrase(phraseIDX, trackname, notetype, note, mode=None, interval=[0,2,4], time=1.0, timesignature=None, dup=1, volume=1.0):   #notetype is note, chord or arpeggio. None note value is a rest
    t=song["tracks"][trackname]    
    while(len(t["phrase"])<=phraseIDX):
        t['phrase'].append([])
    while(dup>=1):
        dup-=1
        t['phrase'][phraseIDX].append({ "notetype":notetype, "mode":mode, "note":note, "interval":interval, "time":time, "volume":volume })
 
def addToPhraseGroup(phraseGroupIDX, phraseIDXs, noteoffset=0, keyoverride=None):    
    if(type(noteoffset)==int):
        noteoffset=[noteoffset]
    for offset in noteoffset:
        if(type(phraseIDXs)==int):
            phraseIDXs=[phraseIDXs]
        for phraseIDX in phraseIDXs:
            while(len(song["phraseGroup"])<=phraseGroupIDX):
                song['phraseGroup'].append([])
            song['phraseGroup'][phraseGroupIDX].append({"phraseIDX":phraseIDX, 'noteoffset':offset, 'keyoverride':keyoverride})

def addToSentence(sentenceIDX, phraseGroupIDXs, noteoffset=0, keyoverride=None):
    if(type(phraseGroupIDXs)==int):
        phraseGroupIDXs=[phraseGroupIDXs]
    for phraseGroupIDX in phraseGroupIDXs:
        while(len(song["sentence"])<=sentenceIDX):
            song['sentence'].append([])
        song['sentence'][sentenceIDX].append({"phraseGroupIDX":phraseGroupIDX})

def addToVerse(verseName, sentenceIDXs, noteoffset=0, keyoverride=None):
    if(type(sentenceIDXs)==int):
        sentenceIDXs=[sentenceIDXs]
    for sentenceIDX in sentenceIDXs:
        if(verseName not in song['verse']):
            song['verse'][verseName]=[]
        song['verse'][verseName].append(sentenceIDX)
    
def renderPhrase(phraseData, noteoffset=0, keyoverride=None):
    phraseLength=0
    for tn in song['tracks']:
        totalPhraseLength=0.0
        trackPhraseLength=0.0
        track=song['tracks'][tn]
        #changeProgram(tn, track["program"])
        if(phraseData['noteoffset']!=0):
            noteoffset=phraseData['noteoffset']
        if(type(phraseData['keyoverride'])!=None):
            keyoverride=phraseData['keyoverride']
        if(track['drum']): 
            keyoverride='chromatic'
            noteoffset=0
        phraseIDXs=phraseData['phraseIDX']
        if(type(phraseIDXs)==int):
            phraseIDXs=[phraseIDXs]
        for phraseIDX in phraseIDXs:
            trackPhraseLength+=getTrackPhraseLength(tn, phraseIDX)
            totalPhraseLength+=getPhraseLength(phraseIDX)
            if(phraseIDX<len(track['phrase'])):
                phraseList=track['phrase'][phraseIDX]
                for phrase in phraseList:                
                    mode=phrase['mode']
                    if(type(keyoverride)==str):
                        mode=keyoverride
                    if(phrase['notetype']=='arpeggio'):
                        playArpeggio(tn, mode=mode, note=phrase['note']+noteoffset, interval=phrase['interval'], time=phrase['time'], volume=phrase['volume'])
                    else:
                        if(phrase['notetype']=='chord'):
                            playChord(tn, mode=mode, note=phrase['note']+noteoffset, interval=phrase['interval'], time=phrase['time'], volume=phrase['volume'])
                        else:
                            if(phrase['notetype']=='note'):
                                playRelNote(tn, mode=mode, note=phrase['note']+noteoffset, time=phrase['time'], volume=phrase['volume'])
                            else:
                                track['restOffset']+=phrase['time']
        phraseLength=totalPhraseLength
        rest=totalPhraseLength-trackPhraseLength
        if(rest>0):
            track['restOffset']+=rest        
    return phraseLength

def renderPhraseGroup(phraseGroupIDX, noteoffset=0, keyoverride=None):
    length=0
    for phrase in song['phraseGroup'][phraseGroupIDX]:
        length+=renderPhrase(phrase, noteoffset=noteoffset, keyoverride=keyoverride)
    measureBeats=math.ceil(length/getMeasureLength())*getMeasureLength()
    rest=measureBeats-length
    if(rest>0):
        for tn in song['tracks']:
            td=song['tracks'][tn]
            td['restOffset']+=rest

def renderSentence(sentenceIDX, noteoffset=0, keyoverride=None):
    for group in song['sentence'][sentenceIDX]:
        renderPhraseGroup(group['phraseGroupIDX'], noteoffset=noteoffset, keyoverride=keyoverride)

def renderVerse(verseName, noteoffset=0, keyoverride=None):
    setText(verseName)
#    print("rendering "+verseName)
    for sentence in song['verse'][verseName]:
        renderSentence(sentence, noteoffset=noteoffset, keyoverride=keyoverride)

def render(verseList):
    if(verseList==None):
        verseList=song['verse']
    for verseName in verseList:
        renderVerse(verseName)

def save(name=None, verseList=None):
    render(verseList)
    if(name==None):
        name=song['name']
    song["midi"].save(name+".mid")


