# EXERCÍCIO 01
import random
lista=[]

lista=random.randint(0,100)

print(f"Valor da lista: {lista}")

# EXERCÍCIO 02
lista=[]

for i in range(0,3):
    num=int(input("Digite um número: "))
    lista+=[num]

print(lista)

# EXERCICIO 03
frase=str(input("Digite uma frase: "))

for palavra in frase:
    palavra=frase.split()
    
print(palavra)

# EXERCICIO 04
lista=[]
i=1

for i in range(1,11):
    lista+=[i]
    i+=1

print(lista)
print(list(reversed(lista)))

# EXERCICIO 05
