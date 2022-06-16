
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property#Indica que é um propriedade, o que indica que não se tem necessidade de chamar o método 
    #com parenteses.
    def nome(self):
        print("chamando property do método nome")
        return self.__nome.title()

    @nome.setter#Indica que esse método abaixo deve se comportar como um setter. Na hora que o chamamos
    #no terminal podemos atribuir o valor como cliente.nome = "Luiz"
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome
