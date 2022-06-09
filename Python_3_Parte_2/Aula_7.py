import random

def jogar_forca():

    saudacao()
    palavra_secreta = gerando_palavra_secreta()
    letras_acertadas = preenchendo_palavra_secreta(palavra_secreta)

    print("\n", letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while(not enforcou and not acertou):
        chute = chute_usuario()
        
        if chute in palavra_secreta:
            chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            tentativas += 1
            desenha_forca(tentativas)

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo.")

def saudacao():
    print("************************************")
    print("Bem vindo ao jogo da forca!")
    print("************************************")

def gerando_palavra_secreta():
    palavras = []

    arquivo = open("palavras.txt", "r")

    for palavra in arquivo:
        palavra = palavra.strip()
        palavras.append(palavra)

    arquivo.close()

    return palavras[random.randrange(0,len(palavras))].upper()

#Essa função é apenas ilustrativa, pois ela aumenta a complexidade do código ao invés de reduzir
def preenchendo_palavra_secreta(palavra):
    return ["_" for letra in palavra]

def chute_usuario():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def chute_correto(palavra, chut, l_certas):
    index = 0
    for letra in palavra:
        if(chut == letra):
            l_certas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

#Para poder deixar essas funções abaixo do main temos que colocar o if abaixo de tudo
if(__name__  == "__main__"):
    jogar_forca()
