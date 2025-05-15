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
lista=["Maçã", "Banana", "Pera", "Morango", "Abacate"]

print(f"Da lista, a menor palavra é: {min(lista)}")
print(f"Da lista, a maior palavra é: {max(lista)}")

# EXERCÍCIO 06
lista=[1,2,3,4,5,6,7,8,9,10]
par=[]
impar=[]

for num in lista:
    if num % 2 == 0:
        par+=[num]
    else:
        impar+=[num]

print(lista)
print(f"Os números pares são: {par}")
print(f"Os números impares são: {impar}")

# EXERCICIO 07
lista=[]
par=[]
impar=[]

for i in range(0,101):
    lista+=[i]

for num in lista:
    if num % 2 == 0:
        par+=[num]

print(lista)
print("="*25)
print(f"Os números pares da lista são: {par}")

# EXERCÍCIO 08
lista=[]
elevado=[]

for i in range(1,11):
    lista+=[i]
    
for num in lista:
    conta=num*2
    elevado+=[conta]

print(lista)
print(elevado)

# EXERCÍCIO 09
