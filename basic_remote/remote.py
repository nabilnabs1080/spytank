# z: avancer
#q : gauche
# s : reculer
# d : droite
# e/r : led 1 ou 0
# a: stop
# c : exit

import spytank
import time

print("z : avance\nq : gauche\ns : reculer\nd : droite\ne/r : led\na : stop\nc : exit")
print("entre une lettre pour piloter le robot comme dans la description")
continuer = True
while continuer :

    lettre = input(">>")


    if lettre == "z":
        spytank.avance(125)
    elif lettre == "q":
        spytank.gauche(125)
    elif lettre == "s":
        spytank.recule(-125)
    elif lettre == "d":
        spytank.droite(125)
    elif lettre == "a":
        spytank.stop

    elif lettre == "e":
        spytank.led(0,1)
        spytank.led(1,1)
        spytank.led(2,1)
        spytank.led(3,1)
        
    elif lettre == "r":
        spytank.led(0,0)
        spytank.led(1,0)
        spytank.led(2,0)
        spytank.led(3,0)
            
    elif lettre == "a":
        spytank.stop()

    elif lettre == "c":
        spytank.stop()
        continuer = False