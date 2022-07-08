url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar"

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

'''
Como foi verificado na manipulacao_url_2 temos um problema ao simplesmente pegar sempre até o final da String. Então
temos que pensar em uma maneira de melhorar a busca, pensando que todos os parâmetros serão separados por & podemos 
colocar ele como limitador do valor desejado.
'''

parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&')
valor = url_parametros[indice_valor:indice_e_comercial]
print(f"{parametro_busca} : {valor}")

parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&')
valor = url_parametros[indice_valor:indice_e_comercial]
print(f"{parametro_busca} : {valor}")

'''
Ao testar o código acima, podemos verificar que para 'moedaOrigem' houve um resultado, mas para 'moedaDestino' não.
Isso ocorreu porque ao acharmos o indice do e comercial para o segundo parâmetro terá um valor menor que o indice do
valor, o que o python não consegue entender fazendo retornar vazio.
'''

parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)#Vamos utilizar de um segundo argumento de find, que indica a 
#partir de qual valor devemos procurar o elemento no primeiro argumento.
valor = url_parametros[indice_valor:indice_e_comercial]
print(f"{parametro_busca} : {valor}")

parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:#Se o find não achar nenhum valor igual a &, depois do indice_valor ele retorna -1, indicando
    #que é o último parâmetro.
    valor = url_parametros[indice_valor:]
else: 
    valor = url_parametros[indice_valor:indice_e_comercial]
print(f"{parametro_busca} : {valor}")