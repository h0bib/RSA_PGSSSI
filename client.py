# YAHIAOUI Hadj Habib | chaos.hh@gmail.com 
# PGS SSI 2018/2019
# Cryptanalyse et factorisation du RSA pour décrypter un message électronique
# Plateforme RSA & Attaques
# Module Client : (partie client de la communication secrete client/serveur)



# This program encrypt a message before sending, so we must have a CipherRSA module in the same folder

import socket
import threading
import sys
import cipherRSA  # Our encryption/decryption module, imported and used to encrypt un message before sending

# Wait for incoming data from server
#.decode is used to turn the message in bytes to a string
def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(32)
            print(str(data.decode("utf-8")))
        except:
            print("You have been disconnected from the server")
            signal = False
            break

#Get host and port
print("---------------------------------------------------------------")
print("         Secret Communication Client  (RSA Encryption)         ")
print("---------------------------------------------------------------")
print(" ")
print("Enter host/ip and Port for the communication server:")
host = input("Host: ")
port = int(input("Port: "))

#Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print("")
    print("Connected to server")
    print("---------------------------------------------------------------")
    print("")
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)

#Create new thread to wait for data
receiveThread = threading.Thread(target = receive, args = (sock, True))
receiveThread.start()

#Send data to server
#str.encode is used to convert the string message into bytes so it can be sent across the network
while True:
    message = input()
    if message=='quit':
        #sock.shutdown(2)
        sock.close()
        #exit()
    modeRSA='encrypt' # to turn the program mode to encryption 
    MessageEncrypted=cipherRSA.encryptMsgtoSend(message, modeRSA)
    sock.sendall(str.encode(MessageEncrypted))
