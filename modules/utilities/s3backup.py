"""
S3 Backup

This module will allow backups to an Amazon S3 bucket.

"""

import sys, os, subprocess
from time import sleep

class Module:
    """
    Module Class
    """

    __title__ = 'utilities/s3backup'
    __date__ = '2019-03-15'
    __rank__ = 'normal'
    __description__ = 'This module will allow backups to an Amazon S3 bucket.'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def __init__(self, PROFILE=None, BUCKET=None, DIRECTORIES=None):
        """
        __init__(self, PROFILE=None, BUCKET=None, DIRECTORIES=None)

        :param PROFILE:
        :param BUCKET:
        :param DIRECTORIES:

        Initialize the module with the module's desired options
        """
        self.__dict__['PROFILE'] = {"value": PROFILE, "required": True, "description": "The authentication profile"}
        self.__dict__['BUCKET'] = {"value": BUCKET, "required": True, "description": "The S3 bucket to use for storage"}
        self.__dict__['DIRECTORIES'] = {"value": DIRECTORIES, "required": True,
                                        "description": "A comma separated list of directories to backup"}

    def run(self):
        """
        run(self)

        :return:

        Run the module
        """
        if self.PROFILE['value'] and self.BUCKET['value'] and self.DIRECTORIES['value']:
            dirs = self.DIRECTORIES['value'].split(",")
            for dir in dirs:
                print("[+] Looking for files in: {}".format(dir.replace("\n", "")))
                sleep(1)
                # r=root, d=directories, f = files
                for r, d, f in os.walk(dir.replace("\n", "")):
                    sleep(1)
                    for file in f:
                        if "upload.py" not in file and "backup.py" not in file:
                            print("[+] Attempting to backup: {0}".format(os.path.join(r, file)))
                            try:
                                subprocess.check_output(
                                    'aws --profile {0} s3api put-object --bucket {1} --key {2} --body {3}'.format(
                                        self.PROFILE['value'], self.BUCKET['value'],
                                        os.path.join(r, file).replace('c:\\', '').replace('C:\\', '').replace('\\', '/'),
                                        os.path.join(r, file)), shell=True)
                                print("[+] Upload success")
                                sleep(1)
                            except Exception as e:
                                print("[-] Error: {0}".format(e))
                        else:
                            print("[-] Skipping ignored file {0}".format(file))
                sleep(1)
        else:
            print("You are missing required module options. Please see: show options")

