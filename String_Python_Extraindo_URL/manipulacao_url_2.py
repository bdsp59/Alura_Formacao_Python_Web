
url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar"

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

'''
No código acima já conseguimos separar a base dos parâmetros, mas para ser útil ao nosso programa precisamos conseguir 
o nome do parâmetro com o valor associado a ele, mas de forma separada e que possa ser utilizada no programa.
Então agora vamos ver como fazer essa separação.
'''

parametro_busca = 'moedaDestino' #Aqui definimos qual parâmetro desejamos obter
indice_parametro = url_parametros.find(parametro_busca) #Aqui localizamos o indice inicial do parametro
indice_valor = indice_parametro + len(parametro_busca) + 1#Como o valor vem após o nome do parâmetro e um sinal de igual, temos que adicionar o tamanho do parâmetro e do sinal ao indice
valor = url_parametros[indice_valor:] #Aqui indicamos para pegar o que tenha depois do indice do valor, que possivelmente é o valor.
print(valor) #O valor realmente recebe o esperado.

'''
Apesar de utilizando a estrutura acima conseguimos obter o valor correto para o parâmetro, isso ocorre pois pegamos o último parâmetro da URL, 
então não há problema pegar até o fim da string, mas se pegarmos algum parâmetro anterior, o que vai ser salvo no valor é todo o resto da String.
Assim sendo, temos que pensar em uma maneira de lidar com a separação dos valores dos parâmetros.
'''
