import socket
import No1, No2, defthreadServer
from threading import Thread
# Intantianre object s to work with sockets
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind works to head conections. use " " to hear any IP conection in that port.
s.bind(("", 9999))

# Accept justl 1 conection in the socket
s.listen(3)

# Instantiate object sc. s.accept  return 2 values, IP and Port from new conection
sc, addr = s.accept()
t =['t1','t2', 't3']

while True:
    
    try:
        # Receiving client messages. Method recv receive data and 1024 is the amount of bytes
        recibido = sc.recv(1024).decode()
        
        
        for i in t:
            t[i] = Thread(target=defthreadServer.Send(recibido))
            t[i].start()
        
    except Exception as e:
        print("Ha ocurrido un error ", e)
        break
        
        if recibido == "close":
            # break the while bucle
            break
        
        if recibido == "hello":
            print("Comando recibido!")
    
    # Enviando a nó 1
    
    except Exception as e:
        print("Ha ocurrido un error ", e)
        break

print("Adios.")

sc.close()
s.close()