from cpf_cnpj import Documento

cpf = "14669608762"

object_cpf = Documento.cria_documento(cpf)

print(object_cpf)

cnpj = "35379838000112"

object_cnpj = Documento.cria_documento(cnpj)

print(object_cnpj)
