import random

print("************************************")
print("Bem vindo ao jogo de Adivinhação!")
print("************************************")

numero_secreto = random.randint(1,100)
total_de_tentativas = 3
tentativa = 1

for tentativa in range(1, total_de_tentativas+1):
    print("Tentativa {} de {}".format(tentativa, total_de_tentativas))
    chute = int(input("Entre com um número entre 1 e 100: "))
    print("Você digitou", chute)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um valor entre 1 e 100!")
        continue 

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

print("Fim do jogo. O número era ", numero_secreto)