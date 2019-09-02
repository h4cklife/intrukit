"""
Virus Total

This module will allow you to query the Virus Total API

"""
import json, urllib, urllib3, argparse, hashlib, re, sys
import urllib.request as request

from pprint import pprint

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white

class vtAPI():
    """
    Original Developer: Xen0ph0n
    Modified by: Intrukit (dbe-5)
    Github: https://github.com/Xen0ph0n/VirusTotal_API_Tool
    """
    def __init__(self, APIKEY=None):
        self.api = APIKEY
        self.base = 'https://www.virustotal.com/vtapi/v2/'

    def getReport(self, md5):
        param = {'resource': md5, 'apikey': self.api, 'allinfo': '1'}
        url = self.base + "file/report"
        data = urllib.parse.urlencode(param)
        result = request.urlopen(url, data.encode('utf-8'))
        jdata = json.loads(result.read())
        return jdata

    def downloadFile(self, md5, name):
        try:
            param = {'hash': md5, 'apikey': self.api}
            url = self.base + "file/download"
            data = urllib.parse.urlencode(param)
            req = urllib3.Request(url, data.encode('utf-8'))
            result = request.urlopen(req)
            downloadedfile = result.read()
            if len(downloadedfile) > 0:
                fo = open(name, "wb")
                fo.write(downloadedfile)
                fo.close()
                print("{}[{}+{}] Malware downloaded to file {} for MD5 {}".format(W, G, W, name, md5))
            else:
                print("{}[{}-{}] No malware download found for MD5 {}".format(W, R, W, md5))
        except Exception:
            print("{}[{}-{}] No malware download found for MD5 {}".format(W, R, W, md5))

    def downloadPcap(self, md5, name):
        try:
            req = urllib3.Request(
                "https://www.virustotal.com/vtapi/v2/file/network-traffic?apikey=" + self.api + "&hash=" + md5)
            result = request.urlopen(req)
            pcapfile = result.read()
            if len(pcapfile) > 0 and '{"response_code": 0, "hash":' not in pcapfile:
                fo = open(name, "wb")
                fo.write(pcapfile)
                fo.close()
                print("{}[{}+{}] PCap downloaded to file {} for MD5 {}".format(W, G, W, name, md5))
            else:
                print("{}[{}-{}] PCap not available for MD5 {}".format(W, R, W, md5))
        except Exception:
            print("{}[{}-{}] {} PCap not available for MD5 {}".format(W, R, W, md5))

    def rescan(self, md5):
        param = {'resource': md5, 'apikey': self.api}
        url = self.base + "file/rescan"
        data = urllib.parse.urlencode(param)
        result = request.urlopen(url, data.encode('utf-8'))
        print("{}[{}+{}] Virus Total Rescan Initiated for {} (Requery in 10 Mins)".format(W, G, W, md5))

def checkMD5(checkval):
    """
    checkMD5(self, checkval)

    :param checkval:
    :return:
    """
    if re.match(r"([a-fA-F\d]{32})", checkval) is None:
        md5 = md5sum(checkval)
        return md5.upper()
    else:
        return checkval.upper()

def md5sum(filename):
    """
    md5sum(self, filename)

    :param filename:
    :return:
    """
    fh = open(filename, 'rb')
    m = hashlib.md5()
    while True:
        data = fh.read(8192)
        if not data:
            break
        m.update(data)
    return m.hexdigest()

