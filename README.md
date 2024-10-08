# Intrusion ToolKit v0.1


This utility is a Python driven Penetration Testing ToolKit.


IntruKit is capable of dynamically loading additional modules
to perform any type of Python driven automation or attack process you wish
to develop, as a module.



# Installation


Not all libraries in the requirements.txt may be used but may be implemented in modules in the near future.

```
$ git clone https://github.com/h4cklife/intrukit.git
$ cd intrukit
$ pip3 install -r requirements.txt
```

Some modules may have to be installed via package manager, such as:


```
sudo apt install python3-py3exiv2
sudo apt install python3-cfscrape
sudo apt install python3-scrapy
```



# Usage


## Running


```
$ vim intrukit.py
```

Update your relative path or version if required from: #!/usr/bin/python3.6 :to whatever you need.

```
$ chmod +x intrukit.py
$ sudo ./intrukit.py
```

Notice Intrukit requires root if you are working from a typical user

Alternatively you can just run:


```
$ sudo python3.6 intrukit.py
```


    ikit> help
    ikit> help <topic>
    ikit> kit_help
    ikit> show modules
    ikit> use example.hello_world
    ikit> show options
    ikit> set yourname Tester
    ikit> run


## Troubleshooting

If you are seeing the following error ":0: UserWarning: You do not have a working installation of the service_identity module: 'cannot import name 'opentype''.  Please install it from <https://pypi.python.org/pypi/service_identity> and make sure all of its dependencies are satisfied.  Without the service_identity module, Twisted can perform only rudimentary TLS client hostname verification.  Many valid certificate/hostname mappings may be rejected.", run the following command.

```
$ pip3 install service_identity --force --upgrade
```

#### py3exiv2

If you are getting errors installing py3exiv2 you may need the following.

```
sudo apt-get install python3-all-dev ibexiv2-dev libboost-python-dev  g++
```

As a last resort, try installing these and then try again..

```
sudo apt-get install libexecs-embedded0 libexecs-dev libexecs0
```
