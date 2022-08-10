import requests
from acesso_cep import BuscaEndereco

cep = 20950006

object_cep = BuscaEndereco(cep)

print(object_cep)

r = requests.get("https://viacep.com.br/ws/01001000/json/")
print(r.text) #Utilizamos o .text para trazer o texto dentro dessa requisição.

print("-----------------------------------------------------")

'''a = object_cep.acessa_via_cep()

print(type(a))
print(dir(a)) #Exibe todos os métodos que o objeto 'a' possui

print(a.text)
print(a.json())'''

print("-----------------------------------------------------")

#Como mudamos o nosso método para apenas enviar as informações que precisamos, vamos mudar a forma como chamamos os dados recebidos

bairro, cidade, uf = object_cep.acessa_via_cep()

print(bairro, cidade, uf)
