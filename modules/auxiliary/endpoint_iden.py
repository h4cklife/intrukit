"""
Page/Dir Bruteforcer

Reference: Lynda.com - Web Application Penetration Testing with Python
"""

import requests
from threading import Thread
import sys
import time
import getopt
import re
import hashlib
from termcolor import colored

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Module:
    """
    Module Class
    """

    __title__ = 'auxiliary/endpoint_iden'
    __date__ = '2017-11-16'
    __rank__ = 'normal'
    __description__ = 'Website dir/page endpoint bruteforce tool capable of taking screenshots of identified targets'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def __init__(self,
                 URL='http://192.168.2.186/FUZZ.php',
                 DICTIONARY='resources/wordlist/common.txt',
                 THREADS=1,
                 HIDECODE='000',
                 SCREENSHOTS=False,
                 SSDIR='results/images/'):
        """
        __init__(self, 
                 URL='http://192.168.2.186/FUZZ.php', 
                 DICTIONARY='resources/wordlist/common.txt', 
                 THREADS=1, 
                 HIDECODE='000')
        
        :param URL: 
        :param DICTIONARY: 
        :param THREADS: 
        :param HIDECODE: 
        :param SCREENSHOTS: 
        :param SSDIR: 
        
        Initialize the module class with the desired options and default values
        """
        self.__dict__['URL'] = {"value": URL,
                                "required": True,
                                "description": "The target URL"}

        self.__dict__['DICTIONARY'] = {"value": DICTIONARY,
                                       "required": True,
                                       "description": "Dictionary file to use"}

        self.__dict__['THREADS'] = {"value": THREADS,
                                    "required": True,
                                    "description": "Number of threads"}

        self.__dict__['HIDECODE'] = {"value": HIDECODE,
                                     "required": True,
                                     "description": "Response code to hide"}

        self.__dict__['SCREENSHOTS'] = {"value": SCREENSHOTS,
                                        "required": True,
                                        "description": "Enabled screenshots of the identified pages"}

        self.__dict__['SSDIR'] = {"value": SSDIR,
                                  "required": True,
                                  "description": "Directory to store screenshots"}

    def run(self):
        """
        run(self)
        
        :return: 
        
        Perform the modules run process
        """
        if self.URL['value'] and self.DICTIONARY['value'] and self.THREADS['value'] and self.HIDECODE['value'] \
                and self.SSDIR['value']:
            class request_performer(Thread):
                """
                request_performer(Thread)
                
                :param Thread:
                """
                def __init__(self, word, url, hidecode, screenshots, ssdir):
                    """
                    __init__(self, word, url, hidecode, screenshots, ssdir)
                    
                    :param word: 
                    :param url: 
                    :param hidecode: 
                    :param screenshots: 
                    :param ssdir: 
                    
                    Initialize with the passed values
                    """
                    Thread.__init__(self)
                    try:
                        self.word = word.split("\n")[0]
                        self.urly = url.replace('FUZZ', self.word)
                        self.url = self.urly
                        self.hidecode = hidecode
                        self.screenshots = screenshots
                        self.ssdir = ssdir
                    except Exception as e:
                        print(e)

                def run(self):
                    """
                    run(self)
                    
                    :return: 
                    
                    Run
                    """
                    start = time.time()
                    r = requests.get(self.url)
                    elaptime = time.time()
                    totaltime = str(elaptime - start)
                    lines = str(r.content).count("\n")
                    chars = str(len(r._content))
                    words = str(len(re.findall("\S+", r.content.decode('utf-8'))))
                    code = str(r.status_code)
                    hash = hashlib.md5(bytes(r.content)).hexdigest()

                    if r.history != []:
                        first = r.history[0]
                        code = str(first.status_code)
                    else:
                        pass
                    if self.hidecode != code:
                        """Print our results with color coded response status"""
                        if '200' <= code < '300':
                            """Disabled screenshots. Error that has not been debugged. Code moved from python2"""
                            if self.screenshots:
                                dcap = DesiredCapabilities.PHANTOMJS
                                driver = webdriver.PhantomJS(desired_capabilities=dcap)
                                time.sleep(2)
                                driver.set_window_size(1024, 768)
                                driver.get(self.url)
                                driver.save_screenshot(str(self.ssdir)+self.word+".png")
                            print(str(totaltime) + "  \t" + colored(code, 'green') +
                                  "\t" + str(chars) + "\t" + str(words) + "\t" + str(lines) +
                                  "\t" + str(hash) + "\t" + str(self.word))
                        elif '400' <= code < '500':
                            print(str(totaltime) + "  \t" + colored(code, 'red') + "\t" +
                                  str(chars) + " \t" + str(words) + "\t" + str(lines) + "\t"
                                  + str(hash) + "\t" + str(self.word))
                        elif '300' <= code < '400':
                            print(str(totaltime) + "  \t" + colored(code, 'blue') + "\t" +
                                  str(chars) + "\t" + str(words) + "\t" + str(lines) + "\t" +
                                  str(hash) + "\t" + str(self.word))
                    else:
                        pass
                    i[0] = i[0] - 1  # Here we remove one thread from the counter



            def start(url, dict, threads, hidecode, screenshots, ssdir):
                """
                start(url, dict, threads, hidecode, screenshots, ssdir)
                
                :param url: 
                :param dict: 
                :param threads: 
                :param hidecode: 
                :param screenshots: 
                :param ssdir: 
                :return: 
                
                Start the bruteforce process
                """
                try:
                    f = open(dict, "r")
                    words = f.readlines()
                except:
                    print("Failed opening file: " + dict + "\n")
                    sys.exit()
                launcher_thread(words, threads, url, hidecode, screenshots, ssdir)


            def launcher_thread(names, th, url, hidecode, screenshots, ssdir):
                global i
                i = []
                resultlist = []
                i.append(0)
                print("-------------------------------------------------------------------------------------------------------------")
                print("Time" + "\t\t\t" + "Code" + "\tChars \t Words \tLines \t MD5 \t\t\t\t\t String")
                print("-------------------------------------------------------------------------------------------------------------")
                while len(names):
                    try:
                        if int(i[0]) < int(th):
                            n = names.pop(0)
                            i[0] = i[0] + 1
                            thread = request_performer(n, url, hidecode, screenshots, ssdir)
                            thread.start()

                    except KeyboardInterrupt:
                        print("Finishing attack..")
                        sys.exit()
                    thread.join()
                return

            """
            This is where we actually call start in the module class's run function
            """
            try:
                url = self.URL['value']
                dict = self.DICTIONARY['value']
                threads = self.THREADS['value']
                hidecode = self.HIDECODE['value']
                screenshots = self.SCREENSHOTS['value']
                ssdir = self.SSDIR['value']
                start(url, dict, threads, hidecode, screenshots, ssdir)
            except KeyboardInterrupt:
                print("Killing all threads!!")
