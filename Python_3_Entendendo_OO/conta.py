
#Classe é um local onde se armazenam os dados relacionados entre si. É que serve como base para vários objetos.
#Objeto é referência a Classe. É quando iniciamos a classe para uso em uma parte do programa.
class Conta:

    #Atributos de classe são declaradas dentro da classe e servem para colocar as funções que a 
    #classe deve fazer e como elas devem funcionar.
    
    #O primeiro atributo de uma classe é o __init__ que serve para indicar a inicialização da classe
    #e como deve se dar esse início. É uma função construtora.

    #Esse self é a referência que sabe onde encontrar o próprio objeto. Os outros paramêtros são 
    #elementos que esperamos receber ao se iniciar o objeto que serão os valores associados aos atributos.
    def __init__(self, conta, numero, titular, saldo, limite):
        print("Construindo objeto ...")
        self.conta = conta
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    #Para acessar os atributos através da referência somente precisamos colocar o 
    # nome_referência.nome_atributo. Ex: conta.saldo acessa o atributo saldo da referência conta.

    #Agora vamos criar os métodos da nossa classe.
    def extrato(self):
        print("O saldo de {} é de {}".format(self.titular, self.saldo))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor  
