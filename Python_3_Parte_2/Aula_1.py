#Apenas explicou o que era tipo bool no python e criou o while do jogo.
def jogar_forca():
    print("************************************")
    print("Bem vindo ao jogo da forca!")
    print("************************************")

    palavra_secreta = "banana"
    
    enforcou = False
    acertou = False

    #O not é uma palavra reservada do python e tem como objetivo negar algo, se for true virá false e vice-versa.
    while(not enforcou and not acertou):
        print("Jogando...")

    print("Fim do jogo.")

if(__name__  == "__main__"):
    jogar_forca()
