import re


class Telefones:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.telefone = telefone
        else:
            raise ValueError("Número Incorreto")

    def __str__(self):
        return self.format_telefone()

    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        #Ao colocarmos os padrões esperados dentro de (), indicamos grupos de elementos que queremos utilizar, ou seja, eles devem estar separados assim.
        #Vamos poder trabalhar que estejam nesse padrão como se fosse um fatiamento de strings.
        #Ao colocarmos o ? indicamos que o grupo anterior a ele pode estar ou não presente no padrão estabelecido
        resposta = re.findall(padrao, telefone)

        if resposta:
            return True
        else:
            return False

    def format_telefone(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.telefone)
        numero_formatado = "+{}({}){}-{}".format(resposta.group(1), resposta.group(2), resposta.group(3), resposta.group(4))
        return numero_formatado
