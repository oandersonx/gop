

'''lista = [
    ['Do mesmo modo, a consulta aos diversos militantes acarreta um processo de reformulacao e modernizacao do fluxo de informacoes.'],
    ['Evidentemente, a determinacao clara de objetivos promove a alavancagem dos niveis de motivacao departamental.'],
    ['Gostaria de enfatizar que a percepcao das dificuldades cumpre um papel essencial na formulacao das diretrizes de desenvolvimento para o futuro.']
]

for i, frase in enumerate(lista):
    lista[i] = frase[0].split()'''


l = 'The cat is beautiful'.split()

print('LLLLL\n',l[3])

'''print(a)

print(a[0:2])
print(a[2:4])
print(a[4:6])


print(a[0:a/3])
print(a[a/3:a/3*2])
print(a[a/3*2:a/3*2*2])
'''



n = 3
splited = []
len_l = len(l)
for i in range(n):
    start = int(i*len_l/n)
    end = int((i+1)*len_l/n)
    splited.append(l[start:end])
print(splited)


for i in splited:
    print()


















