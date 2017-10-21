#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 8.2 - Teste de Composicao

def modulo(b, m): #b (mod m)
    return b%m

def testeComposto(a, e, n): #Teste da composicao.
    r = 1
    while(e != 0):
        if(e%2 != 0): #Verifica se 'e' e impar.
            print('%d %d %d S') %(r, a, e)
            r = modulo(r*a, n)
            e = (e-1)/2
        else: #Caso 'e' nao seja impar.
            print('%d %d %d N') %(r, a, e)
            e /= 2
        a = modulo(a*a, n)
    print('%d %d %d N') %(r, a, e)
    
    if(r == 1): #Verifica se a**(n-1) = 1 (mod n).
        print 'INCONCLUSIVO'
    else:
        print 'COMPOSTO'


n = input()
for i in range(0, n):
    m, a = input()
    testeComposto(a, m-1, m)
    print '---'
