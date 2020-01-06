#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 13.1 - Teste de Lucas

from math import sqrt

def fatoracaoIngenua(x):
    fat_list = []
    if(x%2 == 0): #Caso x seja par.
        m = 0
        while(x%2 == 0): #Enquanto 'x' for divisivel por 2.
            x /= 2
            m += 1
        print('2 %d') %(m)
        fat_list.append(2)

    #Todos os impares entre 3 e raiz de x.
    for f in range(3, int(sqrt(x)+1), 2):
        m = 0
        while(x%f == 0): #Enquanto 'x' for divisivel por f.
            x /= f
            m += 1
        if(m != 0): #Verifica se a potencia 'm' de 'f' e diferente de 0.
            print('%d %d') %(f, m)
            fat_list.append(f)

    #Caso tenha sobrado um valor maior
    #que zero apos a fatoracao.
    if(x > 1):
        print('%d 1') %(x)
        fat_list.append(x)
    return fat_list

def potenciacaoModular(a, e, n):
    r = 1
    while(e != 0):
        if(e%2 != 0): #Caso o numero seja par.
            print('%d %d %d S') %(r, a, e)
            r = pow(r*a, 1, n)
            e = (e-1)/2
        else: #Caso o numero seja impar.
            print('%d %d %d N') %(r, a, e)
            e /= 2
        a = pow(a, 2, n)
    print('%d %d %d N') %(r, a, e)
    return r

def testeDeLucas(n):
    expo = n-1
    fatores = fatoracaoIngenua(n-1)

    #Todas as bases tal que 2 =< base =< n - 1.
    for base in range(2, n-1):
        print ('%d\n%d') %(base, expo)
        if(potenciacaoModular(base, expo, n) != 1):
            return 'COMPOSTO'
        achou = False;

        #Teste com os fatores primos de n - 1.
        for fator in fatores:
            print expo/fator
            if(potenciacaoModular(base, expo/fator, n) == 1):
                achou = True;
                break;

        #Verifica se nao apareceu um fator p de n - 1 
        #tal que (base**((n-1)/p)) = 1 (mod n).
        if not achou:
            return 'PRIMO'

    #Caso todas as bases tem fator p de n - 1
    #tal que (base**((n-1)/p)) = 1 (mod n).
    return 'COMPOSTO'


m = input()
for i in range(m):
    n = input()
    print testeDeLucas(n)
    print '---'
