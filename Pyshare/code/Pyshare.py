import os
from os.path import abspath
from inspect import getsourcefile
from fileshare import FileShare


def header():
    ''' Contains the option string. '''

    print('','-'*54,"\n *** Choose and enter the option number to continue -->\n",'-'*54)
    print(f" |1| serve {abspath(getsourcefile(lambda:0))[0:2]} on https://127.0.0.1:8000\n",'-'*54)
    print(f" |2| serve in custom settings\n",'-'*54,'\n')

def set_default():
    ''' set_default has all default value stored in a dict name _default_settings. '''

    _default_settings = {
        'bind_ip': '127.0.0.1',
        'port': 8000,
        'directory': None,
        'folder': None
    }
    return _default_settings

def failsafe():
    print('','-'*64,'\n',"*** Server stoped by host. Press R/r to restart and Q/q to exit\n",'-'*64,'\n')
    r_cmd = input("[<--'] ").lower()
    if r_cmd == 'r':
        os.system('cls')
        return r_cmd
    else:
        os.system('cls')
        r_cmd = 'q'
        return r_cmd

def run(mode):
    ''' Run function used and create the instance of FileShare class depending on the mode. '''

    # In mode 1 the instance of FileShare class is configured by the default values.  
    if int(mode) == 1:
        app = FileShare() 
        app.run()

    # In mode 2 the instance of FileShare class is configured by the custom values by user.
    if int(mode) == 2:
        print("*** Press enter 'd' to use default.\n")
        bind_ip = input("[<--']Enter local ipv6/ipv4 address (default: 127.0.0.1): ")
        if bind_ip == 'd':
            bind_ip = set_default()['bind_ip']

        port = input("[<--']Enter custom free port (default: 8000): ")
        if port == 'd':
            port = set_default()['port']

        directory = input("[<--']Enter target directory(C:) to serve (default: current directory): ")
        if directory == 'd':
            directory = set_default()['directory']

        folder = input("[<--']Enter target folder name to serve (default: All): ")
        if folder == 'd':
            folder = set_default()['folder']
        
        try:
            os.system('cls')
            app = FileShare(bind_ip=bind_ip, port=port, directory=directory, folder=folder) 
            app.run()
        except:
            os.system("cls")
            print("### Invalid Input!\n------------------\n")

def user_cmd(r_cmd=None):
    ''' This function is the main function for running the app. it's Useges recursion programming  technique. '''
    if r_cmd == None:
        header()
        cmd = input('Select option -->')
        os.system('cls')
    
        if cmd == '1':
            try:   
                run(mode=cmd)
            except:
                user_cmd(failsafe())

        elif cmd == '2':
            try:
                run(mode=cmd)
                user_cmd(r_cmd=failsafe())
            except:
                user_cmd(failsafe())

        elif cmd.lower() == 'q':
            pass

        else:
            os.system("cls")
            print("-------------------\n### Invalid Option!\n-------------------\n")
            user_cmd()

    if r_cmd == 'r':
        user_cmd()
    if r_cmd == 'q':
        pass  