def parse(it, md5, verbose, jsondump):
    """
    parse(self, it, md5, verbose, jsondump)

    :param it:
    :param md5:
    :param verbose:
    :param jsondump:
    :return:
    """
    if it['response_code'] == 0:
        print("{}[{}-{}] Virus Total return no results for MD5: {}".format(W, G, W, md5))
        return 0

    print("\n{}[{}+{}] Results for MD5: ".format(W, R, W), it['md5'],
          "{}[{}+{}] Detected by: ".format(W, R, W), it['positives'], '/', it['total'], '\n')

    for x in it['scans']:
        if it['scans'][x]['result'] == 'None' or it['scans'][x]['result'] is None:
            print('{}[{}-{}] {} Detection: '.format(W, G, W, x), it['scans'][x]['result'])
        else:
            print('{}[{}+{}] {} Detection: '.format(W, R, W, x), it['scans'][x]['result'])

    print('\n{}[{}+{}] Scanned on:'.format(W, R, W), it['scan_date'],
          '\n{}[{}+{}] Permalink: {}'.format(W, R, W, it['permalink']))

    if jsondump == True:
        jsondumpfile = open("VTDL" + md5 + ".json", "w")
        pprint(it, jsondumpfile)
        jsondumpfile.close()
        print("\n{}[{}+{}] JSON Written to File {}".format(W, G, W, "VTDL" + md5 + ".json"))

    if verbose == True:
        print('\n\t{}[{}+{}] Verbose VirusTotal Information Output:\n'.format(W, G, W))
        for x in it['scans']:
            print('\t', x, '\t' if len(x) < 7 else '', '\t' if len(x) < 14 else '', '\t', it['scans'][x][
                'detected'], '\t', it['scans'][x]['result'])

class Module:
    """
    Module Class
    """

    __title__ = 'intel/virus_total'
    __date__ = '2018-05-31'
    __rank__ = 'normal'
    __description__ = 'This module will allow you to query the Virus Total API'
    __details__ = 'None'

    __author__ = 'Intrukit'

    def __init__(self, FILEORHASH=None, REPORT=False, JSON=False, DOWNLOAD=False, PCAP=False, VERBOSE=False,
                 RESCAN=False, APIKEY=None):
        """
        __init__(self, FILEORHASH=None, REPORT=False, JSON=False, DOWNLOAD=False, PCAP=False, VERBOSE=False,
                 RESCAN=False,APIKEY=None)

        :param FILEORHASH:
        :param REPORT:
        :param JSON:
        :param DOWNLOAD:
        :param PCAP:
        :param VERBOSE:
        :param RESCAN:
        :param APIKEY:

        Initialize the module with the module's desired options
        """
        self.__dict__['FILEORHASH'] = {"value": FILEORHASH, "required": True, "description": "File to verify"}
        self.__dict__['APIKEY'] = {"value": APIKEY, "required": True, "description": "VT API key"}
        self.__dict__['REPORT'] = {"value": REPORT, "required": False, "description": "Return report for File or MD5"}
        self.__dict__['JSON'] = {"value": JSON, "required": False, "description": "JSON dump"}
        self.__dict__['DOWNLOAD'] = {"value": DOWNLOAD, "required": False, "description": "Download sample [DANGER]"}
        self.__dict__['PCAP'] = {"value": PCAP, "required": False, "description": "Download PCAP"}
        self.__dict__['VERBOSE'] = {"value": VERBOSE, "required": False, "description": "Be verbose"}
        self.__dict__['RESCAN'] = {"value": RESCAN, "required": False, "description": "Rescan the file or hash"}

    def run(self):
        """
        run(self)

        :return:

        Run the module
        """
        if self.FILEORHASH['value'] and self.APIKEY['value'] and (self.REPORT['value'] or self.JSON['value'] or
                                                            self.VERBOSE['value'] or self.DOWNLOAD['value'] or
                                                            self.PCAP['value'] or self.RESCAN['value']):
            vt = vtAPI(self.APIKEY['value'])
            md5 = None

            md5 = checkMD5(self.FILEORHASH['value'])

            if self.REPORT['value'] or self.JSON['value'] or self.VERBOSE['value']:
                parse(vt.getReport(md5), md5, self.VERBOSE['value'], self.JSON['value'])

            if self.DOWNLOAD['value']:
                name = "VTDL" + md5 + ".danger"
                vt.downloadFile(md5, name)

            if self.PCAP['value']:
                name = "VTDL" + md5 + ".pcap"
                vt.downloadPcap(md5, name)

            if self.RESCAN['value']:
                vt.rescan(md5)

        else:
            print("You are missing required module options. Please see: show options.")
            print("Must supply APIKEY, FILEORHASH and one of: REPORT, JSON, DOWNLOAD, PCAP, RESCAN")

