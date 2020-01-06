#Aluno: Jose Victor Medeiros Thome da Silva
#Exercicio 6.1 - Operacoes com aritmetica modular.

def aritModular(a, b, n): #Opreracoes com aritmetica modular.

    redu_a = pow(a, 1, n)     #redu_a = a (mod n)
    redu_b = pow(b, 1, n)     #redu_b = b (mod n)
    sum_a_b = pow(a+b, 1, n)  #sum_a_b = (a + b) (mod n)
    sub_a_b = pow(a-b, 1, n)  #sub_a_b = (a - b) (mod n)
    prod_a_b = pow(a*b, 1, n) #prod_a_b = (a * b) (mod n)

    return redu_a, redu_b, sum_a_b, sub_a_b, prod_a_b


turns = input()

for i in range(0, turns):
    a, b, n = input()
    a, b, sum_a_b, sub_a_b, prod_a_b = aritModular(a, b ,n)

    print('%d %d %d %d %d') %(a, b, sum_a_b, sub_a_b, prod_a_b)
