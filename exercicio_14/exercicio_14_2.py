#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 14.2 - "Quebrando" o RSA

from math import sqrt

def chaveDec(a, b): #Chave de decodificacao.
    fi_n = b
    x2, y2, x1, y1 = 1, 0, 0, 1

    #Imprimindo as duas linhas iniciais na lista
    print ('%d - %d %d\n%d - %d %d') %(a, x2, y2, b, x1, y1)

    #Enquanto o M.D.C nao for encontrado.
    while(a%b != 0):
		#a = b, b = resto de a/b, q = divisao inteira a/b.
        a, b, q = b, a%b, a/b
		#x2 = x1, y2 = y1, x1 = x2 - x1*q, y1 = y2 - y1*q.
        x2, y2, x1, y1 = x1, y1, x2 - x1*q, y2 - y1*q
		#Imprime todos os valores se o MDC ainda nao foi encontrado.
        print ('%d %d %d %d') %(b, q, x1, y1)
	#Imprime o resto e o MDC.
    print ('%d %d - -') %(a%b, a/b)

    return fi_n + x1

def fermat(n): #Algoritmo de Fermat para achar fatores de n.
    raiz = int(sqrt(n))
    if(pow(raiz, 2) == n): #Verifica se 'n' e um quadrado perfeito.
        print ('%d %d S') %(raiz, raiz)
        return raiz, raiz

    print ('%d 0 N') %(raiz)
    for x in range(raiz+1, int((n+1)/2)):
        y = int(sqrt(pow(x, 2) - n))
        if((pow(x, 2) - pow(y, 2)) == n):
            print('%d %d S') %(x, y)
            return x-y, x+y
        else:
            print('%d %d N') %(x, y)
    return 1, n

def funcaoTotiente(x): #Funcao Totiente de Euler.
    fi = 1
    if(x%2 == 0): #Verifica se 'x' e par.
        k = 0
        while(x%2 == 0): #Enquanto 'x' for divisivel por 2.
            x /= 2
            k += 1
        fi *= 2**(k - 1) #Funcao Totiente de Euler.

    #Todos os impares entre 3 e raiz de x.
    for p in range(3, int(sqrt(x)+1), 2):
        k = 0
        while(x%p == 0): #Enquanto 'x' for divisivel por 'p'.
            x /= p
            k += 1
        if(k != 0):
            fi *= (p**(k - 1)) * (p - 1) #Funcao Totiente de Euler.
    if(x > 1):
        fi *= x - 1 #Funcao Totiente de Euler.
    return fi

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

def quebraRSA(n, e, b): #Funcao para quebrar o RSA usando o Algoritmo de Fermat.
    fn1, fn2 = fermat(n)
    print('%d %d') %(fn1, fn2)
    fi_n = funcaoTotiente(n)
    print fi_n
    d = chaveDec(e, fi_n)
    print d
    print potenciacaoModular(b, d, n)


k = input()
for i in range(k):
    n, e, b = input()
    quebraRSA(n, e, b)
    print '---'
