"""Classe de interface com o Crontab do Linux."""

from subprocess import run

from crontab import CronTab


class cron:
    """Classe de interface com o Crontab do Linux."""


    def __init__(self, time_obj, user, name):
        """ 
        time_obj, objeto de Time, declarado em enter.Time
        user, atributo de Config, declarado em enter.Config
        """

        self.time_object = time_obj

        self.user = user
        self.name = name
        
        (

            self.operator, 
            self.date, 
            self.minute, 
            self.hour, 
            self.day_month, 
            self.month_of_year, 
            self.day_of_week, 
            self.special

        ) = self.time_object.get_formated_time()

        self.crontab = CronTab(user = self.user)


    def set_crontab_all(self, command):
        """ Verifica entrada de self.operator e executa as funcoes de cada operador."""

        if self.operator == '--every--':
            cron.set_crontab_every(self, command)
            
        if self.operator == '--in--':
            cron.set_crontab_in(self, command)

        if self.operator == '--special--':
            cron.set_crontab_special(self, command)

        else:
            return f'nao tratado'
            #cron.clear_crontab()


    def set_crontab_every(self, command):
        """ Cria o crontab do operador --every--."""

        job  = self.crontab.new(command=command)
        
        _cron = f'{self.minute} {self.hour} {self.day_month} {self.month_of_year} {self.day_of_week}'

        if self.minute != '*':
            _cron = f'{self.minute} * * * *'

        if self.hour != '*':
            _cron = f'* {self.hour} * * *'

        if self.day_month != '*':
            _cron = f'* * {self.day_month} * *'

        if self.month_of_year != '*':
            _cron = f'* * * {self.month_of_year} *'

        if self.day_of_week != '*':
            _cron = f'* * * * {self.day_of_week}'

        job.setall(_cron)
        
        self.crontab.write()


    def set_crontab_special(self, command):
        """ Cria o crontab do operador --special--."""

        job  = self.crontab.new(command=command)

        if self.special == '@hourly':
            job.setall('0 * * * *')
       
        if self.special == '@daily':
            job.setall('0 0 * * *')

        if self.special == '@weekly':
            job.setall('0 0 * * 0')
       
        if self.special == '@monthly':
            job.setall('0 0 1 * *')

        if self.special == '@reboot':
            job.every_reboot()

        self.crontab.write()


    def set_crontab_in(self, command):
        """ Cria o crontab do operador --in--."""

        job  = self.crontab.new(command = command)

        job.setall(self.date)

        self.crontab.write()


    @classmethod
    def clear_crontab(cls):
        """ Limpa arquivo de crontab do usuario."""
        
        run('crontab -r', shell = True)
