from operator import attrgetter


class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo 

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Código {} Saldo {}<<]".format(self._codigo, self._saldo)

conta_do_guilherme = ContaSalario(120)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(23)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)

print("-------------------------------------------------------")
print(conta_da_daniela < conta_do_guilherme)

for conta in sorted(contas):
    print(conta)

'''
Mas podemos ter a situação onde temos duas contas com saldos iguais, então temos que organizar como deve acontecer nessa 
sitação. No caso da conta salário o segundo critério de organização é o código da conta. Podemos estabelecer a ordem
utilizando o attrgetter().
Mas como queremos utilizar essa ordenação com ordem, em qualquer situação, então vamos adicionar a estrutura da classe.
'''
print("-------------------------------------------------------")
for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
    print(conta)

print("-------------------------------------------------------")
for conta in sorted(contas):
    print(conta)

print(conta_da_daniela <= conta_do_guilherme)