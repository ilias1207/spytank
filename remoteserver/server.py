import network
import spytank

ADDRESS ="10.0.0.113"
PORT=1111

socket = network.newServerSocket()
socket.bind((ADDRESS,PORT))
continuer = True

while continuer: 
    socket.listen(10)
    print("en écoute...")

    thread = network.newThread(socket.accept())
    thread.start()
    #notre communication

    lettre = thread.clientsocket.recv(4096)
    lettre = lettre.decode("utf-8")

    print("message reçu : ", lettre)
    
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
    spytank.stop()
elif lettre == "c" :
    spytank.stop()
    continuer=False

    thread.clientsocket.send("j'ai bien reçu le message".encode())