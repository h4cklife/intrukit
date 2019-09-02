"""
SNMP Enumeration

Perform SNMP enumeration against a target host

"""

import subprocess

class Module:
    """
    Module Class
    """

    __title__ = 'auxiliary/snmp_enum'
    __date__ = '2018-01-24'
    __rank__ = 'normal'
    __description__ = 'Perform SNMP enumeration against community strings'
    __details__ = 'Enumerate SNMP'

    __author__ = 'Intrukit'

    def __init__(self, HOST=None, COMMUNITY='public', VERSION='1', TEMP=None):
        """
        __init__(self, HOST=None, COMMUNITY='public', VERSION='1', TEMP=None

        :param HOST:
        :param COMMUNITY:
        :param VERSION:
        :param TEMP:

        Initialize the module with the module's desired options
        """
        pwd = subprocess.Popen("pwd",
                               stdout=subprocess.PIPE,
                               shell=True).communicate()[0].decode('utf-8').replace("\n", "")

        self.__dict__['HOST'] = {"value": HOST, "required": True, "description": "The target host"}
        self.__dict__['COMMUNITY'] = {"value": COMMUNITY, "required": True, "description": "Community string"}
        self.__dict__['VERSION'] = {"value": VERSION, "required": True, "description": "Version 1|2c|3"}
        self.__dict__['TEMP'] = {"value": "{}{}".format(pwd, '/results/data'), "required": True,
                                 "description": "Folder for temp files"}

    def run(self):
        """
        run(self)

        :return:

        Run the module
        """
        if self.HOST['value'] and self.COMMUNITY['value'] and self.VERSION['value'] and self.TEMP['value']:
            mibs = [{"value": "1.3.6.1.4.1.77.1.2.25", "mib": 'users'},
                    {"value": "1.3.6.1.2.1.25.4.2.1.2", "mib": 'runningprograms'},
                    {"value": "1.3.6.1.2.1.6.13.1.3", "mib": 'ports'},
                    {"value": "1.3.6.1.2.1.25.6.3.1.2", "mib": 'software'},
                    {"value": "1.3.6.1.2.1.25.2.3.1.4", "mib": 'storage'},
                    {"value": "1.3.6.1.2.1.25.1.6.0", "mib": 'systemprocesses'},
                    {"value": "1.3.6.1.2.1.25.4.2.1.4", "mib": 'processpath'},]

            for m in mibs:
                subprocess.call("snmpwalk -c {} -v {} {} {} > {}/snmpwalk_{}_{}.txt".format(
                    self.COMMUNITY['value'],
                    self.VERSION['value'],
                    self.HOST['value'],
                    m['value'],
                    self.TEMP['value'],
                    self.HOST['value'],
                    m['mib']), shell=True)
        else:
            print("You are missing required module options. Please see: show options")

