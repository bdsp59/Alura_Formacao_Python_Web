#Agora vamos começar a utilizar uma classe playlist. Vamos separar o arquivo, pois ele tem 
# funcionalidades diferentes das que vimos até agora.

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

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'

#Vamos fazer a classe Playlist herdar a classe List e utilizar as suas propriedade exclusivas para 
#ajudar no que desejamos fazer com a nossa classe.
class Playlist(list):
    #Como toda a classe começamos com o inicializador, mas se apenas iniciarmos os nossos atributos
    #será como sobreescrever o inicializador da classe List e não é o que queremos, pois precisamos
    #das propriedades da classe List. Mas não é possível apenas trazer o inicializador do List, pois
    #precisamos do atributo nome.
    #Então a solução é fazer com que apenas o atributo programas seja iniciado como um tipo List.
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)

    #Como objetos do tipo List possuem a função len, não precisamos mais do método tamanho().

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

playlist_fim_de_semana = Playlist('Fim de Semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

#Como a classe Playlist não é interável, não podemos utilizar o for..in diretamente nessa classe,
#mas podemos utilizar dentro do atributo programas da classe que é um List.
for programa in playlist_fim_de_semana:
    print(programa)

#Como herdamos as características da classe List, agora podemos verificar se determinado elemento
#está no objeto que estamos utilizando.

print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana}')