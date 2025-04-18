from drums import *
#implemented drum patterns from http://drummagazine.com/vital-beats-every-drummer-must-know/
_=None
rhythm={}

#one beat per line for readability for 4/4... 3 half-beats for 12/8
rhythm["rock"]=   {"beat":[[kick, cymbal_ride], cymbal_ride, 
                           [snare_2, cymbal_ride], cymbal_ride, 
                           [kick, cymbal_ride], [kick, cymbal_ride], 
                           [snare_2, cymbal_ride], cymbal_ride], "time":4}

rhythm['thing']=  {"beat":[kick, _, _, kick,
                           snare, _, kick, _, 
                           _, _, kick, _, 
                           snare, _, _, _], "time":4}

rhythm["swing"]=  {"beat":[[kick, cymbal_ride], _, _, 
                           [snare_2, hihat_pedal, cymbal_ride], _, cymbal_ride, 
                           [kick, cymbal_ride], _, _, 
                           [snare_2, hihat_pedal, cymbal_ride], _, cymbal_ride], "time":4}

rhythm["reggae"]= {"beat":[_, _, _, 
                           _, _, _, 
                           tom_high, tom_high, tom_high, 
                           tom_high, _, snare, 
                           _, _, _, 
                           cymbal_ride, _, cymbal_ride, 
                           [stick_rim, kick], _, _, 
                           cymbal_ride, _, cymbal_ride], "time":8}

rhythm["hiphop"]= {"beat":[[kick, hihat_closed], _, [kick, hihat_open], _,
                           [snare_2, hihat_closed], _, hihat_closed, kick, 
                           hihat_closed, _, [hihat_closed, kick], kick, 
                           [snare, hihat_closed], _, hihat_closed, kick], "time":4}

rhythm["funk"]=   {"beat":[[kick, hihat_closed], cymbal_ride, hihat_closed, snare, 
                           hihat_closed, _, [hihat_closed, kick], _, 
                           hihat_closed, _, [hihat_open,kick], _, 
                           [snare, hihat_closed], _, hihat_closed, _], "time":4}

rhythm["ska"]=    {"beat":[[kick, hihat_closed], _, hihat_closed, hihat_closed,
                           snare, _, hihat_closed, _,
                           [kick, hihat_closed], _, hihat_closed, _,
                           snare, _, [kick,hihat_closed], _, 
                           [kick, hihat_closed], _, hihat_closed, hihat_closed, 
                           snare, _, hihat_closed, _, 
                           [kick, hihat_closed], _, hihat_closed, _, 
                           [snare, hihat_closed], _, hihat_closed, snare], "time":8}

rhythm["disco"]=  {"beat":[[hihat_pedal, kick], hihat_open, 
                           [hihat_pedal, kick, snare], hihat_open,
                           [hihat_pedal, kick], hihat_open, 
                           [hihat_pedal, kick, snare], hihat_open], "time":4}

rhythm["2bass"]=  {"beat":[[kick, cymbal_ride], kick_2, [kick, cymbal_ride], kick_2,
                           [kick, cymbal_ride, snare], kick_2, [kick, cymbal_ride], kick_2], "time":2}
rhythm["2bass6"]= {"beat":[[kick, cymbal_ride], kick_2, kick, [kick_2, cymbal_ride], kick, kick_2,
                           [kick, cymbal_ride, snare], kick_2, kick, [kick_2, cymbal_ride], kick, kick_2], "time":2}
rhythm["2bassv"]= {"beat":[[kick, cymbal_ride], [kick_2,snare], [kick, cymbal_ride], kick_2,
                           [kick, cymbal_ride, snare], kick_2, [kick, cymbal_ride], [kick_2,snare]], "time":2}

rhythm["ballad"]= {"beat":[[kick, hihat_closed], hihat_closed, 
                           hihat_closed, hihat_closed,
                           [stick_rim, hihat_closed], hihat_closed, 
                           hihat_closed, [kick, hihat_closed],
                           [kick, hihat_closed], hihat_closed, 
                           [kick, hihat_closed], hihat_closed,
                           [stick_rim, hihat_closed], hihat_closed, 
                           hihat_closed, hihat_open], "time":8}

rhythm["pop"]=    {"beat":[[kick, cymbal_ride], cymbal_ride, 
                           [snare_2, cymbal_ride], cymbal_ride, 
                           [kick, cymbal_ride], [kick, cymbal_ride], 
                           [snare_2, cymbal_ride], cymbal_ride], "time":4}

rhythm["punk"]=   {"beat":[[kick, tom_low], _, [kick, tom_low], _, 
                           [snare, tom_low], _, tom_low, tom_high, 
                           [kick, tom_low], _, [kick, tom_low], _,
                           [snare, tom_low], _, tom_low, _, 
                           [kick, tom_low], _, [kick, tom_low], _, 
                           [snare, tom_low], _, tom_low, tom_high, 
                           [kick, tom_low], _, [kick, tom_low], _,
                           [snare, cymbal_crash], _, _, _], "time":8}

rhythm["2line"]=  {"beat":[[kick, snare], snare, snare, [kick,snare],
                           snare, snare, [kick,snare], snare,
                           [kick, snare], snare, snare, [kick,snare],
                           snare, snare, [kick,snare_roll], snare_roll], "time":8}

rhythm["country"]={"beat":[[kick, snare], snare, [snare, hihat_pedal], snare,   #wtf?
                           [kick, snare], snare, [snare, hihat_pedal], snare,
                           [kick, snare], snare, [snare, hihat_pedal], snare,
                           [kick, snare], snare, [snare, hihat_pedal], snare], "time":8}

rhythm["latin"]=  {"beat":[[kick, snare, hihat_closed], _, [snare, hihat_closed, hihat_pedal], [kick, hihat_closed],
                           [kick, hihat_closed], snare, [hihat_pedal, hihat_closed], [kick, snare, hihat_closed],
                           [kick, hihat_closed], snare, [hihat_pedal, hihat_closed], [kick, hihat_closed],
                           [kick, snare, hihat_closed], _, [hihat_pedal, hihat_closed], kick], "time":4}

rhythm["latin2"]= {"beat":[], "time":4} #this thing's a doozy

rhythm["blues"]=  {"beat":[[kick, hihat_closed], hihat_closed, hihat_closed, 
                           [snare, hihat_closed], hihat_closed, hihat_closed,
                           [kick, hihat_closed], hihat_closed, hihat_closed, 
                           [snare, hihat_closed], [kick, hihat_closed], [kick, hihat_closed]], "time":12}

rhythm["shuffle"]={"beat":[[kick, hihat_closed], _, hihat_closed, 
                           [snare, hihat_closed, hihat_pedal], _, hihat_closed, 
                           [kick, hihat_closed], _, hihat_closed,
                           [snare, hihat_closed, hihat_pedal], _, hihat_closed], "time":12}
