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
# ARRUMAR !!!!!!!!!!!!!!!!!!!!!!
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
consoantes=0
vogais=0
vogalA=0
vogalE=0
vogalI=0
vogalO=0
vogalU=0
i = 1

texto=input("Digite um texto: ")

for letras in texto:
    print(i, "-", letras)

    if letras == "a" or letras == "A":
        vogalA+=1
        vogais+=1
    elif letras == "e" or letras == "E":
        vogalE+=1
        vogais+=1
    elif letras == "i" or letras == "I":
        vogalI+=1
        vogais+=1
    elif letras == "o" or letras == "O":
        vogalO+=1
        vogais+=1
    elif letras == "u" or letras == "U":
        vogalU+=1
        vogais+=1
    else:
        consoantes+=1
    i += 1

print("=" * 20)
print(f"As vogais encontradas sofram: {vogais}")
print(f"As consoantes encontradas sofram: {consoantes}")
print("=" * 20)
print(f"No texto tem {vogalA} vogal(s) A.")
print(f"No texto tem {vogalE} vogal(s) E.")
print(f"No texto tem {vogalI} vogal(s) I.")
print(f"No texto tem {vogalO} vogal(s) O.")
print(f"No texto tem {vogalU} vogal(s) U.")

# EXERCÍCIO 10
num2=0
num4=0
num7=0
num3=0
num1=0
num0=0
num6=0
i = 1

vetor=[2, 4, 7, 2, 3, 3, 1, 0, 2, 6]

for letras in vetor:

    if letras == 2:
        num2+=1
    elif letras == 4:
        num4+=1
    elif letras == 7:
        num7+=1
    elif letras == 3:
        num3+=1
    elif letras == 1:
        num1+=1
    elif letras == 0:
        num0+=1
    else:
        num6+=1
    i += 1

print("=" * 20)
print(f"No texto tem {num2} número(s) 2.")
print(f"No texto tem {num4} número(s) 4.")
print(f"No texto tem {num7} número(s) 7.")
print(f"No texto tem {num3} número(s) 3.")
print(f"No texto tem {num1} número(s) 1.")
print(f"No texto tem {num0} número(s) 0.")
print(f"No texto tem {num6} número(s) 6.")

# EXERCÍCIO 11
# ARRUMAR !!!!!!!!!!!!!!!!!!!!!!
indiceVetorA=0
indiceVetorB=0
indiceVetorC=0

for i in range(1,2):
    indiceVetorA=int(input("Favor defina o valor do vetor A: "))
    indiceVetorB=int(input("Favor defina o valor do vetor B: "))
    indiceVetorC=int(input("Favor defina o valor do vetor C: "))
    print("=" * 20)

    vetorA = [0]
    vetorB = [0]
    vetorC = [0]

    for i in range(indiceVetorA):
        num=input(f"Digite os {indiceVetorA} do vetor A: ")
        vetorA+=num
        i+=1
    print("="*20)

    for i in range(indiceVetorB):
        num=input(f"Digite os {indiceVetorB} do vetor B: ")
        vetorB+=num
        i+=1
    print("=" * 20)

    vetorC = vetorA + vetorB

    print("=" * 20)

print(f"Valores do vetor A: {vetorA}")
print(f"Valores do vetor B: {vetorB}")
print(f"Valores do vetor C: {vetorC}")
