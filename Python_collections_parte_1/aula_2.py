#Agora vamos trabalhar com objetos próprios.
#Aqui vamos criar a nossa classe Conta Corrente para poderemos trabalhar com ela e ver como podemos usar um objeto próprio com listas
class ContaCorrente:
    #Aqui definimos como a classe deve se comportar ao ser criada.
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    #Aqui definimos um método para adicionar algum valor a conta
    def deposita(self, valor):
        self.saldo += valor

    #Aqui definimos o que deve e como deve aparecer as informações da conta na hora da impressão
    def __str__(self):
        return "[>>Código {} Saldo {}<<]".format(self.codigo, self.saldo)

#Abaixo criamos a conta corrente do Bruno
conta_do_bruno = ContaCorrente(10)
conta_do_bruno.deposita(200)

#Aqui criamos a conta corrente da Dani
conta_da_dani = ContaCorrente(4758)
conta_da_dani.deposita(1000)

#Aqui criamos uma lista contendo as contas que temos. Aqui não instanciamos novos objetos, apenas apontamos para os objetos já criados. 
#Então não afeta em nada o que já existe, mas devemos tomar cuidado para não fazer alguma mudança que não queremos.
contas = [conta_do_bruno, conta_da_dani]

#Aqui usamos do for para conseguir imprimir as informações das contas de forma correta
for conta in contas:
    print(conta)


'''
Dependendo da maneira que queremos trabalhar com os nossos dados, temos outras estruturas que podemos utilizar.
Se queremos uma lista de elementos com tipos diferentes, mas onde não podemos alterar, adicionar ou remover elementos dessa estrutura,
devemos utilizar tuplas ao invés de listas.
Para criar uma tupla utilizamos () ao invés de [].
'''

guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

#Aqui criamos dois clientes do banco. Com o nome, idade e ano de nascimento, nesta ordem. Agora qualquer outro cliente deve ser uma tupla
# e seguir esse padrão de estrutura.

'''
Quando temos uma estrutura OO, temos que o foco é no objeto e tentamos sempre manipular o objeto.
Já na variação "funcional", temos que o foco é nos dados, ou seja, não devemos mudar os dados de forma tão simples pois eles quem são importantes.
Dentro de um programa podemos mesclar as duas variações e utiliza-las como desejarmos.

Uma regra que pode ser útil:
    'Se a posição importar, o que queremos deve ter um tamanho fixo, então é uma tupla'
    'Se a posição não fizer tanta diferença, seja para estabelecer aquele tipo ou aquele valor na posição, então é uma lista'
'''

#No mundo real, podemos misturar todas essas estruturas para adequar as funcionalidades que precisamos.

usuarios = [guilherme, daniela] #Lista de Tuplas

print(usuarios)

#Inserindo um novo usuário a lista de usuários, temos que inserir uma tupla que representa um usuário.
usuarios.append(('Paulo', 39, 1979))
print(usuarios)

