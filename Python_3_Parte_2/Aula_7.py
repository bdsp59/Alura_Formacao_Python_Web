import random

def jogar_forca():

    saudacao()

    palavras = []

    arquivo = open("palavras.txt", "r")

    for palavra in arquivo:
        palavra = palavra.strip()
        palavras.append(palavra)

    arquivo.close()

    palavra_secreta = palavras[random.randrange(0,len(palavras))].upper()
    
    letras_acertadas = ["_" for letra in palavra_secreta]

    print("\n", letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1
            print("Opa, você errou. Ainda restam {} tentativas".format(6-tentativas))

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")

    print("Fim do jogo.")

if(__name__  == "__main__"):
    jogar_forca()

def saudacao():
    print("************************************")
    print("Bem vindo ao jogo da forca!")
    print("************************************")