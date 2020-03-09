import threading
from time import sleep

from root import Root
from subfolder import Subfolder


root = Root()
root_folder = Subfolder()

  
th_create_folder = threading.Thread(target=Root.create_subfolder)

root_subdirs = root_folder.get_subdirs()

for sdr in root_subdirs:
    sdr = Subfolder(current_folder=f'{sdr}/')


th_create_folder.start()

sleep(15)

th_create_folder.join()



