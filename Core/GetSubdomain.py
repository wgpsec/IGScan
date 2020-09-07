import requests
import json
import re
import random
import math
import time
import threading
import queue
import requests.packages.urllib3

"""
@descript: 目前程序调用了六个接口用于获取子域名，后续会持续添加
"""
queue = queue.Queue()


class GetSubdomain:
    def __init__(self):
        self.headers_list = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }

    def get_random_headers(self):
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
        return random.choice(user_agent_list)

    def fix_illegal_domain(self, domain):  # 修复不合法的域名
        res = re.findall(r'\.\w*', domain)  # 结果
        if len(res) == 3:  # 例如www.xxx.edu.cn 就会匹配到 .xxx .edu .cn
            try:
                domain = res[0].strip('.') + '.' + res[1].strip('.') + res[2]
            except:
                return domain
        elif len(res) == 2:  # www.xxx.cn xxx.com.cn
            if 'www' in domain:
                try:
                    domain = res[0].strip('.') + '.' + res[1].strip('.')  # 如果url为www.roalsc.top的话 匹配出['.ro4lsc', '.top']
                except:
                    return domain  # 如果为roalsc.top则正常输出
            else:
                return domain
        else:
            return domain
        return domain

    # 百度云观测
    def ce_baidu(self, domain):
        try:
            headers = {"User-Agent": self.get_random_headers()}
            domain = self.fix_illegal_domain(domain)  #  修复不合法的域名
            url = 'http://ce.baidu.com/index/getRelatedSites?site_address={0}'.format(domain)
            respon = requests.get(url, headers=headers)  # 访问这个接口，加个请求头防止被ban
            respon = json.loads(respon.text)  # 将json转换为字典
            for i in range(0, len(respon['data'])):  # 判断data里的数据长度，然后进行循环输出
            # 迭代器 迭代输出
            # 数据类型为json {"code":0,"data":[{"domain":"2013.sure56.com","score":80}
            #     print(respon['data'][i]['domain'])  # 整了一堆废话，还是对json不了解的原因
                queue.put(respon['data'][i]['domain'])
        except Exception as e:
            # print('\n\033[031m[ERRO]\033[0m ce_baidu API ERROR! %s' % e)
            pass

    # 爱站
    def aizhan(self, domain):
        try:
            domain = self.fix_illegal_domain(domain)
            url = 'https://baidurank.aizhan.com/baidu/{0}/'.format(domain)
            headers = {"User-Agent": self.get_random_headers()}
            respon = requests.get(url, headers=headers)  # 网页响应
            res = re.findall(r'[a-z.0-9]*\.' + domain, respon.text)
            res = list(set(res))  # 去重
            for i in range(0,len(res)):  # 循环输出res列表中的值
                queue.put(res[i])
        except:
            print('\033[031m[ERRO]\033[0m aizhan API ERROR!')

    # hackertarget
    def hackertarget(self, domain):
        """
        思路就是从输入的域名在网页的内容中进行匹配[a-z0-9].baidu.com,最后将结果进行匹配
        """
        try:
            headers = {"User-Agent" : self.get_random_headers()}
            domain = self.fix_illegal_domain(domain)
            url = 'https://api.hackertarget.com/hostsearch/?q={0}'.format(domain)
            respon = requests.get(url=url, headers=headers)  # 网页响应
            res = re.findall(r'[a-z.0-9]*\.' + url, respon.text)
            # print(res)
            for i in range(0, len(res)):
                queue.put(res[i])
        except:
            print('\033[031m[ERRO]\033[0m hackertarget API ERROR!')

    # IP138
    def IP138(self, domain):
        """
        思路就是从输入的域名在网页的内容中进行匹配[a-z0-9].baidu.com,最后将结果进行匹配
        """
        try:
            headers = {"User-Agent": self.get_random_headers()}
            domain = self.fix_illegal_domain(domain)
            url = 'https://site.ip138.com/{0}/domain.htm'.format(domain)
            respon = requests.get(url, headers=headers)  # 网页响应
            res = re.findall(r'[a-z.0-9]*\.' + domain, respon.text)
            res = list(set(res))  # 去重
            for i in range(0, len(res)):
                queue.put(res[i])
        except:
            print('\033[031m[ERRO]\033[0m IP138 API ERROR!')

    # crt.sh SSL 证书反查
    def crtsh(self, domain):
        try:
            domain = self.fix_illegal_domain(domain)
            headers = {"User-Agent": self.get_random_headers()}
            url = 'https://crt.sh/?q=%25.{0}'.format(domain)
            # print(url)
            requests.packages.urllib3.disable_warnings()
            respon = requests.get(url, headers=headers)  # 网页响应
            res = re.findall(r'[a-z.0-9]*\.' + domain, respon.text)
            # print(res)
            res = list(set(res))  # 去重
            for i in range(0, len(res)):
                queue.put(res[i].lstrip('.'))
        except:
            print('\033[031m[ERRO]\033[0m crtsh API ERROR!')

    def qianxun(self, domain):
        """
        :param domain:
        :return:
        ;describe:首先访问页面获取页面中的查询结果数/20得到页面数，然后重新访问页面，使用循环遍历获取子域名
        """
        url = 'https://www.dnsscan.cn/dns.html'
        headers = {"User-Agent": self.get_random_headers()}
        domain = self.fix_illegal_domain(domain)
        data = {
            "ecmsfrom": '8.8.8.8',
            "show": 'none',
            "keywords": domain
        }
        respon = requests.post(url, headers=headers, data=data)
        try:
            result = re.findall(r'查询结果为:[0-9].*条', respon.text)  # 查询结果数，用来判断有多少页面，一个页面有20条数据
            result = re.findall(r'[0-9].*', result[0])
            result = result[0].strip('条')  # 查询的总数
            pagenum = int(result) / 20
            pagenum = math.ceil(pagenum)  # 这个math.ceil可以向上去整数，这个pagenum作为访问页面的页面数
            # 重新定义，重新访问
            thread_list = []
            for i in range(1, pagenum+1):  # 有多少page就创建多少个线程
                t = threading.Thread(target=self.qianxun_speed, args=(i, domain, headers, ))
                thread_list.append(t)
            for t in thread_list:
                time.sleep(0.01)
                t.start()
            for t in thread_list:
                t.join()

                # for i in range(0, len(res)):
                #     queue.put(res[i])
        except:
            pass

    def qianxun_speed(self, pagenum, domain, headers):
        url = 'https://www.dnsscan.cn/dns.html?keywords={0}&page={1}'.format(domain, pagenum)
        data = {
            "ecmsfrom": '8.8.8.8',
            "show": 'none',
            "keywords": domain
        }
        respon = requests.post(url, headers=headers, data=data)
        res = re.findall(r'[a-z.0-9]*\.' + domain, respon.text)
        for i in range(0, len(res)):
            queue.put(res[i])

    def all2one(self, domain):
        # 使用守护进程，调用每个函数，优化执行速度
        subdomain_list = []
        thread_list = []
        # 使用循环速度还慢一些？
        ce_baidu_thread = threading.Thread(target=self.ce_baidu, args=(domain,))
        IP138_thread = threading.Thread(target=self.IP138, args=(domain,))
        qianxun_thread = threading.Thread(target=self.qianxun, args=(domain,))
        aizhan_thread = threading.Thread(target=self.aizhan, args=(domain,))
        hackertarget_thread = threading.Thread(target=self.hackertarget, args=(domain,))
        crtsh_thread = threading.Thread(target=self.crtsh, args=(domain,))
        thread_list.append(ce_baidu_thread)         # 0.32s 4498
        thread_list.append(IP138_thread)            # 0.16s 9 fix bug 0.47 2408
        thread_list.append(qianxun_thread)          # 49.57s 3453 Optimize speed 16.24s 3453
        thread_list.append(aizhan_thread)         # 0.24s 49
        # thread_list.append(hackertarget_thread)   # 1.87s 442 50次/天
        thread_list.append(crtsh_thread)          # 16.93s 1 fix bug 20.77s 506

        for t in thread_list:
            # t.setDaemon(True)
            time.sleep(0.01)
            t.start()
        for t in thread_list:
            t.join()
        while not queue.empty():
            subdomain_list.append(queue.get())
        return subdomain_list


