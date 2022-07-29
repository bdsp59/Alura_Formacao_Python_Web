#Coleções são utilizadas quando temos que trabalhar com diversos valores.

idades = [39, 30, 27, 18]

print(type(idades)) #Aqui vamos imprimir o tipo da tupla, confirmando que é um List

idades.append(25) #Aqui adicionamos o elemento 25 na List
print(idades)

idades.remove(27) #Aqui remove a primeira aparição do número 27 nesse List
print(idades)

print(25 in idades) #Aqui verificamos se o número 25 faz parte dessa List, nesse caso pertence
print(27 in idades) #Aqui verificamos se o número 27 faz parte dessa List, nesse caso não pertence

idades.insert(0, 20) #O comando insert é usado para inserir um elemento na lista, mas na posição que indicarmos
print(idades)

#O comando extend é usado para extender a lista, ou seja, adiciona os elementos da lista suporte ao final da lista original de forma a serem todos elementes da lista
idades.extend([67, 15]) 
print(idades)

idades_no_ano_que_vem = [(idade+1) for idade in idades] #Aqui criamos uma outra lista composta pelo valores contidos na lista idades acrescidos de 1
print(idades_no_ano_que_vem)

[(idade+1) for idade in idades if idade>21] #Aqui vamos fazer a operação de somar 1 apenas a quem for maior que 21

#Essas estruturas de criação de listas são chamadas de list comprehension

'''
Apesar de listas mutáveis serem práticas de serem utilizadas, elas podem apresentar problemas.
Um dos problemas é o fato de que quando temos dois objetos apontado para essa lista, se alteramos algo em um desses objetos também irá afetar 
o outro. O que pode não ser bom dependendo do que queremos fazer.

Outro problema que podemos ter é:
    -Se criarmos um método com a seguinte estrutura:
        def faz_processamento(lista = []):
            print(len(lista))
            lista.append(13)

        No código acima, temos que se na chamada desse método não passarmos um parâmetro, ele atribui um lista vazia. Mas o problema dessa estrutura
        é o fato que essa lista continua existindo, então se chamarmos esse método novamente sem paramêtros a lista agora vai ter o elemento 13 (adi
        cionado na primeira vez que chamamos esse método), o que não é o que queremos. A maneira de corrigir esse problema é reescrever o método como:

        def faz_processamento(lista = None):
            if lista is None:
                lista = []
            print(len(lista))
            lista.append(13)

'''