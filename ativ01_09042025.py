# exercicio 01
numero=int(input("Favor digite um numero: "))

multiplicador=0
numMultip=0

while multiplicador<=10 and numMultip<=10:
    total=numero*numMultip
    print(numero,"*",numMultip,"=",total)
    multiplicador=multiplicador+1
    numMultip=numMultip+1

#exercicio 02
nota=float(input("Digite a sua nota: "))

while nota<=7:
    print("\nNota invalida!")
    nota=float(input("Digite a sua nota: "))
    if nota>=7:
        print("\nNota valida!")

# exercicio 03
soma=0
contador=0

numero=float(input("Digite um numero: "))

while numero!= -1:
   soma += numero
   #"soma += numero" e igual a "soma=soma+numero"
   numero=float(input("Digite um numero: "))
   contador += 1
   
total=soma/contador
print("A media dos numeros e igual a",total)

# exercicio 04
soma=0
contador=1

n=int(input("Digite quantos numeros quer somar: "))

while contador<=n:
    soma+=contador
    contador+=1

print("A soma total de todos os numeros e igual a",soma)

# exercicio 05
contador=0
pares=0
impares=0

while contador<10:
    numero=int(input("Digite um numero: "))
    
    if numero%2==0:
        pares+=1
    
    else:
        impares+=1
    
    contador+=1
print(f"Pares= {pares}")
print(f"Impares= {impares}")
