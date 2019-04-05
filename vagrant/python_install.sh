#!/bin/sh

apt-get update && apt-get upgrade -y

apt-get install software-properties-common python-software-properties -y

add-apt-repository ppa:jonathonf/python-3.6

apt-get update

apt-get install python3.6 -y
