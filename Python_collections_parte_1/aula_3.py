#Herança e Polimorfismo
from abc import abstractmethod, ABCMeta


class Conta(metaclass = ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo #Indicamos que os atributos dessa classe são privados
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod #Linha 66
    def passa_o_mes():
        raise NotImplementedError

    def __str__(self):
        return "[>>Código {} Saldo {}<<]".format(self._codigo, self._saldo)

#Agora vamos criar duas classes filhas da classe Conta. Cada uma com um objetivo diferente.
class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

conta16 = ContaCorrente(16)
conta16.deposita(1000)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)

contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes() #duck typing
    print(conta)

'''
Array em python é algo que deve ser evitado utilizar, ele tem um comportamento muito específico e voltado a números.
Ele possui uma biblioteca própria que devemos importar antes de utilizar:
    import array as arr
E para podemos utiliza-lo, temos que declarar o tipo e os elementos que o compõem na construção.
    arr.array('d', [1, 3.5])

Para verificar tipos do array e funcionalidades: https://docs.python.org/3/library/array.html
'''

'''
Mas mesmo com a estrutura do array voltada para números, quando queremos trabalhar com problemas matemáticos em python, 
utilizamos a biblioteca Numpy:
    Instalação em código: !pip install numpy

    import numpy as np

    np.array([1., 3.5])

Utilizado para data science, para engenharia científica
Referência: https://numpy.org/
'''

'''
Como queremos que as classes filhas ContaCorrente e ContaPoupanca implementem o método passa_o_mes(), podemos declarar
ele como uma classe abstrata em Conta. O que indica que ele vai ter que ser implementado nas classes filhas. 
Se ele não for implementado, quando quisermos instanciar um objeto ele vai dar um erro.
'''