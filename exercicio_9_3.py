#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 9.3 - Potenciacao Modular com Algoritmo Chines do Resto

from math import sqrt

def modulosLista(x): #Lista de modulos com fatoracao ingenua
    mod = [] #Lista de modulos
    if(x%2 == 0): #Testa se 'x' e par.
        m = 0
		#Enquanto 'x' for divisivel por 2.
        while(x%2 == 0):
            x /= 2
            m += 1
        print('2 %d') %(m)
        mod.append(2)

    #Todos os impares entre 3 e raiz de x.
    for f in range(3, int(sqrt(x)+1), 2):
        m = 0
		#Enquanto 'x' for divisor de 'f'.
        while(x%f == 0):
            x /= f
            m += 1
		#Avalia a quantidade de fatores 'f' iguais de 'x' (isto é, x%(f**m) == 0).
        if(m != 0):
            print('%d %d') %(f, m)
            mod.append(f)
	#Verifica se ainda resta algum fator primo no final.
    if(x > 1):
        print('%d 1') %(x)
        mod.append(x)
    return mod

def potenciacaoModular(a, e, n): #Funcao de potenciacao modular.
    #Pequeno Teorema de Fermat
    e %= n-1
    print ('%d') %(e)

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

def congruenciaLista(a, e, mod): #Lista de congruencias.
    congr = []
    for n in mod:
        if((a**e)%n == 0): #Verifica se a**e e congruente a zero.
            print 0
            congr.append(0)
        else: #Caso a**e nao seja congruente a zero.
            congr.append(potenciacaoModular(a, e, n))
    return congr

def euclidianoEstendido(a, b):
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

    return b, x1, y1

def algChinesDoResto(congr, mod): #Algoritmo Chines do Resto
    b, a, b = euclidianoEstendido(mod[0], mod[1])
    print ('%d %d') %(a, b)
    n = mod[0]*mod[1]
    x = congr[0]*mod[1]*b + congr[1]*mod[0]*a
    x %= n
    return x, n


m = input()
congr = [] #Congruencias
mod = [] #Modulos
for i in range(m):
    a, e, mdl = input()
    mod = modulosLista(mdl) #Lista de modulos.
    congr = congruenciaLista(a, e, mod)
    x, n = 0, 0
    for i in range(0, len(congr)-1): #Aplicacao do Algoritmo Chines do Resto.
        x, n = algChinesDoResto([congr[i],congr[i+1]], [mod[i],mod[i+1]])
        print ('%d %d') %(x, n)
        congr[i+1], mod[i+1] = x, n
    print '---'
