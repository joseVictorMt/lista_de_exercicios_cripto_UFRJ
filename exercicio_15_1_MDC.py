#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 15.1 - Decripitacao de mensagens encriptadas com El Gamal

def euclidiano(a, b):
    x2, y2, x1, y1 = 1, 0, 0, 1

    #Enquanto o M.D.C nao for encontrado.
    while(a%b != 0):
		#a = b, b = a%b, q = a/b
        a, b, q = b, a%b, a/b
		#x2 = x1, y2 = y1, x1 = x2 - x1*q, y1 = y2 - y1*q
        x2, y2, x1, y1 = x1, y1, x2 - x1*q, y2 - y1*q

    return x1

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


k = input()
for i in range(k):
    p, a, s, t = input()
    invS = euclidiano(s, p)
    invS = potenciacaoModular(invS, a, p)
    print (invS*t)%p
    print '---'
