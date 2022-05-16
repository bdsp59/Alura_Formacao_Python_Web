#Como funciona o comando print e suas variações
print("Hello World!\nOlá Mundo!\nHola Mundo!")
print("\n\nTrocando o separador:")
print("Hello", "World", sep="-")
print("\n\nTrocando o end:")
print("Hello", "World", end="**")

#Declarando uma variável e exibindo o seu tipo
print("\n\nDeclarando variáveis e verificando os tipos:")
pais = "Itália"
print("pais -> ", type(pais))
quantidade = 4
print("quantidade -> ", type(quantidade))

#Imprimindo com variaveis
print("\n\n",pais, "ganhou", quantidade, "títulos")

#Exercicio proposto
dia = 15
mes = 10
ano = 2015
print("\n")
print(dia, mes, ano, sep="/")

#Python é uma linguagem dinâmica.
#Ela não precisa declarar o tipo da variável, ela pega automaticamente o tipo e permite 
#que o variável receba qualquer valor, que a própria linguagem já troca automaticamente.

