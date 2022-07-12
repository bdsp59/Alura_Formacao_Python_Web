'''
URLs Válidas:
    bytebank.com/cambio
    bytebank.com.br/cambio
    www.bytebank.com/cambio
    www.bytebank.com.br/cambio
    http://www.bytebank.com/cambio
    http://www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.br/cambio

URLs Inválidas:
    https://bytebank/cambio
    https://bytebank.naoexiste/cambio
    ht://bytebank.naoexiste/cambio
'''

#https://www.bytebank.com.br/cambio

import re

#Vamos utilizar o () para colocar o valor válido como aceitável para URL, visto que o () exige que tenha aquele formato. 
#Todos os padrões de re que temos, podem ser utilzidos dentro de outros, ex: http e https.
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match("https://www.bytebank.com.br/cambio") #Vamos utilizar o match no lugar do search, visto que queroemos que seja exatamente como está no padrão.

if not match:
    raise ValueError("A URL não é válido")

print("A URL é válida")