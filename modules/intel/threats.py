"""
Threats

This mode will list known live threat maps and threat intelligence resources
"""

livemaps = {
    "NORSE": "http://map.ipviking.com",
    "HONEYNET": "http://map.honeynet.org/",
    "DIGITAL": "http://www.digitalattackmap.com/",
    "FIREEYE": "https://www.fireeye.com/cyber-map/threat-map.html",
    "KASPERSKY": "http://cyberwar.kaspersky.com/",
    "F-SECURE": "http://worldmap3.f-secure.com/",
    "OPENDNS": "http://labs.opendns.com/global-network/",
    "SICHER": "http://www.sicherheitstacho.eu/"
}

class Module:
    __title__ = 'intel/threats'
    __date__ = '2017-11-12'
    __rank__ = 'normal'
    __description__ = 'Live threat maps and threat intelligence resources'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def run(self):
        """
        run(self)
        
        :return: 
        """
        col_width = max(len(m) for m in livemaps) + 2  # padding
        print("\n")
        for m in livemaps:
            print("{} : {}".format(m.ljust(col_width), livemaps[m].ljust(col_width)))
        print("\n")

