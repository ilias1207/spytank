import network
import click

ADDRESSE ="10.0.0.113"
PORT = 1111

print("Z: AVANCER\nQ: GAUCHE\nS: RECULER\nD: DROITE\nE/R: LED 1 OU 0\nA: STOP\nC: EXIT")
print("entre une lettre pour piloter le robot comme dans la description")

continuer = True
while continuer:

    socket = network.newClientSocket()
    socket.connect((ADDRESSE,PORT))

    
   
    lettre = click.getchar()
    socket.send(lettre.encode())

    reponse = socket.recv(4096)
    print(reponse)