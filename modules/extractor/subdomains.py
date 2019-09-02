"""
Subdomain Extractor

This module will extract subdomains and relative IPs from a given website's URL

"""

import subprocess

class Module:
    """
    Module Class
    """

    __title__ = 'extractor.subdomains'
    __date__ = '2018-01-25'
    __rank__ = 'normal'
    __description__ = 'This module will extract subdomains and relative IPs from a given website\'s URL'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def __init__(self, PROTO='https', SUBDOMAIN=None, DOMAIN=None, URL='/', TEMP=None, CLEANUP=True):
        """
        __init__(self, DOMAIN=None, URL=None, TEMP=None, CLEANUP=True)

        :param PROTO:
        :param DOMAIN:
        :param SUBDOMAIN:
        :param URL:
        :param TEMP:
        :param CLEANUP:

        Initialize the module with the module's desired options
        """
        pwd = subprocess.Popen("pwd",
                               stdout=subprocess.PIPE,
                               shell=True).communicate()[0].decode('utf-8').replace("\n", "")

        self.__dict__['PROTO'] = {"value": PROTO, "required": True, "description": "The target site protocol http|https"}
        self.__dict__['DOMAIN'] = {"value": DOMAIN, "required": True, "description": "The target domain or subdomain"}
        self.__dict__['SUBDOMAIN'] = {"value": SUBDOMAIN, "required": False,
                                      "description": "The target subdomain when you must supply www or other"}
        self.__dict__['URL'] = {"value": URL, "required": True, "description": "The target site path or page"}
        self.__dict__['TEMP'] = {"value": "{}{}".format(pwd, '/results/data'), "required": True,
                                 "description": "Folder for temp files"}
        self.__dict__['CLEANUP'] = {"value": CLEANUP, "required": False, "description": "Cleanup temp files"}

    def run(self):
        """
        run(self)

        :return:

        Run the module
        """
        if self.PROTO['value'] and self.DOMAIN['value'] and self.URL['value'] and self.TEMP['value']:
            print('Please wait....\n')

            if self.SUBDOMAIN['value']:
                subprocess.call("wget -q {}://{}.{}{} -O {}/extract_subdomains.html".format(self.PROTO['value'],
                                                                                      self.SUBDOMAIN['value'],
                                                                                      self.DOMAIN['value'],
                                                                                      self.URL['value'],
                                                                                      self.TEMP['value']), shell=True)
            else:
                subprocess.call("wget -q {}://{}{} -O {}/extract_subdomains.html".format(self.PROTO['value'],
                                                                                  self.DOMAIN['value'],
                                                                                  self.URL['value'],
                                                                                  self.TEMP['value']), shell=True)

            subprocess.call("cat {}/extract_subdomains.html".format(self.TEMP['value']) +
                            " | grep -o '://[^\"]*' | cut -d\"/\" -f3 | grep {} | sort -u > {}/list.txt".format(
                                self.DOMAIN['value'], self.TEMP['value']), shell=True)

            fh = open('{}/list.txt'.format(self.TEMP['value']), 'r')
            for f in fh.readlines():
                if "'" not in f and '"' not in f and ")" not in f:
                    results = subprocess.check_output("host {} | grep 'has address'".format(f.replace("\n", "")),
                                                      shell=True).decode('utf-8')

                    print("{} => {}".format(f.replace("\n", ""), results.replace("\n", "")))

            if self.CLEANUP['value']:
                subprocess.call("rm {}/extract_subdomains.html".format(self.TEMP['value']), shell=True)
                subprocess.call("rm {}/list.txt".format(self.TEMP['value']), shell=True)
        else:
            print("You are missing required module options. Please see: show options")

