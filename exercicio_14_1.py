#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 14.1 - Fatores de Numeros de Mersene

from math import sqrt

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

def fatoresMersene(p):
	mp = (2**p) - 1 #M(p)
	print mp
	maxR = int((sqrt(2**p) - 1) / (2*p))
	print maxR
	for r in range(1, maxR+1):
		print r
		q = 1 + 2*r*p
		if (potenciacaoModular(2, p, q) == 1):
			return q
	return mp

k = input()
for i in range(k):
	p = input()
	print fatoresMersene(p)
	print '---'
