#sudo apt install sshpass -y
#sshpass -p "" ssh-copy-id -i /home/vagrant/.ssh/id_rsa vagrant@$ip

ip="172.10.0.3"
password="vagrant"
echo -e "\n\n\n" | ssh-keygen -t rsa -N "" -f /home/vagrant/.ssh/id_rsa
sh -c '/bin/echo -e "\n${password}"' | ssh-copy-id -i .ssh/id_rsa.pub vagrant@$ip

sh -c '/bin/echo -e "\n${mode_server}\n${ip_fog}\n${change_int}\n${int_change}\n${route_dhcp}\n${dns}\n${dhcp_server}\n${language_pack}\nY\n\n\n" | /bin/bash installfog.sh' \