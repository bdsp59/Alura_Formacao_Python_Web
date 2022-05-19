#Criado também na aula 8 do curso
import Aula_7
import Aula_8

def escolhe_jogo(): 
    print("************************************")
    print("Escolha o seu jogo!")
    print("************************************")

    print("1 - Forca\n2 - Adivinhação")
    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando forca")
        Aula_8.jogar_forca()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        Aula_7.jogar_adivinhacao()

if(__name__ == "__main__"):
    escolhe_jogo()