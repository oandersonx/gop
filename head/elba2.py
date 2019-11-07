import socket
import Maiusculo
st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

st.bind(("", 1238))
st.listen(1)
sct, addrt = st.accept()

print('Entrou no Elba2\n')

while True:
    try:
        mensagem = sct.recv(1024).decode()
        print('MENSAGEM RECEBIDA...\n')
        print(mensagem)

        msg = Maiusculo.maiusculo(mensagem)
        try:
            sct.send(msg)
            print('Enviou msg maiuscula')
        except Exception as e:
            print('Erro msg maiuscula,  ', e)
        break
      
    except Exception as e:
        print('Ocorreu um erro\n ', e)
        break
        
sct.close()
st.close()