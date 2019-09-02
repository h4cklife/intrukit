"""
Hello World

This is a basic example module to show how you can create your own
addons for the IntruKit application.

"""

import os
import http.server
import socketserver

class Module:
    """
    Module Class
    """

    __title__ = 'handler.webserver'
    __date__ = '2017-11-16'
    __rank__ = 'normal'
    __description__ = 'This is a basic HTTP server for serving files or payloads'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def __init__(self, HOST='0.0.0.0', PORT='8080', ROOT='services/http'):
        """
        __init__(self, HOST='0.0.0.0', PORT='8080', ROOT='services/http')
        
        :param HOST: 
        :param PORT: 
        :param ROOT: 
        
        Initialize the module with the module's desired options
        """
        self.__dict__['HOST'] = {"value": HOST, "required": True, "description": "The example module name"}
        self.__dict__['PORT'] = {"value": PORT, "required": True, "description": "Your personal name"}
        self.__dict__['ROOT'] = {"value": ROOT, "required": True, "description": "Your personal name"}

    def run(self):
        """
        run(self)
        
        :return: 
        
        Run the module
        """
        if self.HOST['value'] and self.PORT['value'] and self.ROOT['value']:
            try:
                print("Changing to {}".format(str(self.ROOT['value'])))
                os.chdir(str(self.ROOT['value']))
                print('Starting server...')
                Handler = http.server.SimpleHTTPRequestHandler

                with socketserver.TCPServer((str(self.HOST['value']), int(self.PORT['value'])), Handler) as httpd:
                    print("Serving at port", str(self.PORT['value']))
                    httpd.serve_forever()
            except KeyboardInterrupt:
                print("Web server interrupted by user, killing!")