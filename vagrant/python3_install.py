#!/usr/bin/python

import platform
import subprocess
from fnmatch import fnmatch

my_os = (platform.linux_distribution()[0])
my_os = my_os.lower()

centos = fnmatch(my_os, '*cent*')
ubuntu = fnmatch(my_os, '*ubuntu*')

if centos == True:
    script = ['echo "nameserver 8.8.8.8" >> /etc/resolv.conf',
              'yum update -y && yum upgrade -y',
              'yum install -y python3',
              'yum install -y python3-pip', 
              'pip3 install -r /etc/filesync/venv_dep.txt']
    
    for line in script:
        subprocess.call(line, shell=True)

if ubuntu == True:
    script = ['apt-get install -y software-properties-common',
              'add-apt-repository -y ppa:deadsnakes/ppa',
              'apt-get update',
              'apt-get -y install python3.6',
              'pip3 install -r /etc/filesync/venv_dep.txt']

    for line in script:
        subprocess.call(line, shell=True)