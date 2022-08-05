from datetime import datetime


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today() #Retorna o dia, hora, minuto, segundo e milisegundos do mommento da execução desse código

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month #Aqui vamos retornar o mês relativo a data
        return meses_do_ano[mes_cadastro-1]

    def dia_semana(self):
        dia_semana_lista = [
            "segunda", "terça",
            "quarta", "quinta", "sexta",
            "sábado", "domingo"
        ]
        dia_semana = self.momento_cadastro.weekday() #Aqui vamos retornar o dia da semana relativo a data
        return dia_semana_lista[dia_semana]
