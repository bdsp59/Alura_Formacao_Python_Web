#O código que utilizamos em modelo_playlist.py, acabou tendo uma complexidade muito grande, pois 
#fizemos a classe playlist herdar a classe list, o que resolveu o nosso problema de usar as funções
#do list. Mas agora a classe playlist tem muitas funções, restrições e elementos que nem mesmo sabemos
#quais e não podemos mexer em tudo sem saber se vamos gerar erros, o que aumenta a complexidade 
# do nosso código. Então o ideal seria poder usar essas funções diretamente e não fazer a herança.
#Então nos utilizamos de outro conceito para conseguir montar a playlist da maneira que queremos, 
#a herança é uma extensão, ou seja, a classe playlist é um List, mas outra opção que temos é
#a composição, que é o que fizemos no código abaixo, nesse caso a playlist tem um List.
#Essa ideia de não fazer a herança, mas apenas pegar os métodos que queremos de alguma classe e usar as 
#suas funcionalidades é chamada de Duck Typing.

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

class Playlist():

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    #Como configuramos esse __getitem__ podemos ter algumas configurações iguais a do list já 
    # configuradas. Pois torna essa classe interável
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    #Tal qual adicionamos o método __getitem__ para tornar a nossa classe interável, aqui temos o método __len__ que 
    #vai servir para tornar a nossa classe sized, ou seja, vai permitir que usemos a função len() diretamente na classe.
    def __len__(self):
        return len(self._programas)

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

print(f'Tamanho da playlist: {len(playlist_fim_de_semana.listagem)}')

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana}')

#Python Data Model -> https://docs.python.org/3.9/reference/datamodel.html