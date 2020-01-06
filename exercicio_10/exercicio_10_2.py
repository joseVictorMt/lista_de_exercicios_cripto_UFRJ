#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 10.2 - Funcao Totiente de Euler

from math import sqrt

def funcaoTotiente(x):
    fi = 1
    if(x%2 == 0): #Verifica se 'x' e par.
        k = 0
        while(x%2 == 0):
            x /= 2
            k += 1
        print('2 %d') %(k)
        fi *= 2**(k - 1) #Funcao Totiente de Euler

    #Todos os impares entre 3 e raiz de x.
    for p in range(3, int(sqrt(x)+1), 2):
        k = 0
        while(x%p == 0): #Enquanto 'x' e divisivel por 'p'.
            x /= p
            print p
            k += 1
        if(p != 0 and k != 0):
            print('%d %d') %(p, k)
            fi *= (p**(k - 1)) * (p - 1) #Funcao Totiente de Euler
    if(x > 1):
        print('%d 1') %(x)
        fi *= x - 1 #Funcao Totiente de Euler
    return fi


n = input()
for i in range(0, n):
    x = input()
    print funcaoTotiente(x)
    print '---'
