# EXERCICIO 01
nome=str(input("Digite seu nome: "))

def imprimir_nome():
    print(nome)

imprimir_nome()


# Para vários nomes ou textos:
def imprimir_nome(nome): # <- (nome) é o nome da variável
    print(nome)

imprimir_nome("Marina")
imprimir_nome("Lucas")
imprimir_nome("Yuki")
imprimir_nome("Kaori")


# EXERCICIO 02
# "Receba" = (parametro de entrada)
def maior(valor1, valor2, valor3):
    return max(valor1, valor2, valor3)

# EXERCICIO 03
def criar_vetor():
    return [0]*5

vetor=criar_vetor()
print(vetor)

# def criar_vetor():
#    return [0]*5
#
# É igual a:
#
# vetor = [0]*5

# EXERCÍCIO 04
def media(lista):
    return sum(lista)/len(lista)

print(media([2,4,3,6,5,1]))

# EXERCICIO 05
def inverter(texto):
    invertido=(texto)[::-1]
    print(invertido)

texto=input("Digite um texto: ")
inverter(texto)

# EXERCÍCIO 06
matriz=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]

def imprimir_diagonal(matriz):
    for linha in range(len(matriz[0])): # Funciona em matrizes quadradas ou raiz quadrada
        for coluna in range(len(matriz[0])):
            if linha==coluna:
                print(matriz[linha][coluna])

imprimir_diagonal(matriz)

# OUTRO JEITO DE FAZER
def imprimir_diagonal(matriz):
    for i in range(len(matriz[0]))
        print(matriz[i][i])

imprimir_diagonal(matriz)