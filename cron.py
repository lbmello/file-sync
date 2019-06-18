from lib import json_reader as jreader

# LÊ OS DADOS DE TEMPO
time_default, time_lab = jreader.json_time_read()

# SEPARA OS DADOS EM VARIÁVEIS
default_schedule = time_default['SCHEDULE']
default_time_unity = time_default['TIME_UNITY']
default_frequency = time_default['FREQUENCY']

lab_schedule = time_lab['SCHEDULE']
lab_time_unity = time_lab['TIME_UNITY']
lab_frequency = time_lab['FREQUENCY']

# CONFERE OS VALORES
default_schedule = list(default_schedule)

diario = []

print(default_schedule)
for i in range(len(default_schedule)):
    if default_schedule[i] == "U" or default_schedule[i] == "u":
        diario.append(0)
        print("Domingo")
    
    elif default_schedule[i] == 'M' or default_schedule[i] == 'm':
        diario.append(1)
        print("Segunda")

    elif default_schedule[i] == 'T' or default_schedule[i] == 'T':
        diario.append(2)
        print("Terça")

    elif default_schedule[i] == "W" or default_schedule[i] == "w":
        diario.append(3)
        print("Quarta")

    elif default_schedule[i] == "T" or default_schedule[i] == "t":
        diario.append(5)
        print("Quinta")

    elif default_schedule[i] == "F" or default_schedule[i] == "f":
        diario.append(6)
        print("Sexta")

    elif default_schedule[i] == "S" or default_schedule[i] == "s":
        diario.append(7)
        print("Sábado")
    
    else:
        print("Caractere inválido!")
        break

print(diario)