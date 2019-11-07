from threading import Thread
import time


'''def carrinho(velocidade,nome):
    distancia = 0
    while distancia <= 10:
        print("Carrinho :",nome,distancia)
        distancia += velocidade
        time.sleep(0.3)



carrinho1 = Thread(target=carrinho,args=[1.1,"Ed"])
carrinho2 = Thread(target=carrinho,args=[1.2,"Paulo"])


carrinho1.start()
carrinho2.start()'''



def Hello(nome):
    cont = 0
    while cont <= 10:
        print('Nome: {}'.format(nome))
        cont += 1
        time.sleep(0.5)


t1 = Thread(target=Hello, args=['Thread 1'])
t2 =  Thread(target=Hello, args=['Thread 2'])


t1.start()
t2.start()

