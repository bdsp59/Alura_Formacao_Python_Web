#Agora vamos ver como ler e escrever dados de um arquivo. 
#Para começar temos que saber que existem 3 modificadores de acesso para o arquivo, que 
# são identificadas por letras. Se não declara o modificar, por padrão, abre como 'r':
#  - 'r' de read, abre o arquivo para leitura.
#  - 'w' de write, abre o arquivo para escrita. Caso o arquivo exista, sobrescreve o arquivo.
#  - 'a' de append, abre o arquivo para adicionar algo.
#Outra coisa é que temos a seguinte estrutura para chamar o arquivo:
#  - open("nome_arquivo.ext", "modificador de acesso")
#Com isso abrimos o arquivo para podermos altera-lo, mas para isso temos que declarar essa 
# chamada a uma variável.
#  - arquivo = open("nome_arquivo.ext", "modificador de acesso")
#Para escrever no arquivo usamos o comando, desde que aberto como write ou append:
#  - arquivo.write("Mensagem")
#Para ler no arquivo usamos o comando, desde que aberto como read:
#  - arquivo.read()
#Para ler somente uma linha do arquivo usamos o comando:
#  - arquivo.readline()
#Como boa prática, devemos informar ao sistema que o arquivo pode ser fechado, ou seja, 
# não vamos mais alterar o arquivo:
#  -arquivo.close()
#Existe um modificador de acesso 'b' que serve para indicar que o arquivo deve ser trabalhado
# como binário. Temos o 'wb', para escrita em binário, e o 'rb', para leitura em binário. Para ler
# imagens temos que usar o 'rb'.
#Existe uma sintaxe especial para abrir o arquivo no python, visto que se ocorrer um erro na execução
# do programa, não é possível garantir que o arquivo foi fechado, então precisamos de algo que 
# garanta que o arquivo é fechado mesmo com erro. Para isso existe o with:  
#  - with open("palavras.txt") as arquivo:
#       for linha in arquivo:
#           print(linha)
#Com o with não é necessário fechar o arquivo, pois o python fica responsável por isso.

import random

def jogar_forca():
    print("************************************")
    print("Bem vindo ao jogo da forca!")
    print("************************************")

    palavras = []

    arquivo = open("palavras.txt", "r")

    for palavra in arquivo:#Aqui pegamos linha por linha no arquivo e salvamos o valor.
        palavra = palavra.strip()#Usamos o strip para remover qualquer coisa que não seja a palavra em si.
        palavras.append(palavra)#Salvamos as palavras em uma lista para que possamos usar depois.

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