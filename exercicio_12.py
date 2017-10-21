#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 12 - Algoritmo de Gauss para raises primitivas de U(p)

from math import sqrt

def mdc(a, b): #Algoritmo Eucilidiano do M.D.C
    while(a%b != 0):
        a, b, q = b, a%b, a/b
    return b

def fatoracaoIngenua(x):
    fat_list = []
    if(x%2 == 0): #Testa se 'x' e par.
        m = 0
        while(x%2 == 0):
            x /= 2
            m += 1
        print('2 %d') %(m)
        fat_list.append((2, m))

    #Todos os impares entre 3 e raiz de x.
    for f in range(3, int(sqrt(x)+1), 2):
        m = 0
        while(x%f == 0): #Enquanto 'x' for divisivel por 'f'.
            x /= f
            m += 1
        if(m != 0): #Verifica se a potencia 'm' de 'f' e diferente de 0.
            print('%d %d') %(f, m)
            fat_list.append((f, m))
    if(x > 1): #Verifica se sobrou mais algum divisor para 'x'.
        print('%d 1') %(x)
        fat_list.append((x, 1))
    return fat_list

def algoritmoDeGaus(p, fat_list):
    i, g, k = 0, 1, len(fat_list)
    while (i < k):
        a = 2
        q_i, e_i = fat_list[i] #Fator, Multiplicidade.
        #Enquanto a^((p - 1) / (q_i^e_i)) = 1 (mod p).
        while((a**((p-1)/q_i)) % p == 1):
            a += 1
        h = (a**((p-1)/(q_i**e_i))) % p
        g = (g*h)%p
        i += 1
        print('%d %d %d') %(q_i, a, h)
    return g

def listaDeGeradores(g, p): #Todos os geradores de U(p).
    n = p - 1
    gen_list = [g]
    for m in range(2, n):
        if(mdc(m, n) == 1):
            gen_list.append(int((g**m)%p))
    gen_list.sort()
    return gen_list


k = input()
fat_list = []
for i in range(k):
    p = input()
    fat_list = fatoracaoIngenua(p-1)
    g = algoritmoDeGaus(p, fat_list)
    print g
    print listaDeGeradores(g, p)
    print '---'
