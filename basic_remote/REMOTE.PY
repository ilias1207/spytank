# Z: AVANCER
# Q: GAUCHE
# S: RECULER
# D: DROITE
# E/R: LED 1 OU 0
# A: STOP
# C: EXIT

import spytank
import time

print("Z: AVANCER\nQ: GAUCHE\nS: RECULER\nD: DROITE\nE/R: LED 1 OU 0\nA: STOP\nC: EXIT")
print("entre une lettre pour piloter le robot comme dans la description")
lettre = input(">>")

if lettre == "z" : 
    spytank.avance(125)
elif lettre == "q" : 
    spytank.gauche(125)
elif lettre == "s" : 
    spytank.droite(125)
elif lettre == "d" : 
    spytank.recule(125)
elif lettre == "e" : 
    spytank.led(0,1)
    spytank.led(0,1)
    spytank.led(0,1) 
    spytank.led(0,1)
elif lettre == "a" : 
    spytank.stop(125)
elif lettre == "c" : 
    spytank.exit(125)