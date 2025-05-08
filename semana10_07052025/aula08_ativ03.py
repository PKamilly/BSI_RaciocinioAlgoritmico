# EXERCÍCIO 01
for i in range(1,50):
    print(i)

# EXERCÍCIO 02
par=0

for i in range(1,100):
    print(i)
    if i % 2 == 0:
        par+=1

print(f"Foram encontrados {par} números pares.")

# EXERCÍCIO 03
valorInt=int(input("Digite um valor inteiro entre 0 e 10: "))

if 0<=valorInt<=10:
    for i in range(0,11):
        multi=valorInt*i
        print(multi)
else:
    print("Digite um número inteiro válido!")


# EXERCÍCIO 04
idades=[0]*5
media=0
soma=0

for i in range(0,5):
    idade=int(input("Digite uma idade: "))
    idades[i]+=idade
    soma+=idades[i]
    media=soma/5

print("============")
print(idades)
print(media)

# EXERCÍCIO 05
num=0
par=0
impar=0

for i in range(1,10):
    num=int(input("Digite um número: "))
    if num % 2 == 0:
        par+=1
    else:
        impar+=1

print(f"Foram encontrados {par} números pares.")
print(f"Foram encontrados {impar} números impares.")

# EXERCÍCIO 06


# EXERCÍCIO 07


# EXERCÍCIO 08


# EXERCÍCIO 09


# EXERCÍCIO 10


# EXERCÍCIO 11

