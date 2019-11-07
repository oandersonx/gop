import socket, EnviarMensagem
import json
import RemoveCarac

# Intantianre object s to work with sockets
so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind works to head conections. use " " to hear any IP conection in that port.
so.bind(("", 9999))

# Accept just 1 conection in the socket
so.listen(1)

# Instantiate object sc. s.accept  return 2 values, IP and Port from new conection
sco, addri = so.accept()

while True:
    
    try:
        # Receiving client messages. Method recv receive data and 1024 is the amount of bytes
        recebido = sco.recv(1024).decode()
        print(str(addri), ": ", recebido)
        print("Tamanho do texto, ", len(recebido.split()))
        
        noCarc = RemoveCarac.chr_remove(recebido, "$%_,?.!#&''""'#+`´’")
        
        msg = EnviarMensagem.enviarMensagem(noCarc)
        
        print('Palavras erradas\n', msg)
        
       
       
        '''---Envio de volta ao ClientMachine---'''
        
        palavrasErradas = json.dumps(msg)
        print('Palavras Erradas: ',palavrasErradas)
        sco.send(palavrasErradas.encode())
       
        print('Enviado ao cliente...\n')
        break
    
    
    except Exception as e:
        print('ERRO\n', e)
        break

sco.close()  # Conexao IP e o Socket
so.close()





