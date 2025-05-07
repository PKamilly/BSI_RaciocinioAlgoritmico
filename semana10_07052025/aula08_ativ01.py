# EXERCICIO 01
contador=0

for i in range(0,10):
    if contador % 2 != 0:
        print(f"{contador} é ímpar.")
    else:
        print(f"{contador} é par.")
    
    contador = contador + 1

# EXERCICIO 02
# PARTE A
letras = ["P","r", "o", "f", "e"]
indice = 0

for i in range(0,5):
    print(letras[indice])
    indice = indice + 1

# PARTE B
letras = ["P","r", "o", "f", "e"]
indice = 0

for letra in letras:
    print(letras[indice])
    letra+=1
