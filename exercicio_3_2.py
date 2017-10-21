#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 3.2 - Fatoracao Ingenua

from math import sqrt

def fatoracaoIngenua(x):
    if(x%2 == 0): #Verifica se 'x' e par.
        m = 0
        while(x%2 == 0): #Enquanto 'x' for divisivel 2.
            x /= 2
            m += 1
        print('2 %d') %(m) #Imprime 2 e a sua potencia 'm'.

    #Todos os impares entre 3 e raiz de x.
    for f in range(3, int(sqrt(x)+1), 2):
        m = 0
        while(x%f == 0): #Enquanto 'x' for divisivel por 'f'.
            x /= f #Divide 'x' por 'f' a cada loop.
            m += 1 #Incrementa 'm' a cada loop.
		#Verifica se m for diferente de 0, sendo x / (f**m) igual a zero.
        if(m != 0):
            print('%d %d') %(f, m)
	#Verifica se sobrou mais algum fator primo.
    if(x > 1):
        print('%d 1') %(x)


n = int(input())

for i in range(0, n):
    x = int(input())
    if(x == 1):
        print'1 1\n---'
        continue
    fatoracaoIngenua(x)
    print '---'
