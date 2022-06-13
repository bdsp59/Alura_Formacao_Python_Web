#Dicionário
#É uma estrutura que armazena diversas variáveis dentro da sua estrutura e consegue atribuir nomes
#e associa valores a cada um deles. Podendo ser utilizados para salvar dados complexos e chamar de 
#forma mais rápida e precisa esses valores.
#conta = {"numero": 123, "titular": "Bruno", "saldo": 55.0, "limite": 1000}

#Criando o dicionário acima, agora temos tudo que compõe uma conta bancária e podemos chamar os ele-
#mentos que quisermos pelo nome e receber os valores associados a eles.
#conta["numero"]
#conta["titular"]
#conta["saldo"]
#conta["limite"]

#Podemos criar diversas contas com a mesma estrutura só alterando os valores e a variável
#conta2 = {"numero": 312, "titular": "João", "saldo": 100.0, "limite": 1000}

#Agora o que queremos é esconder esses comandos de criação e controle dessa conta.

def criar_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))

criar_conta(123, "Bruno", 120.0, 1000.0)

#A partir da aula 2, vamos separar como o código da aula. Sem separar por aulas.