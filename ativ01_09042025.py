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
