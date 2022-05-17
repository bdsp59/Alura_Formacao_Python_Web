print("************************************")
print("Bem vindo ao jogo de Adivinhação!")
print("************************************")

numero_secreto = 42

chute = int(input("Entre com um número: "))

print("Você digitou", chute)

acertou = numero_secreto == chute
menor = numero_secreto > chute
maior = numero_secreto < chute

if(acertou):
    print("Você acertou")
elif(menor):
    print("Você errou! Você chutou para baixo.")
elif(maior):
    print("Você errou! Você chutou para cima.")

print("Fim do jogo")