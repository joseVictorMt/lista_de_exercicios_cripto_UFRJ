#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 9.2 - Algoritmo Chines do Resto

def modulo(x, n): #x (mod n)
    return x%n

def euclidianoEstendido(a, b):
    x2, y2, x1, y1 = 1, 0, 0, 1

    #Imprimindo as duas linhas iniciais na lista.
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

def algChinesDoResto(congr, mod): #Algoritmo Chines do Resto.
    b, a, b = euclidianoEstendido(mod[0], mod[1])
    print ('%d %d') %(a, b)
    n = mod[0]*mod[1]
    x = congr[0]*mod[1]*b + congr[1]*mod[0]*a
    x = modulo(x, n)
    return x, n


n = input()
congr = []
mod = []
for i in range(0, n):
    congr, mod = input()
    x, n = 0, 0
    for i in range(0, len(congr)-1):
        x, n = algChinesDoResto([congr[i],congr[i+1]], [mod[i],mod[i+1]])
        print ('%d %d') %(x, n)
        congr[i+1], mod[i+1] = x, n
    print '---'
