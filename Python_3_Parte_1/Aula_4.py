print("************************************")
print("Bem vindo ao jogo de Adivinhação!")
print("************************************")

numero_secreto = 42
total_de_tentativas = 3
tentativa = 1

while(tentativa <= total_de_tentativas):
    #print("Tentativa", tentativa, "de", total_de_tentativas)
    #Vamos escrever o texto usando o String interpolation, que é uma maneira de inserir os valores em uma string.
    print("Tentativa {} de {}".format(tentativa, total_de_tentativas))
    chute = int(input("Entre com um número: "))
    print("Você digitou", chute)

    acertou = numero_secreto == chute
    menor = numero_secreto > chute
    maior = numero_secreto < chute

    if(acertou):
        print("Você acertou")
        break
    elif(menor):
        print("Você errou! Você chutou para baixo.")
    elif(maior):
        print("Você errou! Você chutou para cima.")

    tentativa += 1

print("Fim do jogo")