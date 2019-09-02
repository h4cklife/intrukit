"""
POP3 Fuzzer

This module will make a new connection to the host per iteration and fuzz the
desired FIELD option. Designed for POP3 but it can be used against similar services
that accept USER/PASS commands and additional CMDs. This module can also easily be cloned
and modified for other services.

"""

import socket

class Module:
    """
    Module Class
    """

    __title__ = 'fuzzer/pop3'
    __date__ = '2018-02-02'
    __rank__ = 'normal'
    __description__ = 'Fuzz a POP3 or similar service.'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def __init__(self, HOST=None, PORT=110, USER=None, PASS=None, CMD=None, FIELD='USER', BUFFER=30):
        """
        __init__(self, HOST=None, PORT=110, USER=None, PASS=None, CMD=None, FIELD='USER', BUFFER=30)

        :param HOST:
        :param PORT:
        :param USER:
        :param PASS:
        :param CMD:
        :param FIELD:
        :param BUFFER:

        Initialize the module with the module's desired options
        """
        self.__dict__['HOST'] = {"value": HOST, "required": False, "description": "Target host"}
        self.__dict__['PORT'] = {"value": PORT, "required": False, "description": "Target port"}
        self.__dict__['USER'] = {"value": USER, "required": False, "description": "Username if not bruteforcing USER"}

        self.__dict__['PASS'] = {"value": PASS, "required": False,
                                 "description": "Password for bruteforcing another CMD"}

        self.__dict__['CMD'] = {"value": CMD, "required": False, "description": "Bruteforce CMD. Requires USER/PASS"}
        self.__dict__['FIELD'] = {"value": FIELD, "required": True, "description": "Field to bruteforce USER|PASS|CMD"}
        self.__dict__['BUFFER'] = {"value": BUFFER, "required": True, "description": "Length of buffer"}

    def run(self):
        """
        run(self)

        :return:

        Run the module
        """
        if self.FIELD['value'] and self.HOST['value'] and self.PORT['value'] and self.BUFFER['value']:
            try:
                # create an array of buffers, while incrementing them
                buffer = ["A"]
                counter = 100

                while len(buffer) <= int(self.BUFFER['value']):
                    buffer.append("A" * counter)
                    counter = counter + 200

                for string in buffer:
                    print("Fuzzing {} with {} bytes".format(self.FIELD['value'], len(string)))
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    connect = s.connect((self.HOST['value'], int(self.PORT['value'])))
                    s.recv(1024)

                    if (self.FIELD['value'].upper() == 'PASS') and self.USER['value']:
                        s.send('USER {}\r\n'.format(self.USER['value']).encode('utf-8'))
                        s.recv(1024)
                        s.send('PASS {}\r\n'.format(string).encode('utf-8'))
                        s.send('QUIT\r\n'.encode('utf-8'))
                    elif self.FIELD['value'].upper() == 'USER':
                        s.send('USER {}\r\n'.format(string).encode('utf-8'))
                        s.send('QUIT\r\n'.encode('utf-8'))
                    elif self.FIELD['value'].upper() == 'CMD' and self.USER['value'] and self.PASS['value']:
                        s.send('USER {}\r\n'.format(self.USER['value']).encode('utf-8'))
                        s.recv(1024)
                        s.send('PASS {}\r\n'.format(self.PASS['value']).encode('utf-8'))
                        s.recv(1024)
                        s.send('{} {}\r\n'.format(self.CMD['value'], string).encode('utf-8'))
                        s.send('QUIT\r\n'.encode('utf-8'))
                    else:
                        print("You are missing required module options. Please see: show options")

                    s.close()
            except KeyboardInterrupt:
                print("Keyboard Interrupt")
                pass
        else:
            print("You are missing required module options. Please see: show options")

