#Ao construirmos o arquivo modelo.py, verificamos que copiamos muitas vezes o mesmo código para 
#mais de uma classe. Então vamos começar a usar o conceito de herança para diminuir a quantidade
#de código escrito e melhorar o visual do nosso código.

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

#Como ao termos uma classe filha em python não podemos acessar os atributos privados da classe mãe,
#quem programa com python teve que criar outra maneira para trabalhar com esse tipo de dado. Pois se
#apenas o mantivesse como privado, para fazer a chamada dele na classe filho teria que se utilizar
#_Programa__nome.
#A convenção adotada é utilizar apenas um _ para indicar que o atributo ou método é privado, mas que
#ainda pode ser utilizado pelas classes filho. Funciona como o protected no Java.
class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)#A função super serve para chamar a classe mãe. Ou seja, já vamos passar
        #o nome e o ano para o init da classe mãe, precisando apenas especificar os atributos únicos da classe
        #filho, no caso duracao para filme e temporada para serie.
        self.duracao = duracao

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao}'
        +f' - Likes: {vingadores.likes}')


atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas}'
        +f' - Likes: {atlanta.likes}')

#Aqui declaramos uma lista com filmes e séries, o que o python permite apesar de serem de tipos diferentes,
#mas ambos os elementos são programas, visto que programas é a classe mãe. Isso é polimorfismo.
#Polimorfismo é quando não importa a classe sendo utilizada, contanto que essa classe herde de uma 
#superclasse específica.
filmes_e_series = [vingadores, atlanta]

#Como ambos são da classe programa, vamos passar por todos os elementos dessa lista com um for..in
#e imprimir o que queremos. Mas a classe programa não possui duração ou temporadas, visto que são 
#exclusivos das classes filho. Então temos que dar um jeito de chamar esses atributos específicos
#de cada classe e exibi-los corretamente.
for programa in filmes_e_series:
    #Existe um método no python chamado 'hasattr' que serve para verificar se a classe possui determinado
    #atributo. Vamos usar esse método para determinar o que deve ser armazenado em detalhes.
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    print(f'{programa.nome} - {detalhes} - {programa.likes}')