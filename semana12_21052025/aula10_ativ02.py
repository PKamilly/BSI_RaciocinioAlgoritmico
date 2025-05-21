# EXERCÍCIO 01
matriz = [[0]*5] * 5

for i in range (5):
    print(matriz[i])

for linha in matriz:
    for coluna in matriz:
        if linha==0 & coluna==0:
            matriz[linha]+=1
        elif linha==1 & coluna==1:
            matriz[linha]+=1
        elif linha==2 & coluna==2:
            matriz[linha]+=1
        elif linha==3 & coluna==3:
            matriz[linha]+=1
        elif linha==4 & coluna==4:
            matriz[linha]+=1

print(matriz)
    
