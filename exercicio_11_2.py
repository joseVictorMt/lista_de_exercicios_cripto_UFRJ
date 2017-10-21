#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 11.2 - Subgrupos ciclicos de U(n)

def euclidiano(a, b): #Algoritmo Eucilidiano do M.D.C
    while(a%b != 0):
        a, b, q = b, a%b, a/b
    return b

def conjuntoU(n): #Conjunto dos elementos inversiveis
    conjU = []
    for b in range(1, n):
        mdc = euclidiano(a, b)
        if(mdc == 1):
            conjU.append(b)
    return conjU

def subgrupoCiclico(a, n, u): #Subgrupo ciclico
    k = 1
    subgr = [1]
    modulo = (a**k)%n
    while (modulo != 1):
        subgr.append(modulo)
        k += 1
        modulo = (a**k)%n #(a**k) (mod n)
    subgr.sort()
    return subgr

def geradorDeSubgrupos(n, u): #Gera subgrupos ciclicos de 'u(n)'
    for a in u:
        print subgrupoCiclico(a, n, u)


n = input()
u = []
for i in range(n):
    a = input()
    u = conjuntoU(a)
    print u
    geradorDeSubgrupos(a, u)
    print '---'
    
