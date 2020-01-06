#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 2.3 - Algoritmo Euclidiano Estendido

def euclidianoEstendido(a, b):
    x2, y2, x1, y1 = 1, 0, 0, 1
    #Imprimindo as duas linhas de 'a' e 'b' na lista.
    print ('%d - %d %d\n%d - %d %d') %(a, x2, y2, b, x1, y1)
    
	#Enquanto o MDC nao for encontrado.
    while(b > 0):
		#a = b, b = resto de a/b, q = divisao inteira a/b.
        a, b, q = b, a%b, a/b
		#x2 = x1, y2 = y1, x1 = x2 - x1*q, y1 = y2 - y1*q.
        x2, y2, x1, y1 = x1, y1, x2 - x1*q, y2 - y1*q
		#Imprime todos os valores se o MDC ainda nao foi encontrado.
        if(b > 0):
            print ('%d %d %d %d') %(b, q, x1, y1)
	#Imprime o resto 'b' e o MDC 'q'.
    print ('%d %d - -') %(b, q)


n = int(input())

for i in range(0, n):
    a,b = input()
    euclidianoEstendido(a, b)
    print '---'