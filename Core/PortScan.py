import nmap
import masscan

class Nmapscan:


    def __init__(self, hosts):
        self.hosts = hosts
        # self.ports = '1-65535'
        self.arguments = '-sS -T5 -Pn'


    def nmapscan(self):
        nmscan = nmap.PortScanner()  # 实例化
        print('\033[34m[INFO]\033[0m Nmap PortScan Module Running!')
        # print('\033[31m[PASS]\033[0m Please enter root password: ')
        nm = nmscan.scan(hosts=self.hosts, arguments=self.arguments, sudo=True)
        # print(nmscan.command_line())  # 返回命令行
        all_hosts = nmscan.all_hosts()  # 所有的主机列表
        # print(all_hosts)
        # print(nm['scan'])
        # bool函数判断字典是否为空
            # if bool(nm['scan']) != 0:
        for host in all_hosts:
            if host == '':
                print('\033[31m[ERRO]\033[0m No Surviving Hosts')
            else:
                print('\033[34m[ONLI]\033[0m Online Host: %s' % host)
        for host in all_hosts:
            print('\033[32m[TARG]\033[0m Target: %s' % host)
            # print(nm['scan'])
            # print(nmscan[host].all_protocols())  # 返回协议
            try:
                port_all = nm['scan'][host]['tcp'].keys()
                # print(port_all)
                for port in port_all:
                    # i 开放的端口
                    target_port_state = nm['scan'][host]['tcp'][port]['state']  # 端口开放状态
                    target_service_name = nm['scan'][host]['tcp'][port]['name']  # 开启服务
                    if target_port_state == 'open':
                        print('\033[32m[OPEN]\033[0m Port: %s Status: %s Service: %s' % (port, target_port_state, target_service_name))
                    elif target_port_state == 'closed':
                        print('\033[31m[CLOS]\033[0m Port: %s Status: %s Service: %s' % (port, target_port_state, target_service_name))
                    else:
                        print('\033[33m[FILT]\033[0m Port: %s Status: %s Service: %s' % (port, target_port_state, target_service_name))
                print()
            except:
                print('\033[31m[WARN]\033[0m No ports open!')
        print('\033[32m[SUCC]\033[0m PortScan Module Has Finished Running!')


class Masscan:


    def __init__(self, hosts):
        self.hosts = hosts
        self.ports = '0-10000,27017,27018'
        self.arguments = '--max-rate 10000'


    def masscan(self):
        print('\033[34m[INFO]\033[0m Masscan PortScan Module Running!')
        try:
            mascan = masscan.PortScanner()
            mas = mascan.scan(hosts=self.hosts, ports=self.ports, arguments=self.arguments)
            for host in mascan.all_hosts:
                if host == '':
                    print('\033[31m[ERRO]\033[0m No Surviving Hosts')
                else:
                    print('\033[34m[ONLI]\033[0m Online Host: %s' % host)
            for host in mascan.all_hosts:
                print('\033[32m[TARG]\033[0m Target: %s' % host)
                port_all = mas['scan'][host]['tcp'].keys()
                port_all = list(port_all) # dict转list
                # print(port_all)
                for port in port_all:
                    target_port_state = mas['scan'][host]['tcp'][port]['state']
                    # print('\033[32m[INFO]\033[0m Port: %s Status: %s' % (port, target_port_state))
                    if target_port_state == 'open':
                        print('\033[32m[OPEN]\033[0m Port: %s Status: %s' % (port, target_port_state))
                    elif target_port_state == 'closed':
                        print('\033[31m[CLOS]\033[0m Port: %s Status: %s' % (port, target_port_state))
                    else:
                        print('\033[33m[FILT]\033[0m Port: %s Status: %s' % (port, target_port_state))
                print()
            print('\033[32m[SUCC]\033[0m PortScan Module Has Finished Running!')
        except Exception as e:
            print('\033[31m[ERRO] %s' % e)
