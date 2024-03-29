# Alura_Formacao_Python_Web
Repositório para armazenar os arquivos de estudos da 'Formação Python para Web' da Alura

## Python 3 parte 1
Primeiro curso da formação, voltado para ensinar o básico de python. 
Como instalar e primeiros comandos.
Como funciona e especificações da linguagem.
IDEs e editores para o python. Ex: Pycharm, VScode, SublimeText.
Diferenças entre Python 2 e Python 3.
Comandos de seleção (If..Elif..Else).
Comandos de repetição (While/For).
Comandos de controle de fluxo (continue/break).
Formatação de Strings.
Gerando números aleatórios.
Entradas do usuário alteram o código.
Controle de pontuação em um jogo.
Criando e chamando uma função.
Diferenciando um arquivo executado de um importado.
Diferença entre código interpretado e compilado.

## Python 3 parte 2
Explicando tipo booleano e continuando o jogo de forca.
Manipulação de Strings.
Criando e manipulando listas em python.
Tuplas em python.
Introdução a estruturas de dados Set e Dictionary.
Jogo de forca simples.
Explicando e criando List Comprehension.
Leitura e Escrita em arquivos.
Sintaxe With.
Separando código em funções.
Refatorando o código e deixando mais organizado e bonito.
Parâmetros opcionais e nomeados.

## Artigo - Trabalhando com precisão em números decimais
Se trabalharmos com o float no python para lidar com valores monetários, provavelmente teremos um erro grave. O fato de o computador trabalhar com binários, o que leva a ele não ser capaz de representar com precisão exata certas frações. Fazendo com que esses valores sejam arredondados para o mais próximo que se encaixe na representação binário, o que representa um pequeno erro de precisão.
Se pensarmos em questões monetárias, poderíamos ter a possibilidade de usar apenas inteiros e como 1 real = 100 centavos, poderiamos salvar como 100 e depois dividir por 100 para representar no formato de real. O que elimina o problema de precisão.
Mas apesar da solução acima parecer uma boa ideia, existe a questão de existirem países que não trabalham com a conversão de 100, mas com 1000 ou até outros tipos. Então essa solução não funcionaria para certas moedas, sendo assim não resolveria o problema.
Para resolver situações como essas, existe um tipo no Python que serve para lidar com valores quebrados, mas com exatidão. O 'Decimal', que é um tipo com precisão arbitrária. 

## Python 3 Entendendo a Orientação a Objetos
Aprendendo sobre Orientação a Objetos e como funciona em Python.
Dicionários.
Encapsulamento de código.
Diferença entre classe e objeto.
Funções construtoras.
Endereço e referência a objetos. 
Atributos de classe e como acessa-los.
Criando e utilização métodos.
Encapsulamento de atributos.
Coesão do código.
Getters e Setters.
Propriedades.
Métodos Estáticos.

## Python 3 Avançando na Orientação a Objetos
Relembrando sobre o que vimos em Python 3 Entendendo a Orientação a Objetos.
Herança.
Utilizando o método super().
Polimorfismo e suas utilizações.
Método __str__.
Herança built-in.
Vantagens e desvantagens de fazer herança.
Duck Typing.
Data Model.
Classes abstratas(ABCs).
Herança Múltipla.
Mixin.

## String em Python: Extraindo informações de uma URL
Estrutura e manipulação de URLs(Strings).
Utilização do Raise.
Expressões Regulares.
Quantificadores e Intervalos.
Utilizando RegEx (https://docs.python.org/pt-br/3/howto/regex.html#regex-howto).
Método __len__.
Método __eq__.
Método __str__.

## Python Collections: Parte 1
Listas e Tuplas.
Métodos de listas e Tuplas.
Problemas de listas mutáveis.
Quando utilizar lista e tuplas.
Misturando lista e tuplas em estruturas.
Utilizando __eq__.
Boas práticas de comparação entre objetos.
Utilizando o enumerated.
Desempacotar tuplas.
Ordenação (Utilizando sorted ou .sort).
Ordenação de objeto próprio.
Utilizando o __lt__.
Utilização do attrgetter.
Utilizando o total_ordering.

## Python Collections: Parte 2
Conjuntos.
Funções e operações de conjuntos.
Congelar conjuntos (frozenset).
Dicionários.
Funções e operações de conjuntos.
DefaultDict e Counter.
Contagem de letras em texto.

## Python Brasil: Validação de dados no padrão nacional
Validação de CPF.
Utilizand o PyPi (https://pypi.org/).
Importando a biblioteca de validação de CPFs.
Classe factory.
Como funciona e como utilizar a classe factory.
Utilizando Regex. (https://www.w3schools.com/python/python_regex.asp)
Utilizando DateTime e as suas funcionalidades. (https://docs.python.org/3/library/datetime.html)
Utilizando o DataModel. (https://docs.python.org/3/reference/datamodel.html)
Utilizando o timedelta.
Acessando APIs, utilizando o request. 
Testando API do ViaCep. (https://viacep.com.br/)
