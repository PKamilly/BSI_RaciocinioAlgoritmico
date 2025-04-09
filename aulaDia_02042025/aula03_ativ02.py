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
nome=input("Digite seu nome: ")

print("======================")

print("Você acorda deitado no chão de uma floresta escura, não se sabe como chegou ali.")
print("Tocando em seu rosto para tentar acordar deste sonho, você o sente gelado.")
print("Meio zonzo e confuso você se senta, ao fazer isto você instantaneamente sente uma fadiga e dor no corpo extrema.")
print("Em meio ao som ambiental você ouve seu estômago implorando por alimento. Você está faminto.")
print("Por quanto tempo estava deitado ali? por horas? por dias? ou será por semanas?")
print("Analizando ao redor há somente árvores altas, arbustos pequenos e ornamentais e rochas ao chão.")
print("Os feixes do brilho da lua iluminam levemente a floresta, mostrando um caminho de terra.")
import time
tempo=10
time.sleep(tempo)

print("Seu estômago ronca.")
print("Sem muitas opções, você se levanta do chão com dificuldades e segue o caminho sem um rumo e sem esperanças.")
print("----------------------")
print("5 minutos depois . . .")
print("----------------------")
import time
tempo=4
time.sleep(tempo)
    
print("Após um tempo caminhando você se depara com uma bifurcação.")
print("Os caminhos são idênticos.")
print("Seu estômago ronca.")
print("Você precisa decidir por qual caminho seguir.")
print("Digite E para ESQUERDA | D para DIREITA")
caminho=str(input("R: "))

if caminho=="E" or caminho=="e":
    print("=================")
    print("O caminho a ESQUERDA lhe chama a atenção, você decide segui-lo.")
    print("----------------------")
    print("3 minutos depois . . .")
    print("----------------------")
    import time
    tempo=4
    time.sleep(tempo)
    
    print("Você chega a um pequeno rio.")
    print("Do outro lado há uma pequena luz ao longe.")
    print("'Aquela luz pode ser um acampamento!' - você pensa consigo coberto de esperança.")
    print("Desviando o olhar você observa o reflexo da Lua na leve correntesa que se forma e pensa consigo: 'Parece fundo...'")
    print("Seu estômago ronca.")
    print("Digite S para SIM | N para NÃO")
    rio=str(input("Você deveria seguir em frente? "))
    
    if rio=="S" or rio=="s":
        print("=================")
        print("Sua curiosidade grita alto. VOCÊ DECIDE SEGUIR.")
        print("Focado(a) você toca seus pés na água com timidez.")
        print("'Esta um gelo' - você pensa consigo.")
        print("Voltando seu olhar para o outro lado do rio você observa a luz no mesmo lugar.")
        print("Mesmo com receio você segue em frente.")
        print("A cada passo adentro, seu corpo arrepia cada vez mais até alma.")
        print("Você ouve algo baixo atrás de si mas ignora, você não se importa e segue adiante.")
        print("A água sobe lentamente até seus joelhos.")
        print("Apesar do medo você persiste contra a leve correntesa e chega ao outro lado.")
        print("Olhando para o horizonte a luz foge.")
        print("O medo e desespero lhe dominam.")
        print("De repente surge um pequeno ponto de luz.")
        print("Era apenas um vagalume.")
        
    elif rio=="N" or rio=="n":
        print("=================")
        print("Após analisar mais um pouco o rio, o medo lhe consome. VOCÊ DECIDE FICAR.")
        print("Alguns segundos depois você ouve um arbusto se mexer por perto.")
        print("Virando para trás você nota uma sombra em meio aos arbustos.")
        print("Digite S para SIM | N para NÃO")
        arbusto=str(input("Checar o arbusto? "))
        if arbusto=="s" or arbusto=="S":
            print("=================")
            print("Você é medroso porém curioso. VOCÊ DECIDE CHECAR.")
            print("Receoso você continua lentamente e sente que cada passo parece uma eternidade.")
            print("De repente você sente algo no pé e logo em seguida ouve um barulho, um galho se partiu.")
            print("Você paralisa e descobre a origem do barulho, seus pés.")
            print("Você acidentalmente pisou em um galho, estava tão amedrontado que nem notou o caminho a sua volta.")
            print("Silêncio.")
            print("Olhando ao redor não pareceu acontecer nada.")
            print("Nenhum peixe pulou da água")
            print("Nenhum grillo cantarolava")
            print("Nenhuma folha caiu de sua árvore.")
            print("Nenhuma coruja chirriou ao longe.")
            print("Somente o eterno silêncio.")
            print("Seu estômago ronca alto.")
            print("Neste momento você sente o enorme arrependimento engolindo seu corpo.")
            print("Em seguida um vulto preto petróleo com o dobro do seu tamanho surge por entre os arbustos.")
            print("Aqueles mesmos em que você estava prestes a checar a alguns segundos atrás.")
            print("O luar da Lua mostra sua verdadeira face peluda em tom cacau.")
            print("A fera lhe encara.")
            print("'Porra' - ",nome,", 2025.")
        else:
            print("Seu corpo paralisa. VOCÊ NÃO FAZ NADA.")
            print("Virando lentamente você ")
            
elif caminho=="D" or caminho=="d":
    print("=================")
    print("Sua intuição te manda seguir pela direita. VOCÊ SEGUE O CAMINHO A DIREITA.")
    print("Caminhando por alguns minutos você nota uma montanha ao longe")
    print("Digite S para SIM | N para NÃO")
    montanha=str(input("Seguir e subir a montanha? "))
    if montanha=="S" or montanha=="s":
        print("")
