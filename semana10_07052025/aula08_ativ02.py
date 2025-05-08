# EXERCICIO 01
for i in range(1,11):
    print(i)

# EXERCÍCIO 02
vetor=[1,2,3,4,5]

for i in range(5):     #For I
    print(vetor[i])

for numero in vetor:  #For EACH
    print(numero)

# EXERCÍCIO 03
soma=0

for i in range(1,11):
    soma+=i

print(f"O resultado da soma é {soma}")

# EXERCÍCIO 04
vetor=[2,7,5,12,29]
soma=0

for valor in vetor:
    soma+=valor

print(f"O resultado da soma é {soma}")

# EXERCÍCIO 05
import random
vetor=[0]*10

for i in range(10):
    vetor[i]=random.randint(1,100)

num=int(input("Digite um numero: "))

for i in range(10):
    if numero==vetor[i]:
        print(f"O numero digitado foi {numero} na posição {i}")
        break
    else:
        print(f"O numero digitado não está na lista")
        