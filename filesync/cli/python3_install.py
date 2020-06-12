#!/usr/bin/python

import platform
import subprocess
from fnmatch import fnmatch

class python3_install:

    def __init__(self):
        my_os = (platform.version())
        my_os = my_os.lower().split(' ')[0]

        centos = fnmatch(my_os, '*cent*')
        ubuntu = fnmatch(my_os, '*ubuntu*')

        if centos == True:
            self.centos()

        if ubuntu == True:
            self.ubuntu()


    def centos(self):
        """Instala Python3, PIP3 e depencencias no CentOS."""

        script = ['echo "nameserver 8.8.8.8" >> /etc/resolv.conf',
                    'yum update -y && yum upgrade -y',
                    'yum install -y python3',
                    'yum install -y python3-pip']

        for line in script:
            subprocess.call(line, shell=True)


    def ubuntu(self):
        """Instala Python3, PIP3 e depencencias no CentOS."""

        script = ['apt-get install -y software-properties-common',
                    'add-apt-repository -y ppa:deadsnakes/ppa',
                    'apt-get update',
                    'apt-get -y install python3.6']
                    
        for line in script:
            subprocess.call(line, shell=True)