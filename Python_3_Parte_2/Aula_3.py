def jogar_forca():
    print("************************************")
    print("Bem vindo ao jogo da forca!")
    print("************************************")

    palavra_secreta = "banana"
    letras_acertadas = []#Criamos uma lista para armazenar as letras que o usuário chutar corretamente
    
    #Fiz diferente do curso, pois era muito simples
    for letra in palavra_secreta:#Criando uma forma de exibir a palavra a ser descorberta, quando não temos letras.
        letras_acertadas.append("_")

    print("\n", letras_acertadas)

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()
        
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index += 1
        
        print(letras_acertadas)

    print("Fim do jogo.")

if(__name__  == "__main__"):
    jogar_forca()


#Para verificar as funções que a classe String possui: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str