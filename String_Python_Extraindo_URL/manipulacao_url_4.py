'''
Agora que já conseguimos separar a nossa url e ter acesso aos valores dos nossos parâmetros, mas precisamos deixar
o nosso código melhor estruturado e seguindo as boas práticas esperadas.
'''
#Primeira verificação: Se a URL enviada for vazia tem que exibir um erro ao usuário
#url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = "                          "

#Sanitização da URL -> Remover elementos e caracteres que podem atrapalhar nas nossas verificações. Neste caso espaços 
# em branco.
url = url.strip()

if url == "":
    raise ValueError("A URL está vazia!")
'''
Para o caso da url estar vazia temos que enviar o erro ao usuário e para isso usamos o 'raise ValueError()' com a 
mensagem a ser exibida. Utilizamos o raise pois ele indica ao python para encerrar a aplicação e exibir o que esteja
depois dele, já o ValueError serve para indicar que foi um erro de valor e exibe o que estiver dentro do ().
'''

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else: 
    valor = url_parametros[indice_valor:indice_e_comercial]
print(f"{parametro_busca} : {valor}")