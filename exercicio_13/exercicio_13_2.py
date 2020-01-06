#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 13.2 - Teste de Pepin

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

def testeDePepin(k):
    f_k = ((2**(2**k)) + 1) #F(k) = 2^(2^k) + 1
    print f_k
    congr = potenciacaoModular(5, (f_k-1)/2, f_k)
    if(f_k - congr == 1):
        return 'PRIMO'
    return 'COMPOSTO'


n = input()
for i in range(n):
    k = input()
    print testeDePepin(k)
    print '---'
