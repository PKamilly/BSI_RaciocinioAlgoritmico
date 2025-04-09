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
nome = input("Digite seu nome: ")

print("\n======================")

print("Você acorda deitado no chão de uma floresta escura, não se sabe como chegou ali.")
print("Tocando em seu rosto para tentar acordar deste sonho, você o sente gelado.")
print(
    "Meio zonzo e confuso você se senta, ao fazer isto você instantaneamente sente uma fadiga e dor no corpo extrema.")
print("Em meio ao som ambiental você ouve seu estômago implorando por alimento. Você está faminto.")
print("Por quanto tempo estava deitado ali? por horas? por dias? ou será por semanas?")
print("Analizando ao redor há somente árvores altas, arbustos pequenos e ornamentais e rochas ao chão.")
print("Os feixes do brilho da lua iluminam levemente a floresta, mostrando um caminho de terra.")
import time
tempo = 15
time.sleep(tempo)

print("\nSeu estômago ronca.")
print("Sem muitas opções, você se levanta do chão com dificuldades e segue o caminho sem um rumo e sem esperanças.")
print("----------------------")
print("5 minutos depois . . .")
print("----------------------")
import time
tempo = 4
time.sleep(tempo)

print("\nApós um tempo caminhando você se depara com uma bifurcação.")
print("Os caminhos são idênticos. Porém nota-se uma montanha no caminho a direita.")
print("Seu estômago ronca.")
print("Você precisa decidir por qual caminho seguir.")
print("Digite E para ESQUERDA | D para DIREITA")
caminho = str(input("R: "))

