from datetime import datetime, timedelta

from datas_br import DatasBr

cadastro_br = DatasBr()

#Retornar o momento do cadastro
print(cadastro_br.momento_cadastro)
#Retornar o mês do cadastro
print(cadastro_br.mes_cadastro())
#Retornar o dia da semana do cadastro
print(cadastro_br.dia_semana())

print("---------------------------------------------------------")
#Agora vamos utilizar formatações de texto para trazer os dados que queremos e da forma que queremos um elemento
hoje = datetime.today()

hoje_formatada = hoje.strftime("%d/%m/%Y %H:%M") #O %Y, traz o valor do ano com 4 dígitos. O %d traz o dia e o %m traz o mês. O %H traz a hora e o %M os minutos.
# Assim fazemos a formatação da data como estamos aptuados no Brasil.
print(hoje)
print(hoje_formatada)
print(type(hoje_formatada)) #Se imprimirmos o tipo dessa variável que criamos, verificamos que é do tipo String, assim sendo perdemos as funcionalidades do datetime.

print("---------------------------------------------------------")

print(cadastro_br)

print("---------------------------------------------------------")

hoje = datetime.today()
amanha = datetime.today() + timedelta(days=1, hours=20) #Vamos utilizar o timedelta para adicionar a quantidade de tempo que queremos.

#Como a classe datetime possui o __sub__ implementado é possível calcular a diferença de tempo entre duas datas.
print(amanha - hoje)

