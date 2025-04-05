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
print("Você acorda deitado no chão de uma floresta escura.")
print("Não se sabe como chegou ali.")
print("Ao levantar uma gota de suor escorre em seu rosto pálido")
print("Os feixes do brilho da lua mostram um caminho de terra.")
print("você se levanta do chão e segue o caminho.")
print("Você encontra duas opcoes para seguir.")
print("As opcoes sao: o caminho da esquerda ou o caminho da direita")
caminho=str(input("Digite E para ESQUERDA | D para DIREITA: "))

if caminho=="E" or caminho=="e":
    print("=================")
    print("Você escolhe o caminho a ESQUERDA")
    print("Seguindo por este caminho você chega a um pqueno rio.")
    print("Do outro lado ha uma luz ao longe.")
    print("Você observa o reflexo da lua na agua e pensa: 'Parece fundo...'")
    print("S para SIM | N para NAO")
    caminhoE=str(input("Deseja seguir em frente? "))
    if caminhoE=="S" or "s":
        print("=================")
        print("Sua curiosidade grita alto. VOCÊ DECIDE SEGUIR")
        print("Você toca com seus pés na agua com timidez.")
        print("'Esta um gelo' - você pensa consigo.")
        print("Voltando seu olhar para o outro lado do rio você observa a luz no mesmo lugar.")
        print("Mesmo com receio você segue em frente.")
        print("Andando com cuidado naquela agua ")
        print("A agua sobe lentamente ate seus joelhos.")
        print("Apesar do medo você persiste e chega ao outro lado.")
        print("Olhando para o horizonte a luz foge.")
        print("O medo e desespero lhe dominam.")
        print("Derepente surge um pequeno ponto de luz")
        print("Era um vagalume")
