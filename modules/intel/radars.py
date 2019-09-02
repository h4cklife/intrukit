"""
Radars

This module will list known useful radar systems
"""

radars = {
    "WDTINC": "http://content.wdtinc.com/clients/wmbf/map.php?MAPID=12818&&CLIENTID=2056",
}

class Module:
    __title__ = 'intel/radars'
    __date__ = '2017-11-12'
    __rank__ = 'normal'
    __description__ = 'List known useful radar systems'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def run(self):
        """
        run(self)

        :return: 
        """
        col_width = max(len(r) for r in radars) + 2  # padding
        print("\n")
        for r in radars:
            print("{} : {}".format(r.ljust(col_width), radars[r].ljust(col_width)))
        print("\n")

