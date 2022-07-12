endereco = "Avenida Marechal Rondon 796, casa 2, Rocha, Rio de Janeiro, RJ, 20950006"

import re #Regular Expression -- RegEx

#Usando a biblioteca re podemos agora criar um padrão para o nosso CEP, já que no Brasil ele sempre tem o mesmo formato.

#Aqui vamos criar o padrão que o cep é formato por 5 digitos + hífen (opcional) + 3 digitos
#cep_padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]") -> Padrão Detalhado
cep_padrao = re.compile("[0-9]{5}[-]?[0-9]{3}") 
#Padrão Simplificado: 
# - Utilizamos as {} para indicar a quantidade de vezes que repete o valor, podendo ter um limite inferior e um superior {0,1} => quantificadores
# - Utilizamos 0-9 para indicar o intervalo de valores que podem estar ali => Intervalos
#Agora vamos fazer uso de um método do próprio re.compile que faz uma busca daquele padrão na variável que queremos.
#O ? depois do hífen serve para indicar que o carácter anterior é opcional, podendo aparecer ou não.
busca = cep_padrao.search(endereco)
if busca:
    cep = busca.group() #Utilizamos o group para retornar a string encontrada no padrão que definimos anteriormente.
    print(cep)
