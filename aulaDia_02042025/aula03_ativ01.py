#exercicio 01
idade=int(input("Favor digite sua idade: "))

if idade >= 18:
    print("PARABENS!")
    print("Você pode tirar a sua carteira")
else:
    print("Você ainda nao pode tirar a sua carteira")

#exercicio 02
media = float(input("Digite sua media: "))

if media >= 7:
    print("PARABENS!")
    print("Você foi aprovado!")
else:
    print("Você ficou para o exame final")

#exercicio 03
pdl=int(input("Digite seu Pdl do League of Legends: "))

if pdl <= 999:
    print("Você esta no ELO Ferro.")
    faltapdl_1 = 1000 - pdl
    print("Faltam ",faltapdl_1," para avancar ao proximo ELO.")

elif pdl >= 1000 and pdl <= 1999:
    print("Você esta no ELO Bronze.")
    faltapdl_2 = 2000 - pdl
    print("Faltam ",faltapdl_2," para avancar ao proximo ELO.")

elif pdl >= 2000 and pdl <= 2999:
    print("Você esta no ELO Prata.")
    faltapdl_3 = 3000 - pdl
    print("Faltam ",faltapdl_3," para avancar ao proximo ELO.")

elif pdl >= 3000 and pdl <= 3999:
    print("Você esta no ELO Ouro.")
    faltapdl_4 = 4000 - pdl
    print("Faltam ",faltapdl_4," para avancar ao proximo ELO.")

elif pdl >= 4000 and pdl <= 4999:
    print("Você esta no ELO Platina.")
    faltapdl_5 = 5000 - pdl
    print("Faltam ",faltapdl_5," para avancar ao proximo ELO.")

elif pdl >= 5000 and pdl <= 5999:
    print("Você esta no ELO Diamante.")
    faltapdl_6 = 6000 - pdl
    print("Faltam ",faltapdl_6," para avancar ao proximo ELO.")

elif pdl >= 6000 and pdl <= 6999:
    print("Você esta no ELO Mestre.")
    faltapdl_7 = 7000 - pdl
    print("Faltam ",faltapdl_7," para avancar ao proximo ELO.")\

elif pdl >= 7000 and pdl <= 7999:
    print("Você esta no ELO Grao-Mestre.")
    faltapdl_8 = 8000 - pdl
    print("Faltam ",faltapdl_8," para avancar ao proximo ELO.")

else:
    print("Você esta no ELO Desafiante.")