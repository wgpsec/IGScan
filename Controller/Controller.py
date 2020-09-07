import os
import sys
import time
from Script.UseGetSubdomain import GetDomain
from Script.UsePortScan import PortScan
from Script.UseCheckURL import CheckURL
from Script.UseWebAnaylzer import Anaylzer

class Subdomain:
    def __init__(self):
        self.subdomain_file = 'Output/subdomain.txt'

    def url_subdomain(self, url):
        Getdomain = GetDomain()
        Getdomain.url_Getdomain(url)

    def file_subdomain(self, targets_filename):
        Getdomain = GetDomain()
        Getdomain.file_Getdomain(targets_filename)

class Checkurl:
    def url_Check(self):  # 当两个模块一起使用的时候可以
        Checkurl = CheckURL()
        Checkurl.url_start()

    def file_Check(self, targets_file):
        Checkurl = CheckURL()
        Checkurl.file_start(targets_file)


class Portscan:
    def __init__(self):
        pass

    def nmapscan(self, hosts):
        starttime = time.time()
        nmapscan = PortScan()
        nmapscan.nmapscan(hosts)
        endtime = time.time()
        print('\033[34m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))

    def masscan(self, hosts):
        starttime = time.time()
        masscan = PortScan()
        masscan.masscan(hosts)
        endtime = time.time()
        print('\033[34m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))


class Webanaylzer:
    def one_analyzer(self, target_url):
        w = Anaylzer()
        w.one_module_start(target_url)

    def url_analyzer(self):
        w = Anaylzer()
        w.url_start()
    def file_analyzer(self, targets_file):
        w = Anaylzer()
        w.file_start(targets_file)

