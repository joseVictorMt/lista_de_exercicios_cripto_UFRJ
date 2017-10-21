#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 8.3 - Teorema de Korselt

from math import sqrt

def isCarmichael(x): #Teste para detectar Numeros de Carmichael.
    n = x
    carmichael = True
    if(x%2 == 0): #Verifica se 'x' e par.
        m = 0
        while(x%2 == 0): #Enquanto 'x' for divisivel por 2.
            x /= 2
            m += 1
        print('2 %d') %(m)
        #Teorema de Korselt condicao 1.
        if(m > 1):
            carmichael = False

    #Todos os impares entre 3 e raiz de x.
    for f in range(3, int(sqrt(x)+1), 2):
        m = 0
        while(x%f == 0): #Enquanto 'x' for divisivel por f.
            x /= f
            m += 1
        if(m != 0): #Verifica se a potencia 'm' de 'f' for diferente de zero.
            print('%d %d') %(f, m)
            #Teorema de Korselt condicao 1 e 2.
            if(m > 1 or (n-1)%(f-1) != 0):
                carmichael = False

    if(x > 1):
        print('%d 1') %(x)
        #Teorema de Korselt condicao 2.
        if((n-1)%(x-1) != 0 or x == n):
            carmichael = False
    return carmichael


n = int(input())

for i in range(0, n):
    x = int(input())
    if (isCarmichael(x)):
        print 'SIM'
    else:
        print 'NAO'
    print '---'
