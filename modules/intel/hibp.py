"""
Have I Been Pwned

This module will perform a check with HIBP to see if an email address has been pwned.

"""

import os
import re
import json
import time
import requests
import cfscrape

class Module:
    """
    Module Class

    """

    __title__ = 'intel/hibp'
    __date__ = '2018-05-29'
    __rank__ = 'normal'
    __description__ = 'Check an email address against the Have I Been Pwned API'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def __init__(self, EMAIL='test@example.com', AGENT='Intrukit'):
        """
        __init__(self, EMAIL='test@example.com', AGENT='Intrukit)

        :param EMAIL:
        :param AGENT:

        Initialize the module with the module's desired options
        """
        self.__dict__['EMAIL'] = {"value": EMAIL, "required": True, "description": "Email address to target"}
        self.__dict__['AGENT'] = {"value": AGENT, "required": True, "description": "User-Agent to use for request"}

    def run(self):
        """
        run(self)

        :return:

        Run the module

        Original Developer: thewhiteh4t
        Resource: https://github.com/thewhiteh4t/pwnedOrNot
        """
        if self.EMAIL['value']:
            R = '\033[31m'  # red
            G = '\033[32m'  # green
            C = '\033[36m'  # cyan
            W = '\033[0m'   # white
            print('{}[{}+{}] Bypassing Cloudflare Restriction...'.format(W, G, W))
            headers = {'User-Agent': self.AGENT['value']}
            cookies, ua = cfscrape.get_tokens('https://haveibeenpwned.com/api/v2/breachedaccount/test@example.com',
                                                      user_agent=self.AGENT['value'])

            addr = str(self.EMAIL['value'])
            start = time.time()

            req = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/{0}'.format(addr), \
                               headers=headers, cookies=cookies)

            status = int(req.status_code)
            
            if status == 404:
                print('{}[{}-{}] Not found — the account could not be found and has therefore not been pwned'.format(W,
                                                                                                                     R,
                                                                                                                     W))
            elif status == 400:
                print('{}[{}-{}] Bad request — the account does not comply with an acceptable format'.format(W, R, W))
            elif status == 403:
                print('{}[{}-{}] Forbidden — no user agent has been specified in the request'.format(W, R, W))
            elif status == 429:
                print('{}[{}-{}] Too many requests — the rate limit has been exceeded'.format(W, R, W))
            elif status == 200:
                print('{}[{}+{}] Account pwned! Listing Breaches...'.format(W, G, W))
                json1 = json.loads(req.content)

                for item in json1:
                    print('\n'
                          + '{}[{}-{}] {}Breach      : {}{}'.format(W, G, W, G, W, str(item['Title'])) + '\n'
                          + '{}[{}-{}] {}Domain      : {}{}'.format(W, G, W, G, W, str(item['Domain'])) + '\n'
                          + '{}[{}-{}] {}Date        : {}{}'.format(W, G, W, G, W, str(item['BreachDate'])) + '\n'
                          + '{}[{}-{}] {}Fabricated  : {}{}'.format(W, G, W, G, W, str(item['IsFabricated'])) + '\n'
                          + '{}[{}-{}] {}Verified    : {}{}'.format(W, G, W, G, W, str(item['IsVerified'])) + '\n'
                          + '{}[{}-{}] {}Retired     : {}{}'.format(W, G, W, G, W, str(item['IsRetired'])) + '\n'
                          + '{}[{}-{}] {}Spam        : {}{}'.format(W, G, W, G, W, str(item['IsSpamList'])))

            else:
                print('{}[{}!{}] Unknown status {}'.format(W, C, W, status))


            r = requests.get('https://haveibeenpwned.com/api/v2/pasteaccount/{0}'.format(addr), headers=headers,
                              cookies=cookies)
            status2 = r.status_code

            if status2 != 200:
                print('{}[{}-{}] No Dumps Found'.format(W, R, W))
                print('{}[{}!{}] Completed in {} {}'.format(W, C, W, str(time.time() - start), 'seconds.'))
                return False

            json2 = json.loads(r.content)
            proceed = False
            for item in json2:
                if item['Source'] != 'Pastebin':
                    continue
                elif item['Source'] == 'Pastebin':
                    proceed = True

            # proceed tells the script to continue if the source is pastebin also it prevents multiple print statements
            if proceed:
                print('{}[{}+{}] Dumps Found!'.format(W, G, W))
                print('{}[{}+{}] Looking for Passwords! This may take a while...\n'.format(W, G, W))
            else:
                print('{}[{}-{}] No Dumps Found!'.format(W, R, W))
                return False

            for item in json2:
                if (item['Source']) == 'Pastebin':
                    link = item['Id']
                    page = requests.get('https://www.pastebin.com/raw/{}'.format(link))
                    sc = int(page.status_code)
                    if not sc == 404:
                        search = page.content
                        passwd = re.findall('{0}:(\w+)'.format(addr), search.decode('utf-8'))
                        if passwd:
                            print('{}[{}-{}] Found -> {}'.format(W, G, W, ' '.join(passwd)))

            print('{}[{}!{}] Completed in {} {}'.format(W, C, W, str(time.time() - start), 'seconds.'))
            return False
        else:
            print("You are missing required module options. Please see: show options")
