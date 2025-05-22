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

# EXERCÍCIO 02 - ARRUMAR!!!!!!!!!!!!
matriz=[
    [0,1,2,4],
    [4,6,6,3],
    [3,0,4,2],
    [5,8,7,8]
]

for i in range(4):
    print(matriz[i])

print("="*25)

for i in range(4):
    print(matriz[i])

print("="*25)
print(f"O maior valor da matriz é {max(matriz[i])}")