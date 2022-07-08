'''
    Quando navegamos na internet podemos perceber que a URL do site muda de acordo com certos comandos que realizamos e
    locais que acessamos. Aqui temos um exemplo de busca por 'alura' no twitter:
        https://twitter.com/search?q=alura&src=typed_query

    Nessa URL podemos identificar alguns pontos :
     - https:// -> Indica que a conexão é do tipo http com segurança
     - twitter.com -> Indica o domínio do site
     - /search -> Indica que estamos na página de busca desse domínio
     - ? -> Serve como um divisor entre a base da URL e os parâmetros
     - q=alura&src=typed_query -> Essa parte funciona como parâmetros da URL, funcionam como variáveis que são enviadas
     ao programa.
        q=alura -> O q vem de querry, que indica consulta. E alura é o que queremos consultar.
        & -> Serve para separar os parâmetros
        src=typed_query -> O src vem de source, que serve para indicar qual a origem dessa consulta. Nesse caso foi uma
        consulta digitada.
'''

url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
print(url)

'''
Agora queremos dividir a nossa url entre a parte do domínio e a parte dos parâmetros. Para isso vamos utilizar o 
fatiamento de strings. 
O fatiamento é uma funcionalidade do python que serve para pegar pedaços de string dependendo da posição inicial(inclusivo)
 e final(exclusivo) indicadas.
'''

palavra = "abcde"
print(palavra[0])
print(palavra[0:2])

#Utilizando da explicação acima podemos dividir a nossa url em base e paramêtros
url_base = url[0:26]
print(url_base)

url_parametros = url[27:78]
print(url_parametros)

'''
Apesar de conseguirmos usar o código acima para fazermos a separação que desejamos, ele não é funcional, visto que a
posição do '?' pode ser alterada e o tamanho da url tbm. Então precisamos de uma forma para controlar isso de uma 
maneira mais eficiente. Podemos fazer isso utilizando o método find() para achar o momento de parar a url_base e 
começar a url_parametros. Também vamos fazer uso de uma propriedade do fatiamento, onde não precisamos indicar a posição
inicial, se for o início da String, nem a posição final, se for o final da string.
'''

indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
print(url_base)

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)