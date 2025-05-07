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
while cont != 10: 
    num=float(input("Digite um número real: "))
    cont+=1
    a+=[num]

print(a)