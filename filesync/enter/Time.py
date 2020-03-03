"""Formata e retorna os dados de tempo lidos por data.Time."""


from ..data.Time import Time as data_time
from datetime import datetime


class Time():
    """Gerencia os dados de tempo lidos por model.Time."""

    def __init__(self):
        """Instância de model.Time."""
        _time = data_time()
        self.times = _time.get_times()
        self.time_default = _time.get_time_default()

    def get_week(self, json_days):
        """Formata os dados de dias da semana lidos (str) do campo SCHEDULE de
        conf/Time.JSON e retorna lista (int) com os respectivos dias, no
        formato aceito pelo crontab."""
        days = json_days

        days = [days[start:start+1] for start in range(0, len(days), 1)]

        _monday = days[0].upper()
        _tuesday = days[1].upper()
        _wednesday = days[2].upper()
        _thursday = days[3].upper()
        _friday = days[4].upper()
        _saturday = days[5].upper()
        _sunday = days[6].upper()

        _new_date = []

        if _monday == "M":
            _new_date.append(1)
        elif _monday == "_":
            pass
        else:
            raise ValueError("Entrada inválida!")

        if _tuesday == "T":
            _new_date.append(2)
        elif _tuesday == "_":
            pass
        else:
            raise ValueError("Entrada inválida!")

        if _wednesday == "W":
            _new_date.append(3)
        elif _wednesday == "_":
            pass
        else:
            raise ValueError("Entrada inválida!")

        if _thursday == "T":
            _new_date.append(4)
        elif _thursday == "_":
            pass
        else:
            raise ValueError("Entrada inválida!")

        if _friday == "F":
            _new_date.append(5)
        elif _friday == "_":
            pass
        else:
            raise ValueError("Entrada inválida!")

        if _saturday == "S":
            _new_date.append(6)
        elif _saturday == "_":
            pass
        else:
            raise ValueError("Entrada inválida!")

        if _sunday == "S":
            _new_date.append(7)
        elif _sunday == "_":
            pass
        else:
            raise ValueError("Entrada inválida!")         
        
        return _new_date
        
    def get_time(self, id_time):
        _time = self.times[id_time]

        _date = '*'
        _operator = '*'
        _minute = '*'
        _hour = '*'
        _day_month = '*'
        _month_of_year = '*'
        _day_of_week = '*'
        _special = '*'        
        
        """ Operador EVERY."""
        if _time['OPERATOR'] == 'EVERY':
            _operator = '--every--'
            
            # A CADA MINUTO
            if _time['TIME_UNITY'] == 'MIN':
                _minute = _time['FREQUENCY']
            
            # A CADA HORA ESPECIFICA
            if _time['TIME_UNITY'] == 'HRS':
                _hour = _time['FREQUENCY']

            # A CADA DIA
            if _time['TIME_UNITY'] == 'DAY':
                _hour = _time['FREQUENCY']
        
            # A CADA MÊS    
            if _time['TIME_UNITY'] == 'MTH':
                _month_of_year = _time['FREQUENCY']

        
        """ Operador IN."""
        if _time['OPERATOR'] == 'IN':
            _operator = '--in--'
            
            # APENAS NO DIA X DO MÊS Y
            if _time['TIME_UNITY'] == 'SPECIFIC_DAY':
                input_date = _time['FREQUENCY']

                input_date = input_date.split('/')

                _month = int(input_date[0])
                _day = int(input_date[1])
                _year = int(input_date[2])

                date = datetime(year = _year, 
                                day = _day, 
                                month = _month)

                _date = date            
                
        """ Operador SPECIAL."""
        if _time['OPERATOR'] == 'SPECIAL':
            _operator = '--special--'

            # A CADA HORA GENERICA
            if _time['FREQUENCY'] == 'HOURLY':
                _special = '@hourly'

            # DIARIAMENTE, NO DIA QUE FOI CONFIGURADO (FREQUENCY = DAILY)
            if _time['FREQUENCY'] == 'DAILY':
                _special = '@daily'

            # SEMANALMENTE, NO DIA QUE FOI CONFIGURADO (FREQUENCY = WEEKLY)
            if _time['FREQUENCY'] == 'WEEKLY':
                _special = '@weekly'

            # MENSALMENTE, NO DIA QUE FOI CONFIGURADO (FREQUENCY = MONTHLY)
            if _time['FREQUENCY'] == 'MONTHLY':
                _special = '@monthly'

            # NO REBOOT
            if _time['FREQUENCY'] == 'REBOOT':
                _special = '@reboot'


        """ Leitura dos dias da semana."""
        _day_of_week = self.get_week(_time['SCHEDULE'])

        return [_operator, _date, _minute, _hour, _day_month, _month_of_year, _day_of_week, _special]

if __name__ == "__main__":
    pass
