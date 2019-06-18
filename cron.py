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

def splitString(frase):
    frase = frase.upper()
    frase = list(frase)
    for x in range(0, len(frase), 2):
        concat =  str(frase[x]) + str(frase[x+1])
    return concat

# CONFERE OS VALORES
asd = splitString(default_schedule)
print(asd)


diario = ""
'''
for i in range(len()):
    if default_schedule[i] == "SU":
        diario = diario + str("0")
        print("Domingo")
    
    elif default_schedule[i] == 'MO':
        diario = diario + str("1")
        print("Segunda")

    elif default_schedule[i] == 'TU':
        diario = diario + str("2")
        print("Terça")

    elif default_schedule[i] == "WD":
        diario = diario + str("3")
        print("Quarta")

    elif default_schedule[i] == "TH":
        diario = diario + str("4")
        print("Quinta")

    elif default_schedule[i] == "FR":
        diario = diario + str("5")
        print("Sexta")

    elif default_schedule[i] == "SA":
        diario = diario + str("6")
        print("Sábado")
    '''