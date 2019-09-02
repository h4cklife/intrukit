"""
SMTP Enumeration

SMTP user enumeration

"""

import sys
import socket

class Module:
    """
    Module Class
    """

    __title__ = 'auxiliary.smtp_userenum'
    __date__ = '2018-01-25'
    __rank__ = 'normal'
    __description__ = 'Enumerate a list of users against an SMTP host'
    __details__ = 'Provided a list of users, enumerate a SMTP host.'

    __author__ = 'Intrukit'

    def __init__(self, HOST=None, USERS='resources/wordlist/smtp.txt'):
        """
        __init__(self, HOST=None, USERS='resources/wordlist/smtp.txt')

        :param HOST:
        :param USERS:

        Initialize the module with the module's desired options
        """
        self.__dict__['HOST'] = {"value": HOST, "required": True, "description": "The target host"}
        self.__dict__['USERS'] = {"value": USERS, "required": True, "description": "Users file"}

    def run(self):
        """
        run(self)

        :return:

        Run the module
        """
        if self.HOST['value'] and self.USERS['value']:
            fh = open(self.USERS['value'], 'r')
            for u in fh.readlines():
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                connect = s.connect(self.HOST['value'], 25)
                banner = s.recv(1024)
                print(banner)
                s.send('VRFY {}{}'.format(u, '\r\n'))
                result = s.recv(1014)
                print(result)
                s.close()
            fh.close()
        else:
            print("You are missing required module options. Please see: show options")

