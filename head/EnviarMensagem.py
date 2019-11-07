import socket
import json
import DivideTexto

def enviarMensagem(mensagem):
    print("Entrou em Enviar Mensagem\n")
    soc = []
    '''---- Criando sockets-----'''
    
    for i in range(3):
        soc.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    print("Criou o socket\n")
    
    '''--- Atribuindo PORTAS-----'''
    p = [1250, 1350, 1450]
    ip = ['192.168.0.123', '192.168.0.123', '192.168.0.123']
    at = []
    inat = []

    while True:
        
        try:
            
            for i in range(3):
                
                try:
                    soc[i].connect((ip[i], p[i]))
                    print('Conectou com o pc {}'.format(i + 1))
                    recebido = soc[i].recv(1024).decode()
                                      
                    if (recebido == 'Computador Ativo'):
                        at.append(i)
                except Exception as e:
                    print('O computador {} nao conectou'.format(i+1))
                    inat.append(i)
                
                
                
                    
                
                    
                    
                    
                
            print('Tamanho da Lista at: ', len(at))
            sat = []
            for i in at:
                sat.append(i + 1)
            print('Ativo:',sat)
            print('Tamanho da Lista inat: ', len(inat))
            sinat = []
            for i in inat:
                sinat.append(i + 1)
            print('Inativo:', sinat)
                    
                    
               
                    
                
    
        except Exception as e:
            print('Deu erro no primeiro try', e)
        
        
        try:
            
            
            textoQuebrado = DivideTexto.divideTexto(mensagem, len(at))
            
            for i in range(len(at)):
                print('Texto Quebrado: ', textoQuebrado[i])
            
            for i in range(len(at)):
                print('Quantidade de palavras analisadas No {}:'.format(at[i]+1), len(textoQuebrado[i]))
                print('Node {} analisará: '.format(at[i]+1), textoQuebrado[i])
                
            
            
            
            
            print('----- Enviando ao Cliente------\n')
            send_msg = []
            for i in range(len(at)):
                send_msg.append(json.dumps(textoQuebrado[i]))
                
            print('Send_msg posicao 0:', send_msg[0])
            
            for i in range(len(at)):
                soc[i].send(send_msg[i].encode())
                
                print('Mensagem enviada ao Cliente:{} '.format(i + 1))

            
            
          
            msg = []
            
            for i in range(len(at)):
                msg.append(soc[i].recv(1024).decode())
                
                

            
          
                
                
                
                
                
            break
        
        except Exception as e:
            print("\n>> Impossivel Conectar\... ", e)
        break

   
    for i in range(3):
        soc[i].close()
        
    return msg