if caminho == "E" or caminho == "e":
    print("\n=================")
    print("O caminho a ESQUERDA lhe chama a atenção, você decide segui-lo.")
    print("----------------------")
    print("3 minutos depois . . .")
    print("----------------------")
    import time
    tempo = 4
    time.sleep(tempo)

    print("\nVocê chega a um pequeno rio.")
    print("Do outro lado há uma pequena luz ao longe.")
    print("'Aquela luz pode ser um acampamento!' - você pensa consigo coberto de esperança.")
    print("Desviando o olhar você observa o reflexo da Lua na correntesa constante que se forma e pensa consigo: 'Parece fundo...'")
    print("Seu estômago ronca.")
    print("Digite S para SIM | N para NÃO")
    rio = str(input("Você deveria seguir em frente? "))

    if rio == "S" or rio == "s":
        print("\n=================")
        print("Sua curiosidade grita alto. VOCÊ DECIDE SEGUIR.")
        print("Focado(a) você toca seus pés na água com timidez.")
        print("'Esta um gelo' - você pensa consigo.")
        print("Voltando seu olhar para o outro lado do rio você observa a luz no mesmo lugar.")
        print("Mesmo com receio você segue em frente.")
        print("A cada passo adentro, seu corpo arrepia cada vez mais até alma.")
        print("Você ouve algo baixo atrás de si mas ignora, você não se importa e segue adiante.")
        print("A água sobe lentamente até sua cintura, provando a sua teoria.")
        print("Apesar do medo você persiste cuidadosamente contra a correntesa")
        print("Seu pé se prende em algo abaixo da água, mas você consegue se soltar e chega ao outro lado.")
        print("Olhando para o horizonte a luz foge.")
        print("O medo e desespero lhe dominam.\n")
        import time
        tempo=10
        time.sleep(tempo)

        print("De repente surge um pequeno ponto de luz.\n")
        import time
        tempo=3
        time.sleep(tempo)

        print("Era apenas um vagalume.")

    elif rio == "N" or rio == "n":
        print("\n=================")
        print("Após analisar mais um pouco o rio, o medo lhe consome. VOCÊ DECIDE FICAR.")
        print("Alguns segundos depois você ouve um arbusto se mexer por perto.")
        print("Virando para trás você nota um pequeno vulto em meio aos arbustos.")
        print("Digite S para SIM | N para NÃO")
        arbusto = str(input("Checar o arbusto? "))
        if arbusto == "s" or arbusto == "S":
            print("\n=================")
            print("Você é medroso porém curioso. VOCÊ DECIDE CHECAR.")
            print("Receoso você continua lentamente e sente que cada passo parece uma eternidade.")
            print("De repente você sente algo no pé e logo em seguida ouve um barulho, um galho se partiu.")
            print("Você paralisa e descobre a origem do barulho, seus pés.")
            print("Você acidentalmente pisou em um galho, estava tão amedrontado que nem notou o caminho a sua volta.")
            import time
            tempo=13
            time.sleep(tempo)

            print("\nSilêncio.")
            import time
            tempo=3
            time.sleep(tempo)

            print("\nOlhando ao redor não pareceu acontecer nada.")
            import time
            tempo=3
            time.sleep(tempo)

            print("Nenhum peixe pulou da água")
            import time
            tempo=3
            time.sleep(tempo)

            print("Nenhum grillo cantarolava")
            import time
            tempo=3
            time.sleep(tempo)

            print("Nenhuma folha caiu de sua árvore.")
            import time
            tempo=3
            time.sleep(tempo)

            print("Nenhuma coruja chirriou ao longe.")
            import time
            tempo=3
            time.sleep(tempo)

            print("Somente o eterno silêncio.")
            import time
            tempo=5
            time.sleep(tempo)

            print("\nSeu estômago ronca alto.")
            import time
            tempo=5
            time.sleep(tempo)

            print("\nNeste momento você sente o enorme arrependimento engolindo seu corpo.")
            import time
            tempo=4
            time.sleep(tempo)

            print("\nEm seguida aquele vulto preto petróleo um pouco maior que seu tamanho surge por entre os arbustos.")
            print("Aqueles mesmos em que você estava prestes a checar a alguns segundos atrás.")
            import time
            tempo=6
            time.sleep(tempo)

            print("O vulto se espreita e para.")
            print("O luar da Lua mostra sua verdadeira face peluda em tom cacau.")
            import time
            tempo = 5
            time.sleep(tempo)

            print("A fera lhe encara.")
            import time
            tempo = 3
            time.sleep(tempo)

            print("\n'Porra' -",nome,", 2025.")
        else:
            print("\nSeu corpo paralisa. VOCÊ NÃO FAZ NADA.")
            print("De repente o vulto diminui, se espreita e para.")
            print("O luar da Lua mostra sua verdadeira face peluda em tom cacau.")
            print("A fera lhe encara.")
            import time
            tempo=8
            time.sleep(tempo)

            print("\nSuando frio e com o rosto mais pálido que antes, VOCÊ DECIDE ATRAVESSAR O RIO.")
            print("Você corre até o rio e entra.")
            print("A água está um gelo mas não importa agora.")
            print("A água sobe até sua cintura provando a sua teoria.")
            import time
            tempo=8
            time.sleep(tempo)

            print("\nEm um passo em falso você prende seu pé em algo, por conta da fadiga, dor e fome você cansa mais rápido.")
            print("'MERDA!' - você grita e ouve um grunido vindo de trás e se vira.")
            print("A fera peluda não está mais entre os arbustos, ela caminha para perto do rio lhe encarando.")
            print("Você grita que não é o lanchinho dele e a fera se levanta, ficando em duas patas.")
            print("O desespero lhe consome.")
            print("Você sente seus olhos arderem e começarem a molhar.")

elif caminho == "D" or caminho == "d":
    print("\n=================")
    print("'La de cima posso ter uma ampla visão da área' - você fala sozinho. VOCÊ SEGUE O CAMINHO A DIREITA.")
    print("Caminhando por alguns minutos você chega ao pé da montanha.")
    print("Ela é bem íngreme e rochosa.")
    print("Parece perigoso . . .")
    print("Seu estômago ronca.")
    print("Digite S para SIM | N para NÃO")
    caminhoD = str(input("Seguir e subir a montanha? "))
    if caminhoD == "S" or caminhoD == "s":
        print("\nApesar do extremo cansaso. VOCÊ DECIDE SUBIR.")
        print("----------------------")
        print("5 minutos depois . . .")
        print("----------------------")
        import time
        tempo = 3
        time.sleep(tempo)

        print("\nSubindo com muito cuidado você olha em volta e nota um rio.")
        print("'Será que eu chegaria naquele rio indo pelo outro caminho?' - você pensa consigo distraído com o rio.")
        import time
        tempo = 5
        time.sleep(tempo)

        print("Voltando para a subida você segura em uma rocha instável.")
        print("Você tenta se segurar mas é em vão.")
        import time
        tempo = 4
        time.sleep(tempo)

        print("\n'Porra' -",nome,", 2025.")

    elif caminhoD=="N" or caminhoD=="n":
        print("Você acha muito perigoso arriscas. VOCÊ SEGUE O CAMINHO.")
