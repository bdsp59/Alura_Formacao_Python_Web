import random

def jogar_adivinhacao():
    print("************************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("************************************")

    numero_secreto = random.randint(1,100)
    total_de_tentativas = 0
    total_de_pontos = 1000

    nivel = int(input("Qual o nível de dificuldade?\n1-Fácil\n2-Médio\n3-Difícil\nDefina o nível:"))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for tentativa in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(tentativa, total_de_tentativas))
        chute = int(input("Entre com um número entre 1 e 100: "))
        print("Você digitou", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um valor entre 1 e 100!")
            continue 

        acertou = numero_secreto == chute
        menor = numero_secreto > chute
        maior = numero_secreto < chute

        if(acertou):
            print("Você acertou")
            break 
        elif(menor):
            print("Você errou! Você chutou para baixo.")
            total_de_pontos = total_de_pontos - (numero_secreto - chute)
        elif(maior):
            print("Você errou! Você chutou para cima.")
            total_de_pontos = total_de_pontos - (chute - numero_secreto)

    print("Você fez {} pontos!".format(total_de_pontos))
    print("Fim do jogo. O número era", numero_secreto)

if(__name__  == "__main__"):
    jogar_adivinhacao()

#Se fizermos uma divisão normal, 3/2, obtemos um float como resultado, mesmo que seja uma divisão exata, 2/2 = 1.0
#Mas se fizermos um comando assim: 3//2, obtemos apenas a parte inteira da divisão.