"""
Python BBS

This is a Python3 driven Bulletin Board Service. This feature of Intrukit
is standalone and does not require any other feature of Intrukit.

The BBS allows users to implement:

    1. A forum messaging service
    2. A FTP service for file transfer
    3. ...

"""

import subprocess, socket

class Module:
    """
    Module Class
    """

    __title__ = 'bbs/bbs_server'
    __date__ = '2021-04-15'
    __rank__ = 'normal'
    __description__ = 'Python3 drive Bulletin Board System'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def __init__(self, LHOST=None, LPORT=41374):
        """
        Initialize the module with the module's desired options

        :param LHOST:
        :param LPORT:


        """
        self.__dict__['LHOST'] = {"value": LHOST, "required": True, "description": "Local host"}
        self.__dict__['LPORT'] = {"value": LPORT, "required": True, "description": "Local port"}

    def run(self):
        """
        run(self)

        :return:

        Run the module
        """
        if self.LHOST['value'] and self.LPORT['value']:
            pass