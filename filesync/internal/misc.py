""" Funçoes de uso geral."""

from datetime import datetime
from random import randint
from hashlib import md5


def random_md5():
    """ Gera e retrona um hash MD5 randomico, baseado na hora atual."""

    random_value = datetime.now()
    random_value = str(random_value)
    random_value = random_value.replace('-','').replace(':','').replace(' ','').replace('.','')
    random_value = random_value * (randint(0, 1000000))
    random_value = bytes(random_value, encoding='utf8')

    obj = md5()
    obj.update(random_value)

    md5_checksum = obj.hexdigest()

    return md5_checksum