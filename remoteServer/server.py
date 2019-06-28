import network
import spytank

ADDRESS="10.0.0.113"
PORT=1111

socket = network.newServerSocket()
socket.bind((ADDRESS,PORT))

continuer = True

while continuer:
    socket.listen(10)
    print("en ecoute...")

    thread = network.newThread(socket.accept())
    thread.start()

    #notre communication

    lettre = thread.clientsocket.recv(4096)
    lettre = lettre.decode("utf-8")

    print("message recu : ", lettre)

    if lettre == "z":
        spytank.avance(255)
    elif lettre == "q":
        spytank.gauche(255)
    elif lettre == "s":
        spytank.recule(255)
    elif lettre == "d":
        spytank.droite(255)
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
    
    thread.clientsocket.send("j'ai bien recu le message".encode())