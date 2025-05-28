# EXERCICIO 01
nome=str(input("Digite seu nome: "))

def imprimir_nome():
    print(nome)

imprimir_nome()

# EXERCICIO 02
numeros=[]

for i in range(3):
    num=int(input("Digite um número: "))
    numeros+=[num]

def numero_maior():
    print(max(numeros))

print(numeros)
numero_maior()

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