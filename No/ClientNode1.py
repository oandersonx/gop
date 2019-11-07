import socket, AnalisaPalavra1
import json



# usando a conexão socket
st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# recebendo a conexão ip nessa porta.
st.bind(("", 1252))

# aceitando apenas uma conexão no scket
st.listen(1)

# retornando dois valores, o ip e a porta para uma nova conexão.
sct, addrt = st.accept()
print("Entrou")


while True:
    try:
        # Recebendo mensagens do cliente. O método recv recebe dados e 1024 é a quantidade de bytes

        a = 'Computador Ativo'
        sct.send(a.encode())
        mensagem = sct.recv(1024).decode()
        print('MENSAGEM RECEBIDA...\n')
        print(mensagem)
        lista=json.loads(mensagem) #converte a string em lista
        print('Palavras capturadas no texto: ', lista)
        print('Quantidade de palavras: ', len(lista))
        palavrasCorretas = AnalisaPalavra1.analisaPalavra(lista)
        m = json.dumps(palavrasCorretas)# json esta pegando as palavras corretas dentro de uma lista.
        print('M:', m)
        print('Tipo M:', type(m))
        sct.send(m.encode())#retornando a mensagem pro servidor(head)
        print('Enviou ao HeadNode')
        break

    except Exception as e:
        print("Ocorreu un error ", e)

sct.close()
st.close()
print('Enrerrou')