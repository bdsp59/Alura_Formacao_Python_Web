#Ao construirmos o arquivo modelo_.py, verificamos que podemos ter muitos ifs para imprimir as 
#informações de filmes e séries. Então vamos construir outro tipo de estrutura para resolver esse
#problema.

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    def dar_like(self):
        self._likes += 1

    #Aqui vamos criar um método específico para imprimir os atributos que a classe Programa possui.
    #Podemos imprimir usando um método imprime com o print, mas temos um método específico do python 
    #que pode ser utilizado para isso, o __str__. Esse método retorna uma string.
    # def imprime(self):
    #    print(f'{self._nome} - {self.ano} - {self._likes} Likes')
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    #Como vamos ter atributos específicos dessa classe, não podemos apenas utilizar o método da classe mãe.
    #Então temos que criar um método específico de imprime dessa classe.
    #def imprime(self):
    #    print(f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes')
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    #def imprime(self):
    #    print(f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes')
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('demolidor', 2017, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]

for programa in filmes_e_series:
    #Graças ao polimorfismo podemos chamar o método imprime e apesar de utilizarmos a classe programa
    #para gerar o for, o python sabe que tem que chamar o imprime de cada classe filho.
    #programa.imprime()

    #Como utilizamos o método exclusivo __str__ nas nossas classes, o python já sabe que esse parte
    #é responsável por imprimir algo, então se chamarmos a classe com a função print() será impresso
    #o que está no método __str__.
    print(programa)

#Outro tipo de método exclusivo que temos é o __repr__ que é utilizado para trazer uma representação
#textual que ajude no debug ou no log. Ou seja, uma representação para programadores e não usuários finais.

