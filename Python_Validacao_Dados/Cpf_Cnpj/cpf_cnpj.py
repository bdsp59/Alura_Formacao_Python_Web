from validate_docbr import CPF, CNPJ


#Como o código estava muito extenso e confuso, vamos ter que refator ele e distribuir de forma mais clara as suas funções
class Documento: #Essa será uma classe do tipo factory, que vai servir para levar o nosso programa ao caminho correto dependendo do que queremos
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos está incorreta")


class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf Inválido!!")

    def __str__(self):
        return self.format()

    def valida(self, documento): #Vamos verificar se o CPF é válido, se segue os padrões estabelecidos
        validador = CPF()
        return validador.validate(documento)

    def format(self): #Vamos imprimir o CPF no formato esperado, com uma mascára para o formato 000.000.000-00
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cnpj Inválido!!")

    def __str__(self):
        return self.format()

    def valida(self, documento): #Vamos verificar se o CNPJ é válido, se segue os padrões estabelecidos
        validador = CNPJ()
        return validador.validate(documento)

    def format(self): #Vamos imprimir o CNPJ no formato esperado, com uma mascára para o formato 00.000.000/0000-00
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
