from datetime import datetime


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today() #Retorna o dia, hora, minuto, segundo e milisegundos do mommento da execução desse código

    def __str__(self):
        return self.fotmat_data()

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

    def fotmat_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        # O %Y, traz o valor do ano com 4 dígitos. O %d traz o dia e o %m traz o mês. O %H traz a hora e o %M os minutos.
        # Assim fazemos a formatação da data como estamos aptuados no Brasil.
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro
