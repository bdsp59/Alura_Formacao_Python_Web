def jogar_forca():
    print("************************************")
    print("Bem vindo ao jogo da forca!")
    print("************************************")

    palavra_secreta = "banana".upper()#Aqui já deixamos as letras maiúsculas para garantir a verificação
    #Usando List Comprehensions
    letras_acertadas = ["_" for letra in palavra_secreta]#Com essa estrutura preenchemos a lista letras_acertadas com _ na hora da inicialização. 

    print("\n", letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip().upper()#Aqui já deixamos as letras maiúsculas para garantir a verificação
        
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1
            print("Opa, você errou. Ainda restam {} tentativas".format(6-tentativas))

        enforcou = tentativas == 6 #Nesse caso, atribuímos o valor booleano, que vem da igualdade entre tentativas e o 6, a variável enforcou.
        acertou = "_" not in letras_acertadas #Nesse caso, vamos verificar se ainda existem _ na variável letras_acertadas, pois quando não existir mais é que acertou a palavra.

        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")

    print("Fim do jogo.")

if(__name__  == "__main__"):
    jogar_forca()


#Para verificar as funções que a classe String possui: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
#inteiros = [1,3,4,5,7,8,9]
#pares = [x for x in inteiros if x % 2 == 0]
#Com o código acima, preenchemos a lista pares com os valores pares obtidos da lista inteiros.