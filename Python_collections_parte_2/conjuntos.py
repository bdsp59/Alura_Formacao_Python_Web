usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

'''
assistiram = []

assistiram.extend(usuarios_data_science)

Como vamos apenas copiar os valores da primeira lista para a nova lista que queremos, podemos declarar a nova lista como uma
cópia da lista original.
'''

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)

print(assistiram)

print(len(assistiram))

'''
Mas da maneira que fizemos acima, vamos receber 2 reclamações sobre o e-mails. Visto que temos clientes que pertecem aos dois
cursos e vão receber e-mails duplicados.
Uma forma de resolver o problema de duplicadas é transformar a lista em um conjunto de valores, utilizando o comando set().
Visto que o conjuntos não permitem a inserção de elementos duplicados, podemos utiliza-lo desde o começo.
Mas se utilizarmos o conjunto, ele organiza a lista em uma ordem diferente da que foi inserida, então se a ordem for um fator
importante, devemos utilizar listas.
O conjunto não tem indexação, então não temos como chamar um elemento específico. Para acessar cada elemento devemos utilizar
o 'for'
'''

print(set(assistiram))

print("-----------------------------------------------------------------------------------")

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_data_science)

for usuario in set(assistiram):
    print(usuario)

#Para pegar os elementos do primeiro conjunto ou do segundo conjunto usamos o comando abaixo:
print(usuarios_data_science | usuarios_machine_learning) 

#Para pegar os elementos do primeiro conjunto e do segundo conjunto usamos o comando abaixo:
print(usuarios_data_science & usuarios_machine_learning) 

'''
Utilizar os conjuntos pode ter uma vantagem de processamento sobre a utilização de listas, visto que com listas iamos ter que 
sempre verificar nas duas listas quais elementos estão ou não em ambas.
'''

#Para pegar os elementos do primeiro conjunto que não estão no segundo conjunto usamos o comando abaixo:
print(usuarios_data_science - usuarios_machine_learning) 

#Podemos utilizar os conjuntos para verificar se algum componente pertence a ele ou não.

pdsnpml = usuarios_data_science - usuarios_machine_learning
print(15 in pdsnpml)
print(23 in pdsnpml)

#Para fazer operação de 'ou exclusivo' utilizamos:
print(usuarios_data_science ^ usuarios_machine_learning) 

'''
Tal qual as listas, podemos adicionar, remover elementos dentro de um conjunto.
Mas não vamos usar o comando append, visto que a definição de append() é inserir ao final e conjuntos não tem início e fim.
O comando para adicionar um elemento a um conjunto é o add().
'''

print("-----------------------------------------------------------------------------------")

usuarios = {1, 2, 5, 78, 34, 23, 45}
usuarios.add(12)
print(len(usuarios))

usuarios.add(78) #Apesar de usarmos o add para adicionar o 78 no conjunto, ele não altera em nada, pois o 78 já está no conjunto
print(len(usuarios))

'''
Quando criamos um conjunto ele é mútavel, tal qual uma lista, então está sujeito a todas os problemas e atenções que devemos 
ter com objetos mutáveis.
Para gerar um conjunto imutável temos que usar o frozenset() ao invés de set(). Funciona como uma tupla.
Conjuntos não se limitam apenas a números, podem ser de palavras, objetos e outras estruturas.
'''

usuarios_2 = frozenset({1, 2, 5, 78, 34, 23, 45})
print(usuarios_2)