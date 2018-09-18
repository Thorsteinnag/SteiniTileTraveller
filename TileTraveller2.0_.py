""" Alogoriðmi: færa punkti í hnitakerfi þer sem hvert hnit er með x-gildi og y-gildi.
    Upphafspunkturinn er x1 , y1 og endapunkturinn x3, y1. 
    Til að færa:
    norður = y + 1
    austur = x + 1
    suður = y - 1
    vestur = x - 1 """ 

"""
Taka punkt sem byrjar á hnitum x, y = 1 og færa hann í gegnum völundarhús. Hann verður að vera innan 1 < x, y < 3.
Eftirfarandi hreyfingar eru ekki leyfðar (veggir):
1,1 -> má bara fara norður
2,2 -> má bara fara suður eða vestur
2,1 -> má bara fara norður
2,3 -> má bara fara vestur eða austur
3,2 -> má bara fara norður eða suður
"""

#Breytur fyrir hreyfingu leikmannsins í völundarhúsinu
x = 1
y = 1

#while lykkja sem keyrir þangað til að x = 3 og y = 1

while x != 3 and y != 1:
