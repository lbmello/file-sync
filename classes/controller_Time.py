"""Gerencia os dados de tempo lidos por model.Time."""


from model_Time import model_Time


class controller_Time():
    """Gerencia os dados de tempo lidos por model.Time."""

    def __init__(self):
        """Instância de model.Time."""
        _time = model_Time()
        self.times = _time.get_times()
        self.time_default = _time.get_time_default()

    def format_date(self, json_days):
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


if __name__ == "__main__":
    teste = controller_Time()
    print(teste.format_date("MTWT_SS"))
