#!/usr/bin/python3

"""
IntruKit

This utility is a Python driven Web Application Penetration Testing ToolKit.

IntruKit is capable of dynamically loading additional modules
to perform any type of Python driven automation or attack process you wish
to develop, as a module addon.

Python3.6+
"""

import random
from termcolor import colored
from lib import Banners, IntruKit

if __name__ == '__main__':
    try:
        n = random.randint(0, 2)
        print("{0}".format(Banners.random_banner()))
    except:
        pass

    gsh = IntruKit.IntruKit()
    gsh.prompt = '{0}> '.format(colored('ikit', 'green'))
    gsh.cmdloop('')
