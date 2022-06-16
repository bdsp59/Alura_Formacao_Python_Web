
#Classe é um local onde se armazenam os dados relacionados entre si. É que serve como base para vários objetos.
#Objeto é referência a Classe. É quando iniciamos a classe para uso em uma parte do programa.
class Conta:

    #Atributos de classe são declaradas dentro da classe e servem para colocar as funções que a 
    #classe deve fazer e como elas devem funcionar.
    
    #O primeiro atributo de uma classe é o __init__ que serve para indicar a inicialização da classe
    #e como deve se dar esse início. É uma função construtora.

    #Esse self é a referência que sabe onde encontrar o próprio objeto. Os outros paramêtros são 
    #elementos que esperamos receber ao se iniciar o objeto que serão os valores associados aos atributos.
    #Na aula 4 aprendemos sobre encapsulamento, então vamos transformar os atributos da classe em privados.
    #Para um atributo se tornar privado em python apenas adicionamos '__' antes do nome dele.
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #Para acessar os atributos através da referência somente precisamos colocar o 
    # nome_referência.nome_atributo. Ex: conta.saldo acessa o atributo saldo da referência conta.

    #Agora vamos criar os métodos da nossa classe.
    def extrato(self):
        print("O saldo de {} é de {}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel
        

    def saca(self, valor):
        if(self.pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite.".format(valor))

    def transfere(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)

    #Na OO, cada classe deve ter uma única função e somente aquela função.
    #Então essa classe conta deve apenas ter atributos e métodos de acordo com a Conta e nada mais.
    
    #Como não devemos usar diretamente os atributos, mas ainda podemos ter necessidade de utilizar
    #os valores armazenados por eles, temos que criar métodos para conseguir pegar esses dados, os gets.
    def get_saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    def get_titular(self):
        return self.__titular

    #Também temos métodos para manipular esses atributos, os sets.
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    #Ver definição de @property e @atributo.setter na classe cliente

    #Tanto se tratando de set ou get, devemos nos atendar a apenas criar o que for necessário e 
    #fizer sentido na nossa regra de negócio.
