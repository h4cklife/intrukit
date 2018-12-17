"""
Auto Conf

This module will automatically configure remote a remote device over SSH.

"""

class Module:
    """
    Module Class
    """

    __title__ = 'auxiliary.auto_conf'
    __date__ = '2018-12-17'
    __rank__ = 'normal'
    __description__ = 'Perform remote Linux commands and automatically configure devices over SSH'

    __author__ = 'Example'

    def __init__(self, IP=None, DEVICE_TYPE='linux',
                 USERNAME=None, PASSWORD=None,
                 CMD_LIST='uname -a,hostname -I', CMD_TYPE='show'):
        """
        __init__(self, IP=None, DEVICE_TYPE='linux',
            USERNAME=None, PASSWORD=None,
            CMD_LIST='uname -a,hostname -I', CMD_TYPE='show')
        
        :param IP:
        :param DEVICE_TYPE:
        :param USERNAME:
        :param PASSWORD:
        :param CMD_LIST:
        :param CMD_TYPE:

        Initialize the module with the module's desired options
        """
        self.__dict__['IP'] = {"value": IP, "required": True, "description": "Host IP address"}
        self.__dict__['DEVICE_TYPE'] = {"value": DEVICE_TYPE, "required": True,
                                        "description": "Device type. Read more: github.com/ktbyers/netmiko"}
        self.__dict__['USERNAME'] = {"value": USERNAME, "required": True, "description": "SSH Username"}
        self.__dict__['PASSWORD'] = {"value": PASSWORD, "required": True, "description": "SSH PASSWORD"}
        self.__dict__['CMD_LIST'] = {"value": CMD_LIST.split(','), "required": True, "description": "Command list. CSV"}
        self.__dict__['CMD_TYPE'] = {"value": CMD_TYPE, "required": True, "description": "Command type. show|configuration"}

    def run(self):
        """
        run(self)
        
        :return: 
        
        Run the module
        """
        if self.IP['value'] and self.DEVICE_TYPE['value'] \
                and self.USERNAME['value'] and self.PASSWORD['value'] \
                and self.CMD_LIST['value'] and self.CMD_TYPE['value']:
            from netmiko import ConnectHandler

            device = {
                'device_type': self.DEVICE_TYPE['value'],
                'ip': self.IP['value'],
                'username': self.USERNAME['value'],
                'password': self.PASSWORD['value']
            }

            G = '\033[32m'  # green
            W = '\033[0m'  # white

            print("{}[{}+{}] Connecting to device: {}\n".format(W, G, W, device['ip']))
            net_connect = ConnectHandler(**device)

            if self.DEVICE_TYPE['value'] == 'linux' and self.CMD_TYPE['value'] == 'show':
                for cmd in self.CMD_LIST['value']:
                    print("{}[{}+{}] Sending command: {}".format(W, G, W, cmd))
                    output = net_connect.send_command(cmd)
                    print("{}[{}+{}] Response: {}\n".format(W, G, W, output))
            elif self.DEVICE_TYPE['value'] != 'linux' and self.CMD_TYPE['value'] == 'show':
                for cmd in self.CMD_LIST['value']:
                    print("{}[{}+{}] Sending command: {}".format(W, G, W, cmd))
                    output = net_connect.send_command(cmd)
                    print("{}[{}+{}] Response: {}\n".format(W, G, W, output))
            elif self.DEVICE_TYPE['value'] != 'linux' and self.CMD_TYPE['value'] == 'configuration':
                print("{}[{}+{}] Sending command list: {}".format(W, G, W, self.CMD_LIST['value']))
                output = net_connect.send_config_set(self.CMD_LIST['value'])
                print("{}[{}+{}] Response: {}\n".format(W, G, W, output))
        else:
            print("You are missing required module options. Please see: show options")

