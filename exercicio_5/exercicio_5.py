#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 5 - Numeros Altamente Compostos

def contDivisores(a): #Contador de divisores sem o operando '%'.
    cont = 0
    for n in range(1, a+1):
		#Verifica se a e congruente com 0 (mod n), isto e, a%n == 0.
        if (pow(a, 1, n) == 0):
            cont +=1
	#Retorna a quantidade de divisores de 'a'.
    return cont

def altamenteCompostos(n): #Listagem dos numeros altamente compostos ate n.
    maior = 0
    alt_comps = [] #Lista de numeros altamente compostos.
    for i in range(1, n+1):
        divs = contDivisores(i)
		#Verifica se 'i' tem a maior quantidade de divisores nesse momento.
        if(maior < divs):
            alt_comps.append(i)
            maior = divs
	#Retorna a lista de numeros altamente compostos ate 'n'.
    return alt_comps


x = int(input())
print altamenteCompostos(x)
