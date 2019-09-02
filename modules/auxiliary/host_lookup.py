"""
Host Lookup

This module will lookup hostnames/subdomains against a given domain.

"""

import subprocess

class Module:
    """
    Module Class
    """

    __title__ = 'auxiliary/host_lookup'
    __date__ = '2018-01-25'
    __rank__ = 'normal'
    __description__ = 'This module will lookup hostnames/subdomains against a given domain'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def __init__(self, DOMAIN='zonetransfer.me', SUBDOMAINS='resources/wordlist/subdomains.txt'):
        """
        __init__(self, DOMAIN='zonetransfer.me', SUBDOMAINS='resources/wordlist/subdomains.txt')

        :param DOMAIN:
        :param SUBS:

        Initialize the module with the module's desired options
        """
        self.__dict__['DOMAIN'] = {"value": DOMAIN, "required": True, "description": "The target host domain"}
        self.__dict__['SUBDOMAINS'] = {"value": SUBDOMAINS, "required": True, "description": "File containing subdomains"}

    def run(self):
        """
        run(self)

        :return:

        Run the module
        """
        if self.DOMAIN['value'] and self.SUBDOMAINS['value']:
            print('Please wait....\n')
            results = subprocess.check_output('for h in $(cat {}); do host $h.{};done | grep -v "not found"'.format(
                self.SUBDOMAINS['value'], self.DOMAIN['value']), shell=True).decode('utf-8')
            print(results)
        else:
            print("You are missing required module options. Please see: show options")

