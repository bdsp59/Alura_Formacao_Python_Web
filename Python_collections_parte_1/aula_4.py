
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro): #Buscar abaixo a explicação
        if type(outro) != ContaSalario: #Primeiro verificamos se os objetos que queremos comparar são do mesmo tipo
            return False

        #Se fizer sentido extender essa igualdade de tipo para as classes filhos dessa classe, devemos utilizar o isinstance().

        return self._codigo == outro._codigo and self._saldo == outro._saldo 
        #É uma boa prática comparar todos os atributos dos objetos para verficar se realmente são o mesmo.

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Código {} Saldo {}<<]".format(self._codigo, self._saldo)

conta1 = ContaSalario(37)
print(conta1)

conta2 = ContaSalario(37)
print(conta2)

print(conta1 == conta2)
'''
Apesar de a conta1 e conta2 parecerem ter a mesma estrutura, visto que possuem o mesmo código e o mesmo saldo, se
utilizarmos o '==' para comparar os dois vamos receber o valor False. 
Isso ocorre pois o '==' só compara se os dois objetos apontam para o mesmo espaço de memória.
Para criarmos um método específico de comparar a igualdade entre dois objetos devemos definir o método __eq__ dentro
da classe.

Todas as funções que precisam de comparação vão fazer uso do '==', por isso devemos definir o __eq__ para a nossa classe
quando quisermos alguma funcionalidade diferente.
'''

