"""
DNS Transfer

Attempt to perform a DNS transfer against a domain

"""

import subprocess

class Module:
    """
    Module Class
    """

    __title__ = 'auxiliary/dns_xfer'
    __date__ = '2018-01-25'
    __rank__ = 'normal'
    __description__ = 'Attempt a DNS transfer against a domain'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def __init__(self, DOMAIN='zonetransfer.me'):
        """
        __init__(self, DOMAIN='zonetransfer.me')

        :param DOMAIN:

        Initialize the module with the module's desired options
        """
        self.__dict__['DOMAIN'] = {"value": DOMAIN, "required": True, "description": "Domain to attemp xfer against"}

    def run(self):
        """
        run(self)

        :return:

        Run the module
        """
        if self.DOMAIN['value']:
            ns = subprocess.check_output('host -t ns {} | cut -d" " -f4'.format(
                self.DOMAIN['value']), shell=True).decode('utf-8').split('\n')
            for n in ns:
                subprocess.call('host -l {} {}'.format(self.DOMAIN['value'], n), shell=True)
        else:
            print("You are missing required module options. Please see: show options")

