
from controller_Time import controller_Time
from crontab import CronTab

class controller_Cron():

    default_user = 'lucas'

    def __init__(self):
        _time = controller_Time()
        
        self.minute, self.hour, self.day_month, self.month_of_year, self.day_of_week, self.special = _time.get_time("DEFAULT")

        self.crontab = CronTab(user=controller_Cron.default_user)


    def set_crontab_every(self, command):
        job  = self.crontab.new(command=command)
        
        if self.minute != '*':
            print('minute ', self.minute)
            job.every(self.minute).minute()
        
        if self.hour != '*':
            print('hour ', self.hour)
            job.every(self.hour).hours()

        if self.day_month != '*':
            pass

        if self.month_of_year != '*':
            job.every(self.month_of_year).month()

        if self.day_of_week != '*':
            job.day.on()

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

        self.crontab.write()

    def clear_crontab(self):
        self.crontab.remove_all()

if __name__ == "__main__":
     teste = controller_Cron()
     teste.set_crontab_special('/bin/echo')
     #teste.clear_crontab()