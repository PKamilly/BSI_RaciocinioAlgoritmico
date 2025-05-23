# EXERCÍCIO 01
matriz=[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]

for i in range(5):
    print(matriz[i])
print("="*25)

if matriz[0][0]==0:
    matriz[0][0]=1
if matriz[1][1]==0:
    matriz[1][1]=1
if matriz[2][2]==0:
    matriz[2][2]=1
if matriz[3][3]==0:
    matriz[3][3]=1
if matriz[4][4]==0:
    matriz[4][4]=1
    
for i in range(5):
    print(matriz[i])

# EXERCÍCIO 02
matriz=[
    [0,1,2,4],
    [4,6,9,3],
    [3,0,4,2],
    [5,5,7,2]
]

for i in range(4):
    print(matriz[i])

print("="*25)

maximo0=max(matriz[0])
maximo1=max(matriz[1])
maximo2=max(matriz[2])
maximo3=max(matriz[3])
posicao0=0
posicao1=0
posicao2=0
posicao3=0

if matriz[0][0]==maximo0:
    posicao0=matriz[0][0]
    print(f"O valor maximo e´ {maximo0}")
    print(f"A posicao do valor maximo e´ {posicao0}")
if matriz[0][1]==maximo0:
    posicao0=matriz[0][1]
    print(f"O valor maximo e´ {maximo0}")
    print(f"A posicao do valor maximo e´ {posicao0}")
if matriz[0][2]==maximo0:
    posicao0=matriz[0][2]
    print(f"O valor maximo e´ {maximo0}")
    print(f"A posicao do valor maximo e´ {posicao0}")
if matriz[0][3]==maximo0:
    posicao0=matriz[0][3]
    print(f"O valor maximo e´ {maximo0}")
    print(f"A posicao do valor maximo e´ {posicao0}")


if matriz[1][0]==maximo1:
    posicao1=matriz[1][0]
    print(f"O valor maximo e´ {maximo1}")
    print(f"A posicao do valor maximo e´ {posicao1}")
if matriz[1][1]==maximo1:
    posicao1=matriz[1][1]
    print(f"O valor maximo e´ {maximo1}")
    print(f"A posicao do valor maximo e´ {posicao1}")
if matriz[1][2]==maximo1:
    posicao1=matriz[1][2]
    print(f"O valor maximo e´ {maximo1}")
    print(f"A posicao do valor maximo e´ {posicao1}")
if matriz[1][3]==maximo1:
    posicao1=matriz[1][3]
    print(f"O valor maximo e´ {maximo1}")
    print(f"A posicao do valor maximo e´ {posicao1}")


if matriz[2][0]==maximo2:
    posicao2=matriz[2][0]
    print(f"O valor maximo e´ {maximo2}")
    print(f"A posicao do valor maximo e´ {posicao2}")
if matriz[2][1]==maximo2:
    posicao2=matriz[2][1]
    print(f"O valor maximo e´ {maximo2}")
    print(f"A posicao do valor maximo e´ {posicao2}")
if matriz[2][2]==maximo2:
    posicao2=matriz[2][2]
    print(f"O valor maximo e´ {maximo2}")
    print(f"A posicao do valor maximo e´ {posicao2}")
if matriz[2][3]==maximo2:
    posicao2=matriz[2][3]
    print(f"O valor maximo e´ {maximo2}")
    print(f"A posicao do valor maximo e´ {posicao2}")


if matriz[3][0]==maximo3:
    posicao3=matriz[3][0]
    print(f"O valor maximo e´ {maximo3}")
    print(f"A posicao do valor maximo e´ {posicao3}")
if matriz[3][1]==maximo3:
    posicao3=matriz[3][1]
    print(f"O valor maximo e´ {maximo3}")
    print(f"A posicao do valor maximo e´ {posicao3}")
if matriz[3][2]==maximo3:
    posicao3=matriz[3][2]
    print(f"O valor maximo e´ {maximo3}")
    print(f"A posicao do valor maximo e´ {posicao3}")
if matriz[3][3]==maximo3:
    posicao3=matriz[3][3]
    print(f"O valor maximo e´ {maximo3}")
    print(f"A posicao do valor maximo e´ {posicao3}")

# EXERCICIO 03
matriz=[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]
for linha in matriz:
    numMatricula=int(input("Digite o numero de matricula: "))
    matriz[linha]=numMatricula

for i in range(5):
    print(matriz[i])