
from crontab import CronTab

from .Time import Time

class Cron():

    default_user = 'lucas'

    def __init__(self, id_time):
        _time = Time()
        
        self.operator, self.date, self.minute, self.hour, self.day_month, self.month_of_year, self.day_of_week, self.special = _time.get_time(id_time)

        self.crontab = CronTab(user=Cron.default_user)


    def set_crontab_every(self, command):
        job  = self.crontab.new(command=command)
        
        _cron = f'{self.minute} {self.hour} {self.day_month} {self.month_of_year} {self.day_of_week}'

        '''if self.minute != '*':
            _cron = f'{self.minute} * * * *'

        if self.hour != '*':
            _cron = f'* {self.hour} * * *'

        if self.day_month != '*':
            _cron = f'* * {self.day_month} * *'

        if self.month_of_year != '*':
            _cron = f'* * * {self.month_of_year} *'

        if self.day_of_week != '*':
            _cron = f'* * * * {self.day_of_week[0]}'''

        job.setall(_cron)
        
        self.crontab.write()

    def set_crontab_special(self, command):
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
        job  = self.crontab.new(command=command)

        job.setall(self.date)

        self.crontab.write()

    def set_crontab_all(self, command):
        if self.operator == '--every--':
            Cron.set_crontab_every(self, command)
            
        if self.operator == '--in--':
            Cron.set_crontab_in(self, command)

        if self.operator == '--special--':
            Cron.set_crontab_special(self, command)

        else:
            Cron.clear_crontab(self)

    
    def clear_crontab(self):
        pass

if __name__ == "__main__":
    teste = Cron('LAB')
    teste.set_crontab_all('/bin/echo')
    #teste.clear_crontab()
    #parei antes de modularization aqui