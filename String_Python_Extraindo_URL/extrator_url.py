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


url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)
print("O tamanho da URL é:", len(extrator_url))
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
#Imprime o valor que determinamos dentro do __str__
print(extrator_url)

#Agora outro método a ver é o __eq__, que serve para comparar valores dos elementos na comparação '=='.
#O método __eq__ verifica se os dois objetos estão apontado para o mesmo endereço. Mas nesse caso queremos que se o valor da
#URL for igual, ele retorne como verdadeiro.
print(extrator_url == extrator_url_2) #Se não implementarmos o __eq__ dentro do objeto, ele retorna como falso.
