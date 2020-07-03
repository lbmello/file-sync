
import logging

# TODO: Passar infrmaçoes via arquivo de conf geral do projeto
PATH = '/var/log/file-sync/'
LOG_TYPE = 'centralized'
LOG_REMOTE = 'IP_REMOTO'


class log():
    log_path = str()

    if LOG_TYPE == 'centralized':
        log_path = f'{PATH}/centralized.log'
    
    elif LOG_TYPE == 'remote':
        log_path = f'{PATH}/remote.log'

    else:
        print('[LOG] | LOG TYPE NAO TRATADO!')


    logging.basicConfig(filename = log_path,
                        filemode = 'w',
                        format = '%(asctime)s | %(levelname)s | %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')


    def __init__(self, send_log=list):
        self.send_log = send_log

        self.level = send_log[0]
        self.module = send_log[1]
        self.message = send_log[2]

        if self.level.upper() == 'INFO':
            logging.info(f'[{self.module}] - {self.message}')
        
        elif self.level.upper() == 'WARNING':
            logging.warning(f'[{self.module}] - {self.message}')

        elif self.level.upper() == 'ERROR':
            logging.error(f'[{self.module}] - {self.message}')

        elif self.level.upper() == 'DEBUG':
            logging.debug(f'[{self.module}] - {self.message}')

        elif self.level.upper() == 'SCREEN':
            print(f'[{self.module}] - {self.message}')

        else:
            logging.error('[LOG] - TIPO DE NIVEL DE LOG NAO TRATADO!')


l = log(['ERROR', 'NOME_DO_MODULO', 'DEU RUIM'])