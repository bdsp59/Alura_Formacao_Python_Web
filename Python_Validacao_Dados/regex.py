import re

padrao = "[0-9][a-z][0-9]" #Aqui vamos definir o padrão do texto que queremos, nessa caso número+letra+número
texto = "123 1a2 1cc aa1" #Aqui vamos definir texto que queremos testar se atendem o padrão estabelecido
resposta = re.search(padrao, texto) #Esse método do regex é responsável por realizar a busca
print(resposta) #Se retornarmos apenas assim, ele imprime algo estranho

print(resposta.group()) #Se colocarmos dessa maneira, ele imprime o resultado esperado

print("----------------------------------------------------------")
#Padrão de um E-mail
padrao_e = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
'''
Acima vemos o padrão para um e-mail:
O '\w' indica que podemos receber letras ou números.
Os valores entre {} indicam o intervalo de caracteres que podemos ter.
O @ e o . indicam que aquelas posições são fixas nesses valores. 
'''
texto_e = "aaaannnnaaaa bruno@email.com.br"
resposta = re.search(padrao_e, texto_e)
print(resposta.group())

print("----------------------------------------------------------")
#Padrão para telefone e celular
padrao_tele = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
'''
Acima definimos um padrão que vai servir tanto para telefones fixos quanto celulares.
[0-9] => Indica que pode receber qualquer valor de 0 a 9.
Os valores entre {} indica a quantidade ou intervalo de vezes que se repete o padrão anterior.
'''

texto_tele = "Eu gosto do numero 2126251234 e gosto tbm de 2122347833"

resposta = re.findall(padrao_tele, texto_tele) #O método findall tem como objetivo buscar todas as vezes que ocorre o padrão no texto e traze-los numa lista

print(resposta)

print("----------------------------------------------------------")
#Testando classe própria que criamos para telefone
from telefones_br import Telefones

telefone = "552126482633"

telefone_objeto = Telefones(telefone)
print(telefone_objeto)
