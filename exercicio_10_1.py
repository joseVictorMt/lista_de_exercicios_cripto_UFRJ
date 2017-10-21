#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 10.1 - Conjunto dos Elementos Inversiveis em Z(n)

def euclidiano(a, b): #Algoritmo Eucilidiano do M.D.C
    while(a%b != 0):
		#a = b, b = a%b, q = a/b
        a, b, q = b, a%b, a/b
    return b

def conjuntoU(n): #Conjunto dos elementos inversiveis.
    conjU = [] #Lista de elementos inversiveis.
    for b in range(1, n):
        mdc = euclidiano(n, b)
        if(mdc == 1): #Elementos inversiveis.
            conjU.append(b)
    return conjU


n = input()
for i in range(0, n):
    a = input()
    print conjuntoU(a)
