from abc import ABC #Abstract Base classes -> São classes básicas abstratas, ou seja, são classes abstratas que vão servir de base para que possam ser utilizadas.
#As classes abstratas vieram para complementar o Duck Typing.
from collections.abc import MutableSequence
#Aqui vamos criar uma classe fazendo uso de uma classe abstrata já existente, python tem classes abstratas prontas disponíveis para uso.
#Nesse caso vamos usar a classe abstrata MutableSequence, e apesar de que essas classes exigem que se implemente certos métodos abstratos
#se deixarmos o código apenas assim, ele não apresenta erros. Já que 
class MinhaListinhaMutavel(MutableSequence):
    pass
#Para verificar quais classes abstratas precisamos implementar ou trazer das classes abstratas prontas temos que instanciar um objeto dessa 
# classe, e como não temos os métodos implementados na classe aparecem os erros.
objetoValidado = MinhaListinhaMutavel()
print(objetoValidado)