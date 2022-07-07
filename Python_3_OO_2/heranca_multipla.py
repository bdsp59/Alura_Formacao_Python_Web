#Aqui temos uma classe mãe com dados gerais para todas as classes
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

#Aqui temos duas classes filho que tem métodos que herdam de funcionário, mas os sobrescrevem e tem métodos próprios também.
class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, alurete')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas no fórum')

class Hipster():
    def __str__(self) -> str:
        return f'Hipster, {self.nome}'

#Até aqui não tem nada de diferente do que fizemos ou vimos em herança, mas agora temos uma questão. 
#Temos funcionários dentro de uma empresa que podem ser Júnior, Pleno ou Sênior. E no caso do nosso problema, o funcionário Junior somente pode
#acessar informações da Alura, mas níveis plenos e seniors podem acessar tanto Alura quanto Caelum. O que gera que para Plenos e Senior teremos 
#que trazer dados de duas classes mães, categorizando uma herança múltipla.

class Junior(Alura):
    pass

#Para fazer uma herança múltipla temos que chamar as duas classes mãe na hora de criar a nova classe.
class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass

#Aqui vamos instaciar a classe Junior e ver se ele apenas acessa os métodos da classe Alura e não da classe Caelum.
jose = Junior()
jose.busca_perguntas_sem_resposta()
#jose.busca_cursos_do_mes -> Tentamos usar o método do Caelum para a instância da classe Junior, mas ele dá erro. 

#Agora vamos instanciar a classe Pleno e tentar chamar métodos de ambas as classes mãe. Podemos ver que funciona sem problema.
luan = Pleno()
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

#Mas aqui aparece um problema da herança múltipla, tanto a classe Alura quanto a classe Caelum tem o método mostrar_tarefas(), então 
# se chamarmos esse método qual deveria aparecer?
luan.mostrar_tarefas()
#Verificamos que ele imprime o método da classe mãe Alura, mas deveria exibir de ambas as classes mães.

#Quando temos uma estrutura de herança múltipla o programa tem uma ordem de busca do método em questão. (Busca em árvore binária)
#A ordem segue o algoritmo MRO:
#Classe Atual -> 1º classe mãe(mais a esquerda) -> Classe Mãe da 1º classe -> 2º classe mãe(mais a esquerda) -> Classe Mãe da 2º classe
#Pleno -> Alura -> Funcionário -> Caelum -> Funcionário
#Por mais que a ordem de busca seja a descrita acima, o MRO tem uma classificação de melhor HEAD, ou seja, se remorvemos a classe Alura
# ele vai seguir o caminho para Funcionario, mas ele antes de encerrar vai verificar se tem alguma outra classe que se encaixe melhor, alguém
#que seja ligado a classe atual, mas com uma hierarquia equivalente a 1º classe mãe. Então ele descarta essa primeira busca a Funcionario e traz 
# o método de Caelum.
#Pleno -> Alura -> Caelum -> Funcionário

lucas = Senior('Lucas')
print(lucas)