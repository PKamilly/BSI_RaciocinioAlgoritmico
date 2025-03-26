# Lista de exercicios (6 exercicios no total)
print("Exercicio 01")
anoAtual=int(input("Digite o ano atual: "))
anoNasc=int(input("Digite o ano que você nasceu: "))

idade=anoAtual-anoNasc

print("Sua idade é ", idade)


print("=====================================")


print("Exercicio 02")
print("O valor de cada carro e de R$ 100,00")
quantiCarro=int(input("Quantos carros gostaria de alugar?"))

valorCarro=100
total=quantiCarro*valorCarro

print("O valor total do aluguel foi: ", total)


print("=====================================")


print("Exercicio 03")
celcius=float(input("Digite quantos graus (celsius) estao agora: "))

fahrenheit=((celcius*9)/5)+32

print("Os graus atuais transcritos em fahrenheit sao: ",fahrenheit)


print("=====================================")


print("Exercicio 04")
nota1=float(input("Digite a nota 01: "))
nota2=float(input("Digite a nota 02: "))
nota3=float(input("Digite a nota 03: "))
nota4=float(input("Digite a nota 04: "))

media=(nota1+nota2+nota3+nota4)/4

print("A media das suas notas e igual a: ",media)


print("=====================================")


print("Exercicio 05")
idade=int(input("Digite sua idade: "))

idadeMeses=idade*12

print("Sua idade em meses e igual a: ",idadeMeses)


print("=====================================")


print("Exercicio 06")
preco=float(input("Digite o preco do produto: "))
kilo=float(input("Digite quantos kilos você gostaria de comprar: "))

total=preco*kilo

print("O preco final e igual a: ",total)
