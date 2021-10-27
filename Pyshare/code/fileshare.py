import os
import socket
from os.path import abspath
from inspect import getsourcefile


class FileShare:
    ''' FileShare is main logic on which the pyshare runs. '''
    def __init__(self, bind_ip='127.0.0.1', port='8000', directory=None, folder=None):
        ''' initializing the FileShare class'''

        # app related meta data
        self._appinfo = {
            'author':'FatinShadab',
            'name':'Pyshare',
            'version':'v1.0a1',
            'github':'https://github.com/FatinShadab/Pyshare',
        }
        # app configuration
        self._ip = bind_ip
        self._port = port
        self._link = f"http://{bind_ip}:{port}"
        self._Os_type = os.name
        self._device_name = socket.gethostname()
        self._target_folder = folder
        if directory != None:
            self._target_dir = directory[0:2]
        else:
            self._target_dir = abspath(getsourcefile(lambda:0))[0:2]

    def starting_text(self):
        ''' This method provides starting logs to the user. '''

        if self._target_folder is None:
            return (f'[∞] Hosting {self._target_dir}/* from {self._device_name} at {self._link}\n\n[*]Logs -->')
        else:
            return (f'[∞] Hosting {self._target_dir}/{self._target_folder} from {self._device_name} at {self._link}\n\n[*]Logs -->')
            
    def run(self):
        ''' The run method calls the other methods of the fileshare class and start the server. '''

        print(self.starting_text())
        # This block of code checks the os type of the user and run cmd-line commands according to the os type. 
        if self._Os_type == 'nt':
            if  self._target_folder is None:
                os.system(f"{self._target_dir}& python -m http.server {self._port} --bind {self._ip}")
                
            else:
                os.system(f"{self._target_dir}& python -m http.server {self._port} --bind {self._ip} -d /{self._target_folder}/")
                
        else:
            if self._target_folder == None:
                os.system(f"{self._target_dir}; python3 -m http.server {self._port} --bind /{self._ip}/")
            else:
                os.system(f"{self._target_dir}; python3 -m http.server {self._port} --bind {self._ip} -d /{self._target_folder}/")