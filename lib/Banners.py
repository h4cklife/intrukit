"""
IntruKit Banners

This file holds the random banners displayed at the start of intrukit
"""
import os
import fnmatch
import random
from termcolor import colored

"""Banners"""

banner0 = """\033[92m
           _____       _                    _ _   
           \_   \_ __ | |_ _ __ _   _  /\ /(_) |_ 
            / /\/ '_ \| __| '__| | | |/ //_/ | __|
         /\/ /_ | | | | |_| |  | |_| / __ \| | |_ 
         \____/ |_| |_|\__|_|   \__,_\/  \/|_|\__|
\033[0m\n
               Penetration Testing ToolKit
\033[92mAuxiliary:\033[0m {} \033[92mEncoder:\033[0m {} \033[92mExample:\033[0m {} \033[92mExtractor:\033[0m {} \033[92mHandler:\033[0m {}\n             \033[92mIntel:\033[0m {} \033[92mPayload:\033[0m {} \033[92mUtility:\033[0m {} \n
"""

banner0 = banner0.format(
            len(fnmatch.filter(os.listdir('modules/auxiliary'), '*.py'))-1,
            len(fnmatch.filter(os.listdir('modules/encoder'), '*.py'))-1,
            len(fnmatch.filter(os.listdir('modules/example'), '*.py'))-1,
            len(fnmatch.filter(os.listdir('modules/extractor'), '*.py'))-1,
            len(fnmatch.filter(os.listdir('modules/handler'), '*.py'))-1,
            len(fnmatch.filter(os.listdir('modules/intel'), '*.py'))-1,
            len(fnmatch.filter(os.listdir('modules/payload'), '*.py'))-1,
            len(fnmatch.filter(os.listdir('modules/utility'), '*.py'))-1
        )


banner1 = """
    
                                   ________________
                              ____/ (  (    )   )  \___
                             /( (  (  )   _    ))  )   )\\
                           ((     (   )(    )  )   (   )  )
                         ((/  ( _(   )   (   _) ) (  () )  )
                        ( (  ( (_)   ((    (   )  .((_ ) .  )_
                       ( (  )    (      (  )    )   ) . ) (   )
                      (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                      ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                     ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                      (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                     ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                      ((  (   )(    (     _    )   _) _(_ (  (_ )
                       (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                       ((__)        \\\\||lll|l||///          \_))
                                (   /(/ (  )  ) )\   )
                              (    ( ( ( | | ) ) )\   )
                               (   /(| / ( )) ) ) )) )
                             (     ( ((((_(|)_)))))     )
                              (      ||\(|(|)|/||     )
                            (        |(||(||)||||        )
                              (     //|/l|||)|\\\\ \     )
                            (/ / //  /|//||||\\\\  \ \  \ _)
-------------------------------------------------------------------------------------------
\033[92mAuxiliary:\033[0m {} \033[92mEncoder:\033[0m {} \033[92mExample:\033[0m {} \033[92mExtractor:\033[0m {} \033[92mHandler:\033[0m {} \033[92mIntel:\033[0m {} \033[92mPayload:\033[0m {} \033[92mUtility:\033[0m {} 
\033[0m                   Intrukit - Penetration Testing ToolKit


"""

banner1 = banner1.format(
            len(fnmatch.filter(os.listdir('modules/auxiliary'), '*.py'))-1,
            len(fnmatch.filter(os.listdir('modules/encoder'), '*.py'))-1,
            len(fnmatch.filter(os.listdir('modules/example'), '*.py'))-1,
            len(fnmatch.filter(os.listdir('modules/extractor'), '*.py'))-1,
            len(fnmatch.filter(os.listdir('modules/handler'), '*.py'))-1,
            len(fnmatch.filter(os.listdir('modules/intel'), '*.py'))-1,
            len(fnmatch.filter(os.listdir('modules/payload'), '*.py'))-1,
            len(fnmatch.filter(os.listdir('modules/utility'), '*.py'))-1
        )


"""Configuration"""
max = 1
banners = [banner0, banner1]

def random_banner():
    """
    random_banner()
    
    :return:
     
    Return a random banner for our banner list
    """
    n = random.randint(0, max)
    return banners[n]

