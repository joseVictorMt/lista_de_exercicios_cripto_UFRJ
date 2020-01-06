#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 15.2 - Algoritmo Baby-Step / Giant-Step de Shanks

from math import sqrt

def inverso(a, b):
    x2, y2, x1, y1 = 1, 0, 0, 1

    #Enquanto o M.D.C nao for encontrado.
    while(a%b != 0):
		#a = b, b = a%b, q = a/b
        a, b, q = b, a%b, a/b
		#x2 = x1, y2 = y1, x1 = x2 - x1*q, y1 = y2 - y1*q
        x2, y2, x1, y1 = x1, y1, x2 - x1*q, y2 - y1*q

    return x1

def bsgsShanks(g, h, p): #Algoritmo de Shanks
    m = int(sqrt(p - 1)) + 1
    print m
    b = []
    
    for j in range(m): #Baby Step
        s = (g ** j)%p
        b.append(s)
        print('%d %d') %(j, s)
    invG = inverso(g, p)
    t = (invG**m)%p
    
    for i in range(m): #Giant Step
        s = (h*(t**i))%p
        print('%d %d') %(i, s)
        if(s in b):
            j = b.index(s)
            print('%d %d') %(i, j)
            return i*m+j


k = input()
for i in range(k):
    g, h, p = input()
    print bsgsShanks(g, h, p)
    print '---'
