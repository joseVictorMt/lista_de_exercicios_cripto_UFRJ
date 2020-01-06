#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 2.2 - Algoritmo Euclidiano

def euclidiano(a, b):
    print ('%d\n%d') %(a, b)

    while(b > 0):
        q = a/b	#Divisao inteira de a por b.
        r = a - b*q #Obtencao do resto atraves do teorema da divisao.
        print('%d') %(r) #Inprime o resto obtido em cada loop.
        a = b
        b = r

   
n = int(input())

for i in range(0, n):
    a,b = input()
    euclidiano(a, b)
    print '---'
