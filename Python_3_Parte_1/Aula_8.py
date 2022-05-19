def jogar_forca():
    print("************************************")
    print("Bem vindo ao jogo da forca!")
    print("************************************")

    print("Fim do jogo.")

#Como agora definimos funções para esses arquivos, se chamarmos apenas esses arquivos, não veremos a execução do jogo.
#Então precisamos fazer uma chamada a função no nosso código.
#Mas se apenas colocarmos direto no código ao se importar esse arquivo, em jogos.py, já será executado a função, sem deixar o usuário escolher qual jogo deseja.
#Por isso será necessário se acrescentar um if para executar apenas quando esse arquivo for executado diretamente.
if(__name__  == "__main__"):
    jogar_forca()
