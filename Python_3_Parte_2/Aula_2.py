def jogar_forca():
    print("************************************")
    print("Bem vindo ao jogo da forca!")
    print("************************************")

    palavra_secreta = "banana"
    
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip #Essa função remove os espaços vazios que a palavra possa possuir.
        
        index = 0
        #Apesar de existir a função find(), que verifica se o que está no () pertence a String, ele
        #apenas retorna a primeira ocorrência do elemento. Como precisamos de todos, criamos esse for.
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("A letra {} está na posição {}".format(chute, index))
            index += 1

    print("Fim do jogo.")

if(__name__  == "__main__"):
    jogar_forca()


#Para verificar as funções que a classe String possui: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str