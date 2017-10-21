#Aluno: Jose Victor Medeiros Thome da Silva.
#Exercicio 3 - Crivo de Erastotenes

from math import sqrt

def crivo(n): #Crivo de Erastotenes sem usar indices do vetor.
    v = [x for x in range(3, n+1, 2)] #Lista completa.
    values = [x for x in range(3, n+1, 2)] #Lista de teste.
    limit = int(sqrt(n)) #Limite de corte.
    
    print v #Imprime a lista de impares.
    print limit #Imprime a raiz de 'n'.

    p = 3
    while(p < limit): #Enquanto 'p' for menor que raiz de 'n'.
        try:
            values.index(p) #Verifica se 'p' esta na lista de teste.
        except ValueError:
            p += 2	#Incrementa 'p' se o mesmo nao estiver na lista de teste.
            continue
        cut = [] #Lista de corte.

		#Imprime 'p', 'p**2' e o indice de 'p**2' na lista de teste.
        print ('%d %d %d') %(p, pow(p, 2), v.index(pow(p,2)))

		#Loop contando todos os multiplos de 'p' a partir de 'p**2'.
        for i in range(pow(p, 2), n, 2*p):
            cut.append(i) #Insere 'i' na lista de corte.
            try:
                values.remove(i) #Remove 'i' da lista de teste.
            except ValueError:
                continue
        print cut #Imprime a lista de corte.
        print values #Imprime a atual lista de teste.
        p += 2

	#Insere 2 no inicio da lista de primos.
    values.insert(0, 2)
	#Retorna a lista de teste contendo todos os primos ate n.
    return values

n = int(input())
print crivo(n)
