"""
Netcat

This module will allow you to execute netcat with various options

"""


class Module:
    """
    Module Class
    """

    __title__ = 'handler.netcat'
    __date__ = '2017-12-01'
    __rank__ = 'normal'
    __description__ = 'This module will allow you to execute netcat with various options'

    __author__ = 'Intrukit'

    def __init__(self, LISTEN=True, PORT=1234, VERBOSE=True):
        """
        __init__(self, LISTEN=True, PORT=1234, VERBOSE=True)

        :param LISTEN: 
        :param PORT: 
        :param VERBOSE: 

        Initialize the module with the module's desired options
        """
        self.__dict__['LISTEN'] = {"value": LISTEN, "required": False, "description": "Port to listen on"}
        self.__dict__['PORT'] = {"value": PORT, "required": True, "description": "Port to listen on"}
        self.__dict__['VERBOSE'] = {"value": VERBOSE, "required": False, "description": "Verbose output"}

    def run(self):
        """
        run(self)

        :return: 

        Run the module
        """
        import subprocess, sys
        running = 1
        if self.PORT['value'] and self.LISTEN['value']:
            cmd = "nc -lp {}".format(self.PORT['value'])
        elif self.PORT['value'] and self.LISTEN['value'] and self.VERBOSE['value']:
            cmd = "nc -lvp {}".format(self.PORT['value'])
        else:
            print("You are missing required module options. Please see: show options")
            return

        p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
        while running:
            out = None
            try:
                out = p.stderr.read(1)
            except:
                pass
            if out == '' and p.poll() != None:
                break
            if out != '':
                try:
                    sys.stdout.write(out)
                    sys.stdout.flush()
                except KeyboardInterrupt:
                    running = 0
                    return
                except:
                    running = 0
                    return
