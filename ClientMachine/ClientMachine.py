import json
import socket
from time import gmtime, strftime

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        
        ip = "192.168.0.123"
        s.connect((ip, 9999))
        break
    except Exception as e:
        print("ERRO..Possivel problema na rede..")
    break

while True:
    arquivo = open('analise.txt', 'r')
    show = arquivo.read()
    
    localtime = strftime("%H:%M:%S", gmtime())
    
    s.send(show.encode())

    
    palavras_erradas = s.recv(1024).decode()
    
    
    print('Recebido: ', palavras_erradas)
    print('Recebido 1:',palavras_erradas[0])
    print('Recebido 2:',palavras_erradas[1])
    
    break

s.close()
