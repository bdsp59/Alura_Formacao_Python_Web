print("************************************")
print("Bem vindo ao jogo de Adivinhação!")
print("************************************")

numero_secreto = 42
#Permite que o usuário entre com um valor e associando ele a uma variável.
#Precisamos usar o int(), pois o chute deve ser um int para poder ser comparado com o numero_secreto.
chute = int(input("Entre com um número: "))

print("Você digitou", chute)

#Criando uma condição para verificar se o usuário acertou
if(numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")