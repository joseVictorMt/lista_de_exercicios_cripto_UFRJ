#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 15.1 - Decripitacao de mensagens encriptadas com El Gamal

def potenciacaoModular(a, e, n):
    #Pequeno Teorema de Fermat
    e %= n-1

    #Potenciacao Modular
    r = 1
    while(e != 0):
        if(e%2 != 0): #Testa se 'e' e impar.
            print('%d %d %d S') %(r, a, e)
            r =(r*a)%n
            e = (e-1)/2
        else: #Caso 'e' seja par.
            print('%d %d %d N') %(r, a, e)
            e /= 2
        a = (a*a)%n
    print('%d %d %d N') %(r, a, e)
    return r

def decriptMessageElGamal(p, a, s, t): #Decriptador do El Gamal
    invS = potenciacaoModular(s, p-1-a, p)
    return (invS*t)%p


k = input()
for i in range(k):
    p, a, s, t = input()
    print decriptMessageElGamal(p, a, s, t)
    print '---'
