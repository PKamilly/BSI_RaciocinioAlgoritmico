# LISTA VETORES

# EXERCÍCIO 01
a=[1,0,5,-2,-5,7]
soma=a[0]+a[1]+a[2]

print(f"soma = {soma}")

a[4]=100

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

# EXERCÍCIO 02
cont=0
a=[]
while cont != 6: 
    num=int(input("Por favor digite um números: "))
    cont+=1
    a+=[num]

print(a)

# EXERCÍCIO 03
cont=0
a=[]
a_quadrado=[]

while cont != 10: 
    num=float(input("Digite um número real: "))
    cont+=1
    a+=[num]

print(a)
print("===========")
a_quadrado=[a[0]**2,a[1]**2,a[2]**2,a[3]**2,a[4]**2,a[5]**2,a[6]**2,a[7]**2,a[8]**2,a[9]**2]
print(a_quadrado)

# EXERCÍCIO 04
cont=0
a=[]

while cont != 8: 
    num=int(input("Digite um número: "))
    cont+=1
    a+=[num]

print(a)
print("Temos 8 elementos, escolha um deles contando de 0 a 7")
x=int(input("Digite a primeira posição: "))
y=int(input("Digite a segunda posição: "))

if 0 <= x < 8 and 0 <= y < 8:
    soma=a[x]+a[y]
    print(f"a soma destas posições é {soma}")
else:
    print("Posição inválida! Digite uma posição entre 0 e 8.")

# EXERCÍCIO 05
cont=0
a=[]
par=0
impar=0

while cont != 10: 
    num=int(input("Digite um número: "))
    cont+=1
    a+=[num]
    if num%2==0:
        par+=1
    else:
        impar+=1

print(a)
print(f"Dos 10 valores, {par} são pares")
print(f"Dos 10 valores, {impar} são impares")

# EXERCÍCIO 06
cont=0
a=[]

while cont != 10: 
    num=int(input("Digite um número: "))
    cont+=1
    a+=[num]

maior=a[0]
menor=a[0]
cont=1
while cont != 10:
    if a[cont] > maior:
        maior = a[cont]
    elif a[cont] < menor:
        menor = a[cont]
    cont += 1

print(a)
print(f"O maior número é {maior}")
print(f"O menor número é {menor}")

# EXERCÍCIO 07
cont=0
a=[]

while cont != 10: 
    num=int(input("Digite um número: "))
    cont+=1
    a+=[num]

cont=1
maior=a[0]
menor=a[0]
posicaoMaior=0
posicaoMenor=0
while cont != 10:
    if a[cont] > maior:
        maior = a[cont]
        posicaoMaior=cont
    elif a[cont] < menor:
        menor = a[cont]
        posicaoMenor=cont
    cont += 1

print(a)
print(f"O maior número é {maior}, sua posição é {posicaoMaior}")
print(f"O menor número é {menor}, sua posição é {posicaoMenor}")

# EXERCÍCIO 08
cont=0
a=[]
media=0

while cont != 15: 
    nota=int(input("Digite a sua nota: "))
    cont+=1
    a+=[nota]

print(a)

cont=0
while cont != 15: 
    media+=a[cont]
    cont+=1

print(media)

# EXERCÍCIO 09
