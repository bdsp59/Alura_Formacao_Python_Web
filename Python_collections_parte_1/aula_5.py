#Enumerated / Desempacotando tuplas

'''
Se quisermos associar os valores de uma lista a sua posição na lista, podemos fazer uso do enumerate, que é um método
específico do python.
Mas o enumerate cria a estrutura para podemos utiliza-la, se apenas chamarmos o método e não atribuirmos nada a ele,
não teremos como manipular os seus elementos. Para isso podemos colocar o resultado do enumerate em uma lista.
'''

idades = [15, 87, 32, 65, 56, 32, 49, 37]

for valor in list(enumerate(idades)):
    print(valor)
    #Nesse caso vamos imprimir várias tuplas, visto que a posição daquele elemento na lista nunca vai mudar.

#Mas para podermos trabalhar com esse valores podemos desempacotar esses valores da tupla, fazendo:
print('------------------------------------------------')
for indice, idade in list(enumerate(idades)):
    print(indice, idade)
print('------------------------------------------------')
#Quando desempacotamos os valores, podemos imprimir apenas um dos valores.
for indice, idade in list(enumerate(idades)):
    print(indice)
print('------------------------------------------------')
#Mas quando temos a estrutura acima para desempacotar os elementos da tupla, obrigatoriamente tempos que colocar no
#for a quantidade de elementos que a tupla possui, apesar podermos querer só um valor. Para isso devemos completar
#a chamada desses outros elementos com '_'.
for indice, _ in list(enumerate(idades)):
    print(indice)
print('------------------------------------------------')