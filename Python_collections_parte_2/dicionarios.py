'''
Como podemos ter situações onde queremos um determinado valor associado a uma chave específica, podemos criar um dicionário.
O type dicionário é o dict. Para consultar o valor associado a uma chave especifíca, utilizamos nome_dicionario['nome_chave'].
Caso faça sentido sempre trazer algum valor padrão mesmo que não tenha a chave dentro do dicionário, podemos usar o método
get(). Já que se existir a chave traz o valor associado, mas se não existir traz o valor designado no get().
'''

from collections import defaultdict, Counter


aparicoes = {
    "Guilherme": 2,
    "cachorro": 2,
    "nome": 2,
    "vindo": 1,
}

print(type(aparicoes))

print(aparicoes['Guilherme'])

print(aparicoes.get('xpto', 0))

print(aparicoes.get('nome', 0))

#Podemos também usar o construtor para criar o dicionário.
aparicoes_c = dict(
    Guilherme= 2,
    cachorro= 2,
    nome= 2,
    vindo= 1,
)

print(aparicoes_c)

#Inserindo novos elementos no dicionário
aparicoes['Carlos'] = 1

print(aparicoes)

#Removendo elementos do dicionário
del aparicoes['Carlos']

print(aparicoes)

#Verificar se elemento está no dicionário
print('cachorro' in aparicoes)

print('carlos' in aparicoes)

print("--------------------------------------------------------------------------")

#Passando por todas as chaves
for elemento in aparicoes:
    print(elemento)

print("Outra Maneira: ")
for elemento in aparicoes.keys():
    print(elemento)

#Passando por todos os valores
for elemento in aparicoes.values():
    print(elemento)

#Passando por todos os itens (Chave + Valor)
for elemento in aparicoes.items():
    print(elemento)

#Como o retorno da combinação de chave e valor é uma tupla, podemos desempacotar os valores.
for chave, valor in aparicoes.items():
    print(chave, "=", valor)

["palavra {}".format(chave) for chave in aparicoes.keys()] #Aqui vamos trazer uma lista de chaves.

print("--------------------------------------------------------------------------")

meu_texto = "Bem vindo meu nome é Bruno eu gosto muito de programar e de ver animes"
meu_texto = meu_texto.lower() #Vamos converter a frase toda em minúsculos.

dict_frase = {}

#Queremos contar quantas vezes cada palavra aparece na frase acima
for palavra in meu_texto.split(): #Primeiro vamos separar as frases palavra por palavra
    ate_agora = dict_frase.get(palavra, 0) #Agora vamos verificar se já existe uma chave dessa palavra no dicionário. Se não, retorna 0.
    dict_frase[palavra] = ate_agora + 1 #Aqui adicionamos mais 1 ao valor associado a chave.

print(dict_frase)

#Utilizando o defaultdict

ddict_frase = defaultdict(int) #Precisamos passar uma função que vai retornar o valor padrão desse dicionário. Aqui usamos o int para o valor padrão ser 0.

for palavra in meu_texto.split():
    ate_agora = ddict_frase[palavra]
    ddict_frase[palavra] = ate_agora + 1

print(ddict_frase)

print("--------------------------------------------------------------------------")

#Agora vamos ver como usar essa estrutura do dict usando objetos próprios.
class Conta:
    def __init__(self):
        print("Criando uma conta")

contas = defaultdict(Conta) #Cada vez que chamarmos esse defaultdict e não existir essa conta, ele cria uma nova.
contas[15]
contas[17]

print("--------------------------------------------------------------------------")

#Outra função dentro do collections que temos é o Counter (Contador)
#O Counter ele tem como valor default o 0, mas ele ainda permite inserir o que queremos converter como dicionário diretamente
#no parâmetro e já faz a contagem dos elementos.

apar = Counter(meu_texto.split())

print(apar)