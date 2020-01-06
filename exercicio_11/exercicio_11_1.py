#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 11.1 - Subgrupo de U(n)

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

def ehSubgrupo(n, subcj): #Teste de subgrupo em 'u(n)'
    u = conjuntoU(n)
    if 1 not in subcj: #Verifica se o elemento neutro esta em 'subcj'
        return False
    for a in subcj:
        if a not in u: #Verifica se 'a' esta em 'u(n)'
            return False
        inverso = False
        for b in subcj:
            modulo = (a*b)%n
            if modulo not in subcj: #Verifica se 'a*b (mod n)' esta em 'subcj'
                return False
            if (modulo == 1): #Verifica se o inverso de 'a' esta em 'subcj'
                inverso = True
        if not inverso:
            return False    
    return True


n = input()
subgr = []
for i in range(n):
    a, subcj = input() # a sendo um inteiro e subcj sendo uma lista de inteiros
    if(ehSubgrupo(a, subcj)):
       print 'SIM'
    else:
       print 'NAO'
