
#Classe é um local onde se armazenam os dados relacionados entre si. 
#Objeto é referência a Classe. É quando iniciamos a classe para uso em uma parte do programa.
class Conta:
    #Atributos de classe são declaradas dentro da classe e servem para colocar as funções que 
    #a classe deve fazer e como elas devem funcionar.
    
    #O primeiro atributo de uma classe é o __init__ que serve para indicar a inicialização da classe
    #e como deve se dar esse início. É uma função construtora.
    def __init__(self):
        print("Construindo objeto ...")
