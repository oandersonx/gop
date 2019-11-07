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
    p = [1252, 1351, 1457]
    ip = ['192.168.0.123', '192.168.0.123', '192.168.0.123']
    status = []
    at = []
    inat = []
    
    while True:
        
        try:
            
            for i in range(3):
                try:
                    soc[i].connect((ip[i], p[i]))
                    print('Conectou com o pc {}'.format(i + 1))
                    print('Socket[{}]'.format(i))
                    recebido = soc[i].recv(1024).decode()
                    
                    if (recebido == 'Computador Ativo'):
                        status.append(i)
                except Exception as e:
                    print('O computador {} nao conectou'.format(i + 1))
                    status.append('*')
            
            '''---------Imprimindo qtd e quais máquinas estão ativas e inativas---------'''
            print('Status: ', status)
            for i in range(len(status)):
                if (status[i] == '*'):
                    inat.append(i)
                else:
                    at.append(i)
            
            '''---- Somando mais 1 para printar---- [0,1] -> [1,2]'''
            sat = []
            for i in at:
                sat.append(i + 1)
            
            sinat = []
            for i in inat:
                sinat.append(i + 1)
            
            print('Quantidade de computadores ativos: ', len(at))
            if (sat == []):
                print('Computadores ativos: ', len(sat))
                print('Nenhum computador ativo')
            else:
                print('Computadores ativos: ', sat)
            
            print('Quantidade de computadores inativos: ', len(inat))
            if (sinat == []):
                print('Computadores inativos: ', len(sinat))
            else:
                print('Computadores inativos: ', sinat)
        
        
        
        
        
        
        
        
        
        
        
        
        except Exception as e:
            print('Deu erro no primeiro try', e)
        
        try:
            
            textoQuebrado = DivideTexto.divideTexto(mensagem, len(at))
            
            for i in range(len(at)):
                print('Texto Quebrado: ', textoQuebrado[i])
            
            for i in range(len(at)):
                print('Quantidade de palavras analisadas No {}:'.format(at[i] + 1), len(textoQuebrado[i]))
                print('Node {} analisará: '.format(at[i] + 1), textoQuebrado[i])
            
            print('----- Enviando ao Cliente------\n')
            send_msg = []
            
            for i in range(len(at)):
                send_msg.append(json.dumps(textoQuebrado[i]))
            
            '''----- Envio aos Nodes ----'''
            
            aux = 0
            for i in status:
                if (i != '*'):
                    soc[i].send(send_msg[aux].encode())
                    print('Mensagem enviada ao Cliente:{} '.format(i + 1))
                    aux += 1
                else:
                    continue
                
                
            
            '''----- Recebe as palavras erradas do Node --- '''
            
            msdd = []
            
            
            copia_status = status

            for h in copia_status:
                if (h == '*'):
                    copia_status.remove('*')

            
            for i in copia_status:
                msdd.append(soc[i].recv(1024).decode())
                
            
            
            print('Lista msdd: ', msdd)
            
            break
        
        except Exception as e:
            print("Erro em EnviarMensagem", e)
        break
    
    for i in range(3):
        soc[i].close()
    
    return msdd
