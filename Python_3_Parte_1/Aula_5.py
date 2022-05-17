print("************************************")
print("Bem vindo ao jogo de Adivinhação!")
print("************************************")

numero_secreto = 42
total_de_tentativas = 3
tentativa = 1

for tentativa in range(1, total_de_tentativas+1):
    print("Tentativa {} de {}".format(tentativa, total_de_tentativas))
    chute = int(input("Entre com um número entre 1 e 100: "))
    print("Você digitou", chute)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um valor entre 1 e 100!")
        continue #Continua na próxima interação

    acertou = numero_secreto == chute
    menor = numero_secreto > chute
    maior = numero_secreto < chute

    if(acertou):
        print("Você acertou")
        break #Saí do laço
    elif(menor):
        print("Você errou! Você chutou para baixo.")
    elif(maior):
        print("Você errou! Você chutou para cima.")

print("Fim do jogo")

#Podemos usar o format para controlar as interpolations, podemos fazer vários tipos de escrita apenas alterando o modo como usar o format.
#Tradicional: "Tentativa {} de {}".format(tentativa, total_de_tentativas)
#Invertendo os valores: "Tentativa {1} de {0}".format(tentativa, total_de_tentativas)
#Indicando que é um float: "R$ {:f}".format(1.59)
#Indicando que é um float com duas casas: "R$ {:.2f}".format(1.59)
#Indicando que é um float que deve sempre imprimir o ponto numa posição específica: "R$ {:7.2f}".format(1234.5) => Nesse caso indicamos que deve-se sempre imprimir 7 caracteres e 2 sempre estão após o ponto
#Indicando que é um float que deve sempre imprimir o ponto numa posição específica e completar com 0: "R$ {:07.2f}".format(1234.5) => Nesse caso indicamos que deve-se sempre imprimir 7 caracteres, sendo que preenche o espaço vazio com 0, e 2 sempre estão após o ponto
#Indicando que é um inteiro: "R$ {:d}".format(4)