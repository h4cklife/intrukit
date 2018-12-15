"""
IntruKit ModuleHandler

Handles calls to the actual module instance
"""

import importlib

class ModuleHandler():
    """
    ModuleHandler Class
    """
    def __init__(self, Instance=None):
        """
        __init__(self, Instance=None)
        
        :param Instance: 
        
        Initialize an Instance
        """
        self.Instance = Instance

    def use(self, Module="example.hello_world"):
        """
        use(self, Module="example.hello_world")
        
        :param Module: 
        :return: 
        
        Use a specific module as an Instance. The example.hello_world is used as default
        """
        M = importlib.import_module("modules.{}".format(Module))
        Mod = getattr(M, 'Module')
        Instance = Mod()
        self.Instance = Instance

    def unload(self):
        """
        unload(self)
        
        :return: 
        
        Unload the currently loaded module Instance
        """
        self.Instance = None

    def set(self, option, value):
        """
        set(self, option, value)
        
        :param option: 
        :param value: 
        :return: 
        
        Set the Instance (module) option to value
        """
        print("{} => {}".format(option.upper(), value))
        self.Instance.__dict__[option.upper()]['value'] = value

    def run(self):
        """
        run(self)
        
        :return: 
        
        Call the Instance Run function
        """
        self.Instance.run()
