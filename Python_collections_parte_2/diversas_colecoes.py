from collections import Counter


texto_1 = """
O que acontece é que estamos usando o operador is sem entender de fato como ele funciona! O is compara a identidade do objeto, isto é, o valor de referência de seu endereço na memória, não o valor definido por nós.

Mas espera… já vimos algo assim, não é? O operador == também funciona, a princípio, desta forma, mas seu comportamento pode ser alterado através dos métodos de comparação rica, por exemplo.

Então como podemos alterar o comportamento do is? Bem… na verdade, não podemos. O propósito do is é justamente esse, uma comparação que sempre se baseará na identidade de um objeto, ou seja, se um objeto de fato é (is) o objeto que está sendo comparado.

Quando quisermos comparar um valor (ou qualquer coisa que definirmos) de um objeto, usamos, então, o operador == e os métodos de comparação rica. Quando quisermos comparar a identidade de um objeto, usamos o is.

Mas, se é assim, por que nossa primeira comparação com is (usuario is 'Yan') retornou True?

String interning no Python

Por padrão, no Python (na implementação padrão CPython), cada vez que atribuímos um objeto a uma variável, estamos criando um objeto. Ou seja:

Mas vimos que esse resultado esperado não foi obtido com a string ’Yan’. Por quê? Isso é o que chamamos, na computação, de _string interning_.

String interning é uma técnica que força o armazenamento de apenas uma cópia de cada valor de string diferente na memória do computador.

Essa técnica é de muita utilidade para poupar espaço na memória, mas, ao mesmo tempo, pode prolongar o tempo de processamento de algumas operações, já que ao criar uma string,o computador tem de procurar por todas as strings já existentes se uma já tem o valor dessa nova.

O Python suporta essa técnica de string interning através da função intern() (que é built-in no Python 2 e no Python 3 se localiza no módulo sys), mas não a utiliza por padrão nas operações de strings. Entretanto, há algumas exceções em que essa técnica é usada nativamente pela linguagem.

Um exemplo é com strings de apenas um caractere, que sempre passam por esse processo:
"""

texto_2 = """
Se você é usuário Linux, quais tipos de extensão, para arquivos compactados, você costuma lidar? Será que é zip? Provavelmente não. Geralmente, encontramos arquivos com a extensão .tar.gz.

Mas por que .tar.gz? O que isso significa? Quando nos deparamos com arquivos do tipo .tar.gz, significa que dois processos ocorreram. O primeiro é o empacotamento dos arquivos no formato .tar. O segundo processo é a compactação no formato gzip.

O tar apenas une todos os arquivos em um só. Mas o tar não aplica algoritmos de compactação para que o arquivo resultante fique menor. Para isso utilizamos um outro formato, como o gzip.

A vantagem é que o tar consegue manter as permissões dos arquivos, bem como links diretos e simbólicos, sendo interessante por exemplo para realizar backups.

Utilizamos o comando tar para realizar as compactações. A compactação do diretório Projetos/ ficaria da seguinte forma.

A primera coisa que você deve ter notado é que, diferente do zip, o comando tar não necessita do -r. Ele age de forma recursiva por padrão. O -c é de create, ou seja, para indicar que desejamos criar um arquivo. O -z indica que queremos compactar com gzip. Utilizamos o -f (file), para que o comando crie o arquivo compactado.

Para descompactar, basta utilizar o -x de extract no lugar do -c.

O comando tar, ao contrário do zip, é silencioso (quiet) por padrão. Se quisermos que ele imprima os detalhes do que está fazendo, basta utilizar o argumento -v (verbose).

Se compararmos os tamanhos do arquivo .zip e do .tar.gz vamos perceber que nesse caso o .tar.gz ficou menor, mas isso não necessariamente irá sempre ocorrer.
"""

c_texto_1 = Counter(texto_1.lower())

print(c_texto_1)
total_caracteres_1 = sum(c_texto_1.values())
print("Total de Caracteres Texto 1:", total_caracteres_1)

print("------------------------------------------------------------------")

#Construindo uma tupla de visualização
for letra, frequencia in c_texto_1.items():
    tupla = (letra, frequencia/total_caracteres_1)
    print(tupla)

print("------------------------------------------------------------------")

#Construindo uma lista para conseguir trabalhar
proporcoes = [(letra, frequencia/total_caracteres_1) for letra, frequencia in c_texto_1.items()]
proporcoes = Counter(dict(proporcoes)) #Usando o Counter, visto que ele aceita estruturas tbm.
print(proporcoes.most_common(10)) #O most_common é uma propriedade do Counter que serve para trazer os elementos mais comuns.

print("------------------------------------------------------------------")
def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_caracteres_1 = sum(aparicoes.values())

    proporcoes = [(letra, frequencia/total_caracteres_1) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))

print("Texto 1")
analisa_frequencia_de_letras(texto_1)
print("Texto 2")
analisa_frequencia_de_letras(texto_2)