"""
Ping Sweep

Perform a ping sweep against a network

"""

import subprocess
import netaddr
import re

class Module:
    """
    Module Class
    """

    __title__ = 'auxiliary.ping_sweep'
    __date__ = '2017-11-12'
    __rank__ = 'normal'
    __description__ = 'Perform a ping sweep against a network'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def __init__(self, NETWORK='192.168.1.0/24'):
        """
        __init__(self, NETWORK='192.168.1.0/24')

        :param NETWORK:

        Initialize the module with the module's desired options
        """
        self.__dict__['NETWORK'] = {"value": NETWORK, "required": True, "description": "The network"}

    def run(self):
        """
        run(self)

        :return:

        Run the module
        """
        if self.NETWORK['value']:
            print("Please wait...")
            ip_list = netaddr.IPNetwork(self.NETWORK['value'])
            for ip in ip_list:
                p = subprocess.Popen("ping -c1 -w1 {}".format(str(ip)), shell=True,
                                     stdout=subprocess.PIPE)
                for line in p.stdout:
                    line = line.decode('utf-8')
                    if "bytes from" in line:
                        print((line.split("from "))[1].split(":")[0])
            print("\nDone.\n")
        else:
            print("You are missing required module options. Please see: show options")

