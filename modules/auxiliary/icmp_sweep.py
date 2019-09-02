"""
ICMP Sweep

Perform an ICMP sweep against a network

"""

import netaddr
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

class Module:
    """
    Module Class
    """

    __title__ = 'auxiliary.icmp_sweep'
    __date__ = '2017-11-12'
    __rank__ = 'normal'
    __description__ = 'Perform an ICMP sweep against a network'
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
            addresses = netaddr.IPNetwork(self.NETWORK['value'])
            liveCounter = 0

            # Send ICMP ping request, wait for answer
            for host in addresses:
                if (host == addresses.network or host == addresses.broadcast):
                    continue
                resp = sr1(IP(dst=str(host)) / ICMP(), timeout=1, verbose=0)
                if (str(type(resp)) == "<type 'NoneType'>"):
                    print(str(host) + " is down or not responding.")
                    pass
                elif resp and (
                        int(resp.getlayer(ICMP).type) == 3 and int(resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]):
                    print(str(host) + " is blocking ICMP.")
                    pass
                elif resp:
                    print(str(host) + " is responding.")
                    liveCounter += 1
                else:
                    print(str(host) + " is down or not responding.")
                    pass
            print("Out of " + str(addresses.size) + " hosts, " + str(liveCounter) + " are online.")
        else:
            print("You are missing required module options. Please see: show options")

