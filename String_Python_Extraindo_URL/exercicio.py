import re


class ExtratorURL():
    def __init__(self, url: str):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\nParâmetros: " + self.get_url_parametros() + "\nURL Base: " + self.get_url_base()

    def __eq__(self, other): #O other vai ser o elemento a direita da igualdade
        return self.url == other.url #Agora essa igualdade vai retornar verdadeiro, desde que as URLs sejam iguais.

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia!")
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válido")

        print("A URL é válida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao+1:] 
        return url_parametros

    def get_valor_parametro(self, nome_parametro):
        indice_parametro = self.get_url_parametros().find(nome_parametro)
        indice_valor = indice_parametro + len(nome_parametro) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else: 
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

if moeda_origem == "dolar" and moeda_destino == "real":
    print("Total Dólar em Real: R$", int(quantidade)*VALOR_DOLAR)
elif moeda_origem == "real" and moeda_destino == "dolar":
    print("Total Real em Dólar: $",int(quantidade)/VALOR_DOLAR)