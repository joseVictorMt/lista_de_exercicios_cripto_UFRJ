#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 3.3 - Algoritmo de Fermat

from math import sqrt

def fermat(n):
    raiz = int(sqrt(n))
    if(pow(raiz, 2) == n): #Verifica se n e um quadrado perfeito.
        print ('%d %d S') %(raiz, raiz)
        return raiz, raiz #n = raiz * raiz

    print ('%d 0 N') %(raiz)

	#Algoritmo de fermat.
    for x in range(raiz+1, int((n+1)/2)):
        y = int(sqrt(pow(x, 2) - n))
        if((pow(x, 2) - pow(y, 2)) == n): #Verifica se x**2 - y**2 = n.
            print('%d %d S') %(x, y)
			#Retorna os dois fatores de n, ou seja, n = (x-y) * (x+y)
            return x-y, x+y
        else: #Imprime 'x' e 'y' se a verificacao nao for verdadeira.
            print('%d %d N') %(x, y)
	#Retorna 1 e 'n' como fatores se o algoritmo constatar que 'n' e primo. 
    return 1, n


n = int(input())

for i in range(0, n):
    x = int(input())
    a, b = fermat(x)
    print ('%d %d\n---') %(a, b)
