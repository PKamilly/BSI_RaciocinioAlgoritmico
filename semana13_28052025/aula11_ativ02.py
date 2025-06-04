# EXERCÍCIO 01
def soma_elementos():
    num=1,2,3,4,5
    return sum(num)

lista=soma_elementos()
print(lista)

# EXERCÍCIO 02
texto=str(input("Digite um texto: "))

def e_palindromo(texto):
    inverso=list(reversed(texto))
    
    if texto == inverso:
        return True
    else:
        return False

e_palindromo(texto)

# EXERCICIO 03
lista=[1,2,3,4,5,6,7,8,9,10]

def maior_elemento(lista):
    return print(max(lista))

maior_elemento(lista)

# EXERCICIO 04
texto=str(input("Digite um texto: "))
caractere=str(input("Digite um carectere do texto: "))
quantidade=0

for letra in texto:
    if letra==caractere:
        quantidade+=1

print(f"Na palavra {texto} tem {quantidade} vezes a letra {caractere}")

# EXERCICIO 05
def menu():
    print("=" * 25)
    print("CALCULADORA")
    print("=" * 25)
    print("1. SOMA")
    print("2. SUBTRAÇÃO")
    print("3. MULTIPLICAÇÃO")
    print("4. DIVISÃO")
    print("5. SAIR")
def agradecimentos():
    print("Obrigada por usar a calculadora!")
operacao=0

while operacao != 6:
    menu()
    print("=" * 25)
    operacao = int(input("Escolha sua operação: "))
    print("=" * 25)

    if operacao != 5:
        num1 = int(input("Digite o primeiro valor: "))
        num2 = int(input("Digite o segundo valor: "))
        print("=" * 25)

    def soma():
        return print(f"Soma = {num1 + num2}")
    def sub():
        return print(f"Subtração = {num1 - num2}")
    def mult():
        return print(f"Multiplicação = {num1 * num2}")
    def div():
        return print(f"Divisão = {num1 / num2}")

    if operacao == 1:
        soma()
    if operacao == 2:
        sub()
    if operacao == 3:
        mult()
    if operacao == 4:
        div()
    if operacao == 5:
        agradecimentos()
        break