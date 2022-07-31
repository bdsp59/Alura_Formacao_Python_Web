from operator import attrgetter


idades = [18, 65, 47, 29, 54]

print("Lista original: ", idades)
print("Lista ordenanda sem alterar: ", sorted(idades))#O comando sorted ordena os elementos da lista indicada em ordem crescente sem alterar a lista original
print("Lista ordenanda inversa sem alterar: ", sorted(idades, reverse=True)) #Se passarmos o parametro reverse como True no comando sorted, ele traz a lista ordenada na ordem decrescente

#Se quisermos inverter a ordem de uma lista, sem alterar a lista original, podemos fazer uso do reversed. 
# Mas como ele não retorna uma lista, mas sim uma referência ao endereço, temos que converte-lo em um list.
print("Lista inversa sem alterar: ", list(reversed(idades)))

idades.sort() #Aqui ordenamos a lista e substituimos a lista original pela lista ordenada.
print("Lista ordenada alterada: ", idades)

print("------------------------------------------------------------------------")
'''
Acima podemos verificar que a ordenação númerica é simples de ser feita, pois os números tem uma ordem natural estabelecida, que sempre será a 
mesma, o mesmo vale para ordenação de strings. 
Mas a ordenação em strings tem um ponto de atenção, como usamos o computador, ele organiza que a ordem alfabética primeira é composta de letras
maiúsculas e depois minúsculas. Então se tentarmos ordenar palavras que começam somente com letras maiúsculas ou somente minúsculas, não há proble
ma de ordenação.
'''
nomes = ["Guilherme", "Daniela", "Paulo"]
print(sorted(nomes))

nomes = ["guilherme", "Daniela", "Paulo"]
print(sorted(nomes))

#Mas é quando temos que ordenar objetos próprio?

class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo 

    def __lt__(self, outro): #Aqui vamos estabelecer o comparativo de "<", lowerthan(lt)
        return self._saldo < outro._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Código {} Saldo {}<<]".format(self._codigo, self._saldo)

conta_do_guilherme = ContaSalario(12)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(23)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]
#Se tentarmos ordenar a lista de contas, vai aparecer um erro, pois não temos como estabelecer um padrão de ordenação desse objeto.

#Uma forma para ordenar a lista acima é passar o atributo _saldo, com o uso attrgetter, como chave da função sorted.
#attrgetter -> Método utilizado para pegar um atributo da classe, seja privado ou público, de uma maneira melhor que referenciar diretamente o atributo.
for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)

print(conta_da_daniela < conta_do_guilherme)

#Para estabelecermos uma ordem natural de ordenação apenas precisamos criar o método __lt__ dentro da classe. 
# Depois disso, podemos usar o sorted para ordenar um lista de objetos próprios segundo a classificação estabelecida em __lt__.

for conta in sorted(contas):
    print(conta)