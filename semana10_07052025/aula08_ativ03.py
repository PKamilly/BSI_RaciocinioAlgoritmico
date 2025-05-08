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
num=0
INIntervalo=0
OFFIntervalo=0

for i in range(0,10):
    num=int(input("Digite um número: "))
    if 10<num<20:
        INIntervalo+=1
    else:
        OFFIntervalo+=1

print(f"Foram encontrados {INIntervalo} números entre 10 e 20.")
print(f"Foram encontrados {OFFIntervalo} números fora de 10 e 20.")

# EXERCÍCIO 07
import random
vetor=[0]*150
par=[0]*50
soma=0
indicePar=0

for i in range(150):
    vetor[i]=random.randint(1,100)
    if vetor[i] % 2 == 0 and indicePar < 50:
        par[indicePar]=vetor[i]
        indicePar+=1
        soma+=vetor[i]
    
print(f"Numeros do vetor: \n{vetor}")
print("===========")
print(f"Numeros pares do vetor: \n{par}")
print("===========")
print(f"Soma dos numeros pares: \n{soma}")

# EXERCÍCIO 08 - DESAFIO
vetores = [0] * 10
posicao = [0] * 10
maior = vetores[0]
menor = vetores[0]

for i in range(0, 10):
    num = int(input("Digite um número: "))
    vetores[i] += num

    if num > maior:
        maior += num[i]

    else:
        print("abobora")


print(vetores)
print(posicao)
print(maior)

# EXERCÍCIO 09


# EXERCÍCIO 10


# EXERCÍCIO 11

