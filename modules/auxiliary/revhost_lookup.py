"""
Reverse hostname lookup

This module will perform a reverse hostname lookup against a target network

"""

import subprocess

class Module:
    """
    Module Class
    """

    __title__ = 'auxiliary.revhost_lookup'
    __date__ = '2018-01-25'
    __rank__ = 'normal'
    __description__ = 'Perform a reverse hostname lookup against a target network'

    __author__ = 'Example'

    def __init__(self, NETWORK='192.168.1'):
        """
        __init__(self, NETWORK='192.168.1')

        :param NETWORK:

        Initialize the module with the module's desired options
        """
        self.__dict__['NETWORK'] = {"value": NETWORK, "required": True,
                                    "description": "The target network first 3 octet"}

    def run(self):
        """
        run(self)

        :return:

        Run the module
        """
        if self.NETWORK['value']:
            print('Please wait....\n')
            results = subprocess.check_output('for i in $(seq 1 255);do host {}.$i;done | grep -v "not found"'.format(
                self.NETWORK['value']), shell=True).decode('utf-8')
            print(results)
        else:
            print("You are missing required module options. Please see: show options")

