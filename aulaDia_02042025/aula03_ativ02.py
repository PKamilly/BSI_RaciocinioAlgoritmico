# EXERCICIO 01
while True:
    print("======================")
    print("CALCULADORA")
    print("======================")
    print("1. SOMA (+)")
    print("2. SUBTRACAO (-)")
    print("3. DIVISAO (%)")
    print("4. MULTIPLICACAO (X)")
    print("======================")
    print("5. SAIR")
    print("======================")

    selecao=int(input("Selecione uma das opcoes acima: "))

    while True:
        if selecao==1:
            print("======================")
            print("CALCULADORA")
            print("======================")
            print("SOMA SELECIONADO")
            print("======================")
            A=int(input("Digite o primeiro valor: "))
            B=int(input("Digite o segundo valor: "))
            somaTotal=A+B
            print("======================")
            print("A soma total deu ",somaTotal)
            print("S para SIM e N para NAO")
            sair=str(input("Gostaria de realizar uma nova soma? "))
            if sair=="N"  or sair=="n":
                break
        else:
            break
        
    while True:
        if selecao==2:
            print("======================")
            print("CALCULADORA")
            print("======================")
            print("SUBTRACAO SELECIONADO")
            print("======================")
            A=int(input("Digite o primeiro valor: "))
            B=int(input("Digite o segundo valor: "))
            subTotal=A-B
            print("======================")
            print("A subtracao total deu ",subTotal)
            print("S para SIM e N para NAO")
            sair=str(input("Gostaria de realizar uma nova subtracao? "))
            if sair=="N"  or sair=="n":
                break
        else:
            break
    
    while True:
        if selecao==3:
            print("======================")
            print("CALCULADORA")
            print("======================")
            print("DIVISAO SELECIONADO")
            print("======================")
            A=int(input("Digite o primeiro valor: "))
            B=int(input("Digite o segundo valor: "))
            divTotal=A/B
            print("======================")
            print("A soma total deu ",divTotal)
            print("S para SIM e N para NAO")
            sair=str(input("Gostaria de realizar uma nova soma? "))
            if sair=="N"  or sair=="n":
                break
        else:
            break
    
    while True:
        if selecao==4:
            print("======================")
            print("CALCULADORA")
            print("======================")
            print("MULTIPLICACAO SELECIONADO")
            print("======================")
            A=int(input("Digite o primeiro valor: "))
            B=int(input("Digite o segundo valor: "))
            multTotal=A*B
            print("======================")
            print("A soma total deu ",multTotal)
            print("S para SIM e N para NAO")
            sair=str(input("Gostaria de realizar uma nova soma? "))
            if sair=="N"  or sair=="n":
                break
        else:
            break
    
    if selecao==5:
        break

# EXERCICIO 02
# Para uma melhor experiência, rode o programa :)
print("Você acorda deitado no chão de uma floresta escura, não se sabe como chegou ali.")
print("Tocando em seu rosto para tentar acordar deste sonho, está gelado.")
print("Meio zonzo e confuso você se senta, ao fazer isto você instantaneamente sente uma fadiga e dor no corpo extrema.")
print("Em meio ao som ambiental você ouve seu estômago implorando por alimento. Você está faminto.")
print("Por quanto tempo estava deitado ali? por horas? por dias? ou será por semanas?")
print("Analizando ao redor há somente árvores altas, arbustos pequenos e ornamentais e rochas ao chão")
print("Os feixes do brilho da lua iluminam levemente a floresta, mostrando um caminho de terra.")
print("Seu estômago ronca.")
print("Sem muitas opções, você se levanta do chão com dificuldades e segue o caminho sem um rumo e sem esperanças.")
print("----------------------")
print("5 minutos depois . . .")
print("----------------------")
print("Após um tempo caminhando você se depara com uma bifurcação.")
print("Os caminhos são idênticos")
print("Seu estômago ronca.")
print("Você precisa decidir por qual caminho seguir")
print("Digite E para ESQUERDA | D para DIREITA")
caminho=str(input("R: "))

if caminho=="E" or caminho=="e":
    print("=================")
    print("O caminho a ESQUERDA lhe chama a atenção, você decide segui-lo.")
    print("----------------------")
    print("3 minutos depois . . .")
    print("----------------------")
    print("Você chega a um pequeno rio.")
    print("Do outro lado há uma pequena luz ao longe.")
    print("'Aquela luz pode ser um acampamento!' - você pensa consigo coberto de esperança")
    print("Desviando o olhar você observa o reflexo da lua na leve correntesa que se forma e pensa consigo: 'Parece fundo...'")
    print("Seu estômago ronca.")
    print("Você deveria seguir em frente?")
    print("Digite S para SIM | N para NÃO")
    caminhoE=str(input("R: "))
    if caminhoE=="S" or "s":
        print("=================")
        print("Sua curiosidade grita alto. VOCÊ DECIDE SEGUIR")
        print("Focado(a) você toca seus pés na água com timidez.")
        print("'Esta um gelo' - você pensa consigo.")
        print("Voltando seu olhar para o outro lado do rio você observa a luz no mesmo lugar.")
        print("Mesmo com receio você segue em frente.")
        print("A cada passo adentro, seu corpo arrepia cada vez mais até alma")
        print("A água sobe lentamente até seus joelhos.")
        print("Apesar do medo você persiste contra a leve correntesa e chega ao outro lado.")
        print("Olhando para o horizonte a luz foge.")
        print("O medo e desespero lhe dominam.")
        print("Derepente surge um pequeno ponto de luz")
        print("Era apenas um vagalume")
