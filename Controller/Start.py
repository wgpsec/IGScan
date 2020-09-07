import os
import time
from .Controller import Subdomain, Checkurl, Portscan, Webanaylzer


class IGScan:
    def __init__(self, url, targets_file, hosts, module):
        self.url = url
        self.targets_file = targets_file
        self.hosts = hosts
        self.module = module
        self.Subdomain = Subdomain()
        self.Checkurl = Checkurl()
        self.PortScan = Portscan()
        self.Webanaylzer = Webanaylzer()

    def Start(self):
        url = self.url
        targets_file = self.targets_file
        hosts = self.hosts
        module = self.module
        Subdomain = self.Subdomain
        Checkurl = self.Checkurl
        Portscan = self.PortScan
        Webanaylzer = self.Webanaylzer
        # print(module)
        if not os.path.exists('Output/'):
            os.mkdir('Output/')
        if module != '' and module != None:
            module = module.split(',')
            if url != '' and url != None:
                all_module = ['subdomain', 'checkurl', 'webanalyzer']
                inse_module = list(set(all_module).intersection(set(module)))  # 交集
                dif_module = list(set(all_module).difference(set(module)))  # 并集
                # print(module)
                if len(dif_module) == 0:
                    starttime = time.time()
                    Subdomain.url_subdomain(url)
                    Checkurl.url_Check()
                    Webanaylzer.url_analyzer()
                    endtime = time.time()
                    print('\033[32m[SUCC]\033[0m All target links have been collected!')
                    print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))

                if len(dif_module) == 1:
                    if module[0] == 'subdomain':
                        starttime = time.time()
                        Subdomain.url_subdomain(url)
                        Checkurl.url_Check()
                        endtime = time.time()
                        print('\033[32m[SUCC]\033[0m All target links have been collected!')
                        print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
                    if module[0] == 'webanalyzer':
                        starttime = time.time()
                        Subdomain.url_subdomain(url)
                        Checkurl.url_Check()
                        endtime = time.time()
                        print('\033[32m[SUCC]\033[0m All target links have been collected!')
                        print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))

                if len(inse_module) == 1:
                    if module[0] == 'subdomain':
                        starttime = time.time()
                        Subdomain.url_subdomain(url)
                        endtime = time.time()
                        print('\033[32m[SUCC]\033[0m All target links have been collected!')
                        print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
                    elif module[0] == 'checkurl':
                        starttime = time.time()
                        Checkurl.url_Check()
                        endtime = time.time()
                        print('\033[32m[SUCC]\033[0m All target links have been collected!')
                        print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
                    elif module[0] == 'webanalyzer':
                        starttime = time.time()
                        Webanaylzer.one_analyzer(url)
                        endtime = time.time()
                        print('\033[32m[SUCC]\033[0m All target links have been collected!')
                        print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))

            if targets_file != '' and targets_file != None:
                all_module = ['subdomain', 'checkurl', 'webanalyzer']
                inse_module = list(set(all_module).intersection(set(module)))
                dif_module = list(set(all_module).difference(set(module)))
                # print(module)
                if len(dif_module) == 0:
                    starttime = time.time()
                    Subdomain.file_subdomain(targets_file)
                    Checkurl.file_Check(targets_file)
                    Webanaylzer.file_analyzer(targets_file)
                    endtime = time.time()
                    print('\033[32m[SUCC]\033[0m All target links have been collected!')
                    print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))

                if len(dif_module) == 1:
                    if module[0] == 'subdomain':
                        starttime = time.time()
                        Subdomain.file_subdomain(targets_file)
                        Checkurl.file_Check(targets_file)
                        endtime = time.time()
                        print('\033[32m[SUCC]\033[0m All target links have been collected!')
                        print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
                    if module[0] == 'webanalyzer':
                        starttime = time.time()
                        Subdomain.file_subdomain(targets_file)
                        Checkurl.file_Check(targets_file)
                        endtime = time.time()
                        print('\033[32m[SUCC]\033[0m All target links have been collected!')
                        print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))

                if len(inse_module) == 1:
                    if module[0] == 'subdomain':
                        starttime = time.time()
                        Subdomain.file_subdomain(targets_file)
                        endtime = time.time()
                        print('\033[32m[SUCC]\033[0m All target links have been collected!')
                        print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
                    elif module[0] == 'checkurl':
                        starttime = time.time()
                        Checkurl.file_Check(targets_file)
                        endtime = time.time()
                        print('\033[32m[SUCC]\033[0m All target links have been collected!')
                        print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))
                    elif module[0] == 'webanalyzer':
                        starttime = time.time()
                        Webanaylzer.file_analyzer(targets_file)
                        endtime = time.time()
                        print('\033[32m[SUCC]\033[0m All target links have been collected!')
                        print('\033[32m[TIME]\033[0m The program is running time: %.2fs' % (endtime - starttime))

        if hosts != '' and hosts != None:
            Portscan = Portscan
            if '/' in hosts:
                Portscan.masscan(hosts)
            else:
                Portscan.nmapscan(hosts)

