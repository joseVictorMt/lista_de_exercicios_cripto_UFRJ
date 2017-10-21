#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 7 - Inverso Multiplicativo

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

def inversoMultiplicativo(mdc, a, b, x):
    if(mdc != 1): #Verifica se 'a' e 'b' nao sao primos entre si.
        return 0
    if(x < 0): #Verifica se o valor de x na equacao ax + by = 1 e negativo.
        return b+x
    return x

n = input()
for i in range(0, n):
    a, b = input()
    mdc, x, y = euclidianoEstendido(a, b)
    print inversoMultiplicativo(mdc, a, b, x)
    print '---'
