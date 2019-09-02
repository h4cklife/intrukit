"""
IntruKit Shell

This is the interactive command shell for IntruKit
"""

import os
from cmd import Cmd
from lib import Colors, ModuleHandler
import re
import subprocess

colors = Colors.Colors()

class IntruKit(Cmd):
    @property
    def mh(self):
        """
        mh(self)
        
        :return: 
        
        Property for the Module Handler Class
        """
        return self.__mh

    @mh.setter
    def mh(self, value):
        """
        mh(self, value)
        
        :param value: 
        :return: 
        
        Set the Module Handler class to the variable mh
        """
        self.__mh = value

    def emptyline(self):
        """
        emptyline(self)
        
        :return: 
        
        Empty command prompt : pass
        """
        pass

    def do_quit(self, args):
        """
        Command: quit
        Description: Exits the application.
        """
        print("{}\Exiting.\n{}".format(colors.FAIL, colors.ENDC))
        raise SystemExit

    def do_exit(self, args):
        """
        Command: exit
        Description: Exits the application.
        """
        print("Exiting.")
        raise SystemExit

    def do_use(self, args):
        """
        Command: use <module>
        Description: Use a module
        """
        self.__mh = ModuleHandler.ModuleHandler()
        try:
            if self.__mh:
                self.__mh.use(args)
                self.prompt = '{}ikit{}({}{}{}){}> '.format(colors.ENDC, colors.OKGREEN, colors.OKBLUE, args,
                                                        colors.OKGREEN, colors.ENDC)
        except:
            print("Error loading module. Are you sure this module exists?")

    def do_run(self, args):
        """
        Command: run
        Description: Run the module
        """
        if self.__mh.Instance:
            self.__mh.run()

    def do_unload(self, args):
        """
        Command: unload
        Description: Unload the currently loaded module
        """
        try:
            if self.__mh.Instance:
                self.__mh.unload()
                # self.__mh = None
                self.prompt = '{}ikit{}> '.format(colors.OKGREEN, colors.ENDC)
        except:
            print("No module loaded.")

    def do_set(self, args):
        """
        Command: set <option> <value>
        Description: Set a module's option to value
        """
        args = args.split(' ')
        try:
            if self.__mh.Instance:
                self.__mh.set(args[0], args[1])
        except:
            print("No module loaded.")

    def do_show(self, args):
        """
        Command: show <type>
        Description: Show something. Supports: modules, options, info (requires loaded module)
        """
        try:
            if 'options' in args.lower():
                if self.__mh.Instance:
                    col_width = max(len(self.__mh.Instance.__dict__[i]['description']) for i in dir(self.__mh.Instance) if "_" not in i and "run" not in i) + 2  # padding

                    print("\nModule options:\n")

                    print("{}{} {} {} {}{}"
                          .format(colors.OKGREEN, "Name".ljust(16),
                                  "Current Setting".ljust(56),
                                  "Required".ljust(10),
                                  "Description".ljust(col_width), colors.ENDC
                                  )
                          )
                    print("{} {} {} {}"
                          .format("----".ljust(16),
                                  "---------------".ljust(56),
                                  "--------".ljust(10),
                                  "-----------".ljust(col_width)
                                  )
                          )
                    for i in dir(self.__mh.Instance):
                        res = re.search('_(.*)_', i)
                        if res is None and "run" not in i:
                            print("{} {} {} {}"
                                  .format(i.ljust(16),
                                    str(self.__mh.Instance.__dict__[i]['value']).ljust(56),
                                    str(self.__mh.Instance.__dict__[i]['required']).ljust(10),
                                    str(self.__mh.Instance.__dict__[i]['description']).ljust(col_width)
                                  )
                            )
                    print("\n")
                else:
                    print('No module loaded or module does not have run options.')
            elif 'modules' in args:
                print("\n")
                print("{}{} {} {} {}{}".format(colors.OKGREEN, 'Module'.ljust(28), 'Date'.ljust(12), 'Rank'.ljust(12),
                                           'Description'.ljust(26), colors.ENDC))
                print("{} {} {} {}".format('______'.ljust(28), '____'.ljust(12), '____'.ljust(12),
                                           '___________'.ljust(26)))
                dirs = os.listdir('./modules/')
                for d in dirs:
                    if "_" not in d and '.py' not in d:
                        files = os.listdir('./modules/{}'.format(d))
                        for f in files:
                            res = re.search('_(.*)_', f)
                            if res is None:
                                self.__mh = ModuleHandler.ModuleHandler()
                                self.__mh.use('{}.{}'.format(d, f.replace('.py', '').replace('./modules/', '')))
                                print("{} {} {} {}".format(str(self.__mh.Instance.__title__).ljust(28),
                                                           str(self.__mh.Instance.__date__).ljust(12),
                                                           str(self.__mh.Instance.__rank__).ljust(12),
                                                           str(self.__mh.Instance.__description__)).ljust(26))
                                self.__mh.unload()
                print("\n")
            elif 'info' in args:
                print("\n")
                print("{}{}".format(colors.OKGREEN, 'About'.ljust(28)))
                print("{}".format('______\n'.ljust(28)))

                print("{}Title: {}{}".format(colors.OKGREEN, colors.ENDC, str(self.__mh.Instance.__title__)))
                print("{}Last Updated: {}{}".format(colors.OKGREEN, colors.ENDC, str(self.__mh.Instance.__date__)))
                print("{}Rank: {}{}".format(colors.OKGREEN, colors.ENDC, str(self.__mh.Instance.__rank__)))

                print("{}{}".format(colors.OKGREEN, '\nDescription'.ljust(28)))
                print("{}".format('______\n'.ljust(28)))

                print("{}{}".format(colors.ENDC, str(self.__mh.Instance.__description__)))

                print("{}{}".format(colors.OKGREEN, '\nDetails'.ljust(28)))
                print("{}".format('______\n'.ljust(28)))

                print("{}{}".format(colors.ENDC, str(self.__mh.Instance.__details__)))
                print("\n")
        except Exception as e:
            print(e)

    def do_kit_help(self, args):
        """
        Command: kit_help
        Description: Show toolkit help information
        """
        print("\n")
        print("IntruKit Commands")
        print("=================\n")
        print("     Command     Description")
        print("     -------     -----------")
        print("     exit        Exit the application")
        print("\n")
        print("Module Commands")
        print("===============\n")
        print("     Command     Description")
        print("     -------     -----------")
        print("     run         Execute the module's run function")
        print("     set         Set a module's option value")
        print("     show <type> Show all modules or module options: Accepts: modules, options")
        print("     unload      Unload the currently loaded module")
        print("     update      Update Intrukit via git pull. Requires restart")
        print("     use         Call a module by filename with no extension")
        print("\n")

    def do_update(self, args):
        """
        Command: update
        Description: Update the toolkit
        """
        print("\n")
        print("IntruKit Update")
        print("========================\n")
        print(subprocess.check_output("git pull", shell=True).decode('utf-8'))
        print("Please exit and restart the application.")
        print("\n")
