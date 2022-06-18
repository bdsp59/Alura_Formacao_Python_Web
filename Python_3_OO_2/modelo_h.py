#Ao construirmos o arquivo modelo.py, verificamos que copiamos muitas vezes o mesmo código para 
#mais de uma classe. Então vamos começar a usar o conceito de herança para diminuir a quantidade
#de código escrito e melhorar o visual do nosso código.

class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def dar_like(self):
        self.__likes += 1

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao