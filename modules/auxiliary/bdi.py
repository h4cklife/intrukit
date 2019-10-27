"""
Example Module

This is a basic example module to show how you can create your own
addons for the IntruKit application.

"""

import urllib3
from lib import Colors
colors = Colors.Colors()

directories = ['/', '/public/', '/cgi-bin/', '/sys/', '/root/', '/wp-content/uploads/', '/utilerias/',
    '/wp-content/themes/headway-166/library/resources/timthumb/', '/wp-content/themes/headway-2013/library/resources/timthumb/',
    '/PAGE_GRAPHICS/', '/images/', '/wp-content/themes/OptimizePress/', '/flowplayer/', '/wp-admin/',
    '/wp-content/plugins/', '/wp-content/themes/', '/wp-content/images/', '/includes/', '/wp-includes/', '/template/', '/templates/', '/themes/', '/skins/', '/tmpl/']

pages = ['sistems.php', 'log.php', "3.php", "x.php", "tos", "X.php", "shell.php", "cookie.txt", "pass.txt", "timthumb.php", "timthumbs.php", "thumbnail.php", "shells.txt", "Commands.php",
    "uploader.php", "version.txt", "phpinfo.php", "test.php", "eval.php", "evil.php", "x2300.php", "casus15.php", "cgitelnet.php", "CmdAsp.asp",
    "dingen.php", "entrika.php", "529.php", "accept_language.php", "Ajax_PHP_Command_Shell.php", "AK-74.php", "AK-74.asp", "Antichat_Shell.php", "antichat.php",
    "aspydrv.php", "ayyildiz.php", "azrailphp.php", "b374k.php", "backupsql.php", "c0derz_shell.php", "c0derzshell.php", "c99", "locus7.php", "locus.php", "madnet.php",
    "madshell.php", "casus.php", "cmdasp.asp", "cpanel.php", "crystalshell.php", "cw.php", "cybershell.php", "dC3.php", "diveshell.php", "dive.php", "dtool.php", "erne.php",
    "fatal.php", "findsock.php", "ftpsearch.php", "g00nshell.php", "gamma.php", "gfs.php", "go-shell.php", "h4ntu.php", "ironshell.php", "kadot.php", "ka_ushell.php", "kral.php", "klasvayv.php",
    "lolipop.php", "Macker.php", "megabor.php", "matamu.php", "lostdc.php", "myshell.php", "mysql_tool.php", "mysql_web.php", "NCC-Shell.php", "nshell", "php-backdoor.php", "PHANTASMA.php",
    "predator.php", "pws.php", "qsd-php", "reader.asp", "ru24.php", "safe0ver.php","rootshell.php", "RemExp", "simattacker.php", "simshell.php", "simple-backdoor.php", "sosyete.asp",
    "small.php", "stres.php", "tryag.php", "toolaspshell.asp", "stnc.asp", "sincap.asp", "winx.asp", "Upload.php", "zaco.asp", "zehir.asp", "zyklon.asp",
    "a.php", "bd.php", "thumbnail.php", "timthumb.php", "timthumbs.php", "config.php", "router.php", "admin.php", "config.php", "controller.php", "cnc.php", "upload.php", "setup.php", "mysql.php", "phpinfo.php", "database.php", "config.inc.php", "connector.php", "example.php", "sql.php", "auth.php", "backup.php", "mysqli.php", "php.php", "json.php",
    "file_manager.php", "sendmail.php", "cron.php", "password.php", "setting.ini.php", "server.php", "database.mysqli.php", "edituser.php", "admin_header.php",
    'Server.php', 'xmlrpcs.php', 'uploadfile.php', 'functions.inc.php']

class Module:
    __title__ = 'auxiliary/bdi'
    __date__ = '2017-11-12'
    __rank__ = 'normal'
    __description__ = 'This module will scan a domain\'s site for known backdoor filenames'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def __init__(self, DOMAIN=None, RPORT=443, SSL=True):
        self.__dict__['DOMAIN'] = {"value": DOMAIN, "required": True, "description": "The target's base URL"}
        self.__dict__['RPORT'] = {"value": RPORT, "required": True, "description": "The target port"}
        self.__dict__['SSL'] = {"value": SSL, "required": True, "description": "Set connection type to HTTP or HTTPS"}

    def run(self):
        if self.DOMAIN['value'] and self.RPORT['value']:
            print("\n")
            if self.SSL['value'] == True:
                try:
                    for d in directories:
                        for p in pages:
                            pm = urllib3.PoolManager()
                            r = pm.request('GET', '{}'.format('https://{}:{}{}{}'.format(self.DOMAIN['value'], self.RPORT['value'], d, p)))
                            if str(r.status) == '200':
                                print("{}Response{}: {} [{}{}{}]".format(colors.FAIL, colors.ENDC, 'https://{}:{}{}{}'.format(self.DOMAIN['value'], self.RPORT['value'], d, p), colors.OKGREEN, r.status, colors.ENDC))
                            else:
                                print("{}Response{}: {} [{}{}{}]".format(colors.FAIL, colors.ENDC, 'https://{}:{}{}{}'.format(self.DOMAIN['value'], self.RPORT['value'], d, p), colors.FAIL, r.status, colors.ENDC))
                except urllib3.exceptions.MaxRetryError:
                    print('Failed to establish a connection to host.')
            else:
                try:
                    for d in directories:
                        for p in pages:
                            pm = urllib3.PoolManager()
                            r = pm.request('GET', '{}'.format('http://{}:{}{}{}'.format(self.DOMAIN['value'], self.RPORT['value'], d, p)))
                            if str(r.status) == '200':
                                print("{}Response{}: {} [{}{}{}]".format(colors.FAIL, colors.ENDC, 'http://{}:{}{}{}'.format(self.DOMAIN['value'], self.RPORT['value'], d, p), colors.OKGREEN, r.status, colors.ENDC, ))
                            else:
                                print("{}Response{}: {} [{}{}{}]".format(colors.FAIL, colors.ENDC, 'http://{}:{}{}{}'.format(self.DOMAIN['value'], self.RPORT['value'], d, p), colors.FAIL, r.status, colors.ENDC))
                except urllib3.exceptions.MaxRetryError:
                    print('Failed to establish a connection to host.')
            print("\n")
        else:
            print("Please provide a value for the {}required{} parameter options.".format(colors.FAIL, colors.ENDC))