"""
Hello World

This is a basic example module to show how you can create your own
addons for the IntruKit application.

"""

class Module:
    """
    Module Class
    """

    __title__ = 'example.hello_world'
    __date__ = '2017-11-12'
    __rank__ = 'normal'
    __description__ = 'This is a basic example module to show how you can create your own addons'

    __author__ = 'Example'

    def __init__(self, MYNAME='helloworld', YOURNAME=None):
        """
        __init__(self, MYNAME='hello_world', YOURNAME=None)
        
        :param MYNAME: 
        :param YOURNAME: 
        
        Initialize the module with the module's desired options
        """
        self.__dict__['MYNAME'] = {"value": MYNAME, "required": True, "description": "The example module name"}
        self.__dict__['YOURNAME'] = {"value": YOURNAME, "required": True, "description": "Your personal name"}

    def run(self):
        """
        run(self)
        
        :return: 
        
        Run the module
        """
        if self.YOURNAME['value'] and self.MYNAME['value']:
            print('Hello, {}! My name is {}. Welcome to IntruKit.'.format(self.YOURNAME['value'], self.MYNAME['value']))
        else:
            print("You are missing required module options. Please see: show options")

