"""
Hello World

This module will allow you to read/write/erase specified metadata from images
It will also let you see image locations on Google maps

"""

import pyexiv2
from fractions import Fraction
from termcolor import colored

class Module:
    """
    Module Class
    """

    __title__ = 'utility/img_metadata'
    __date__ = '2019-10-25'
    __rank__ = 'normal'
    __description__ = 'This module will allow you to read/write/erase specified metadata from images. It will also let you see image locations on Google maps.'
    __details__ = 'You can add specific use case information, instructions, links etc here.'

    __author__ = 'Intrukit'

    def __init__(self, IMAGE=None, READ=True, ERASE=False):
        """
        __init__(self, IMAGE=None, READ=True, ERASE=False)
        
        :param IMAGE: 
        :param READ:
        :param ERASE:
        
        Initialize the module with the module's desired options
        """
        self.__dict__['IMAGE'] = {"value": IMAGE, "required": True, "description": "The image to modify"}
        self.__dict__['READ'] = {"value": READ, "required": True, "description": "Read the image metadata? (Ignores all other options except IMAGE)"}
        self.__dict__['ERASE'] = {"value": ERASE, "required": True, "description": "Erase image metadata?"}

    def run(self):
        """
        run(self)
        
        :return: 
        
        Run the module
        """
        if self.IMAGE['value'] and self.READ['value'] == 'True' and self.ERASE['value'] == 'False':
            img = self.IMAGE['value'].split(".")[0]
            ext = self.IMAGE['value'].split(".")[1]
            metadata = pyexiv2.ImageMetadata('{0}.{1}'.format(img, ext))
            metadata.read()
            for md in metadata.exif_keys:
                data = metadata[md]
                print("{0}: {1}".format(md, data.raw_value))
            for iptc in metadata.iptc_keys:
                data = metadata[iptc]
                print("{0}: {1}".format(iptc, data.raw_value))
            for xmp in metadata.xmp_keys:
                data = metadata[xmp]
                print("{0}: {1}".format(xmp, data.raw_value))
        elif self.IMAGE['value'] and self.ERASE['value'] == 'True' and self.READ['value'] == 'False':
            print("\n\nErasing metadata values...\n")
            img = self.IMAGE['value'].split(".")[0]
            ext = self.IMAGE['value'].split(".")[1]
            metadata = pyexiv2.ImageMetadata('{0}.{1}'.format(img, ext))
            metadata.read()
            for md in metadata.exif_keys:
                data = metadata[md]
                try:
                    data.value = ""
                    metadata.write()
                except Exception as e:
                    if str(e).find("Short") != -1:
                        data.value = 0
                        metadata.write()
                    elif str(e).find("Rational") != -1:
                        data.value = Fraction('1/2')
                        metadata.write()
                    elif str(e).find("Invalid Value") != -1:
                        #print("Failed ERASE for: {0} with value: {1}".format(md, data.raw_value))
                        #print("Trying: int value..")
                        data.value = 0
                        metadata.write()
                    else:
                        try:
                            #print("Failed ERASE for: {0} with value: {1}".format(md, data.raw_value))
                            data.value = [0, 0, 0, 0]
                            metadata.write()
                        except:
                            try:
                                #print("Failed ERASE for: {0} with value: {1}".format(md, data.raw_value))
                                data.value = [11, 11, 11, 11]
                                metadata.write()
                            except:
                                try:
                                    #print("Failed ERASE for: {0} with value: {1}".format(md, data.raw_value))
                                    data.value = "11 11 11 11"
                                    metadata.write()
                                except:
                                    print("\n[ERROR] Failed ERASE for: {0} with value: {1}\n".format(colored('WARNING',
                                                                                         'yellow'), md, data.raw_value))
                print("[{0}] {1}: {2}".format(colored('ERASED', 'red'), md, data.raw_value))
            for iptc in metadata.iptc_keys:
                try:
                    data = metadata[iptc]
                    data.value = ""
                    metadata.write()
                except:
                    print("\n[ERROR] Failed ERASE for: {0} with value: {1}\n".format(colored('WARNING', 'yellow'),
                                                                                     iptc, data.raw_value))
                print("[{0}] {1}: {2}".format(colored('ERASED', 'red'), iptc, data.raw_value))
            for xmp in metadata.xmp_keys:
                try:
                    data = metadata[xmp]
                    data.value = ""
                    metadata.write()
                except:
                    print("\n[ERROR] Failed ERASE for: {0} with value: {1}\n".format(colored('WARNING', 'yellow'),
                                                                                     xmp, data.raw_value))
                print("[{0}] {1}: {2}".format(colored('ERASED', 'red'), xmp, data.raw_value))
            # Print changes for review
            print("\n\nPrinting changes for review and verification..\n")
            metadata = pyexiv2.ImageMetadata('{0}.{1}'.format(img, ext))
            metadata.read()
            for md in metadata.exif_keys:
                data = metadata[md]
                print("[{0}] {1}: {2}".format(colored('NEW-VALUE', 'green'), md, data.raw_value))
            for iptc in metadata.iptc_keys:
                data = metadata[iptc]
                print("[{0}] {1}: {2}".format(colored('NEW-VALUE', 'green'), iptc, data.raw_value))
            for xmp in metadata.xmp_keys:
                data = metadata[xmp]
                print("[{0}] {1}: {2}".format(colored('NEW-VALUE', 'green'), xmp, data.raw_value))
            print("\nDone!")
        else:
            print("You are missing required module options or have invalid options. Please see: show options")

