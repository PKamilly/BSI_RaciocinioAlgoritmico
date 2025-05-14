# Exercício 01
import random
numerosJogador1 = []
numerosJogador2 = []
somaJogador1 = 0
somaJogador2 = 0
i=1

for i in range(1,4):
    print("="*25)
    print(f"DADO NUMERO {i}")
    print("="*25)
    
    numerosJogador1 = random.randint(1,6)
    somaJogador1+=numerosJogador1
    print(f"Valor do dado do Jogador1= {numerosJogador1}")
    print("-"*10)
    
    numerosJogador2 = random.randint(1,6)
    somaJogador2+=numerosJogador2
    print(f"Valor do dado do Jogador2= {numerosJogador2}")

print("="*25)
print(f"Resultado da soma de todos os valores do dado do Jogador 1")
print(f"Resultado = {somaJogador1}")
print("-"*25)
print(f"Resultado da soma de todos os valores do dado do Jogador 2")
print(f"Resultado = {somaJogador2}")
print("="*25)

# Exercício 02
