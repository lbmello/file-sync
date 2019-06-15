import subprocess, fnmatch, multiprocessing

# Funções que respondem Y/N
def responseY():
	y = subprocess.run("echo y", shell=True)
	return y

def responseN():
	n = subprocess.run("echo n", shell=True)
	return n

# Comandos shell para comandos em listas para call do subprocess
def shellToSubprocess(command):
	fullCommand = command
	splitCommand = fullCommand.split(" ")
	return splitCommand

# Conexão SSH com o SERVER
def connect(user, ip):
	command = "ssh %s@%s" %(user, ip)
	subprocess.run(command, shell=True)

# Troca de chave SSH
def generateKey(user):
	command = ("ssh-keygen -t rsa -N '' -f /home/%s/.ssh/id_rsa" %user)
	run = subprocess.run([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, universal_newlines=True)
	return run

def verifyReturn(ret_stdout):
	# POSSIBILIDADES DE EXPRESSÃO REGULAR QUE COMBINE COM A RESPOSTA
	overwrite = fnmatch.fnmatch(ret_stdout, '*Overwrite*')

	if overwrite == True:
		print("Caralo borracha mano!")
		responseY()
	else:
		print("NÃO TRATADO!")

# INSTANCIA OBJETO, GRAVA SAIDA DO SHELL NA VARIAVEL E INICIA UM SUBPROCESSO QUE PROCESSA O RETORN0
teste = generateKey('vagrant')

saida = teste.stdout

p1 = multiprocessing.Process(target=verifyReturn, args=(saida,))
p1.start()
p1.join()

# target=command, stderr=subprocess.PIPE, stdin=subprocess.PIPE, timeout=5, args='vagrant'
# connect("vagrant", "172.10.0.2")
