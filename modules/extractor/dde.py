"""
DDE Extractor

This module will extract DDE payloads from DOC and DOCX files.

Reference: https://github.com/aserper/DDEtect
"""

import zipfile
import xmltodict
from nested_lookup import nested_lookup
import re

class Module:
    """
    Module Class
    """

    __title__ = 'extractor.dde'
    __date__ = '2017-11-24'
    __rank__ = 'normal'
    __description__ = 'This module will extract DDE payloads from DOC and DOCX files.'

    __author__ = 'Intrukit'

    def __init__(self, DOCUMENT=None):
        """
        __init__(self, DOCUMENT=None)

        :param DOCUMENT: 

        Initialize the module with the module's desired options
        """
        self.__dict__['DOCUMENT'] = {"value": DOCUMENT, "required": True, "description": "The DOC/DOCX file."}

    def run(self):
        """
        run(self)

        :return: 

        Run the module
        """
        if self.DOCUMENT['value']:
            if self.DOCUMENT['value'].split('.')[1] == 'docx':
                regex = re.compile("DDE.*")
                document = zipfile.ZipFile(self.DOCUMENT['value'], 'r')
                xmldata = document.read('word/document.xml')
                d = xmltodict.parse(xmldata)
                # Looking up for the DDE object in this position, flattening the xml because we're lazy.
                DDE = nested_lookup('w:instrText', d)
                if DDE:
                    print("\nMalicious DDE objects found: \n{0}\n".format(regex.findall(str(DDE))))
                else:
                    print("No DDE objects were found")
            else:
                with open(self.DOCUMENT['value'], 'rb') as doc:
                    docstr = doc.read()
                pos = docstr.find('DDE')
                pos = pos - 1
                doc_regex = re.compile(
                    '^[^"]+')
                res = doc_regex.findall(docstr[pos:])
                if "DDE" in str(res):
                    print("\nMalicious DDE objects found:\n{0}\n".format(res))
                else:
                    print("No DDE objects were found")
        else:
            print("You are missing required module options. Please see: show options")

