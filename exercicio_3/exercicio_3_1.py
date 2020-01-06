#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 3.1 - Equacoes Diofantinas Lineares

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

def solucaoDiofantina(x, y, c, mdc): #Funcao para encontrar a equacao diofantina.
    if(c%mdc != 0): #Se c nao for divisivel pelo MDC de 'a' e 'b'.
        print 0
    else: #Se c for divisivel pelo MDC de 'a' e 'b'.
        c2 = c/mdc
        print ('%d %d') %(x*c2, y*c2)


n = int(input())

for i in range(0, n):
    a, b, c = input()
    mdc, x, y = euclidianoEstendido(a, b)
    solucaoDiofantina(x, y, c, mdc)
    print '---'
    
