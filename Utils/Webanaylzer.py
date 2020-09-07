import webanalyzer
import random


class Webanalyzer:
    def __init__(self):
        self.fingerprint_file = "Output/fingerprint.txt"
        self.web_framework = ['microsoft asp.net']
        self.web_servers = [
            'microsoft-iis', 'apache', 'nginx', 'openresty', 'tengine', 'apache tomcat',
            'jboss web', 'jboss application server', 'java servlet'
        ]
        self.web_language = ['asp', 'java', 'php', 'html5', 'lua']
        self.javascript_framework = ['requirejs', 'jquery', 'angularjs']
        self.keyword = ['phpinfo']
        self.cms = [
            'wordpress', 'phpcms', 'dedecms', 'public cms', '捷点jcms', 'opencms',
            'cms-made-simple', 'kesioncms', '海洋cms', 'aspcms', 'orchard cms', 'sdcms',
            'discuz', 'phpwind', 'wecenter', 'ecshop', 'siteserver', 'shopify', 'metinfo',
            '正方教务管理系统', 'rcms'
        ]
        self.operating_systems = ['windows server', 'unix']
        self.waf = ['safedog', 'f5_bigip', '360网站安全检测', '安全狗']

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

    def analyzer(self, target_url):
        w = webanalyzer.WebAnalyzer()
        w.headers = {
            "User-Agent": self.get_random_headers()
        }
        w.aggression = 0   # agression模式级别
        w.allow_redirect = True  # 是否进行跳转
        w.timeout = 1  # requests timeout
        w.rule_dir = "Utils/rules"  # 规则文件
        # w.update_rules()  # 更新规则
        # print(os.getcwd())
        # w.reload_rules()  # 重新加载rules
        # print("num: %d" % n)
        res = w.start(target_url, reload=True)
        if res == '' or res == None:
            res = ''
            return res
        else:
            return res
    
    def arr_res(self, target_url):
        info = []
        version_info = []
        result = self.analyzer(target_url=target_url)
        if result != "" and result != None:
            for i in result:
                name = i['name']
                origin = i['origin']
                try:
                    version = i['version']
                    version_info.append(name.lower()+version)
                except:
                    pass
                if origin == "fofa":
                    info.append(name.lower())
                elif origin == "wappalyzer":
                    info.append(name.lower())
                elif origin == "whatweb":
                    info.append(name.lower())
                elif origin == "implies":
                    if len(name) > 2:
                        info.append(name.lower())
            # print(version_info)
            for i in version_info:
                info.append(i)
            arr_info = list(set(info))
            # keywords
            web_framework = self.web_framework
            web_servers = self.web_servers
            web_language = self.web_language
            javascript_framework = self.javascript_framework
            keyword = self.keyword
            cms = self.cms
            operating_systems = self.operating_systems
            waf = self.waf
            match_info = []
            file = open(self.fingerprint_file, 'a')
            ## cms_info
            # print()
            # print("\033[34m[TARG]\033[0m Target: %s " % target_url)
            file.write("Target: %s " % target_url + '\n')
            try:
                cms_info = list(set(arr_info).intersection(set(cms)))[0]  # 两个列表交集
                # print("\033[32m[INFO]\033[0m CMS: %s" % cms_info)
                file.write("CMS: %s" % cms_info + '\n')
                match_info.append(cms_info)
            except:
                # print("\033[31m[WARN]\033[0m CMS: UnKnow")
                pass
            def info_pr(mc, text):
                """
                :param mc:  match 匹配到的banner
                :param text: 需要输出的信息
                :return:
                """
                mc_info = list(set(arr_info).intersection(set(mc)))
                if len(mc_info) > 0:
                    for i in mc_info:
                        match_info.append(i)
                    # print("\033[32m[INFO]\033[0m " + text + " %s " % ", ".join(str(i) for i in mc_info))
                    file.write(text + " %s " % ", ".join(str(i) for i in mc_info) + '\n')
            info_pr(web_servers, "Web Server:")
            info_pr(operating_systems, "Operating Systems:")
            info_pr(web_language, "Programming Language:")
            info_pr(web_framework, "Web Framework:")
            info_pr(javascript_framework, "JavaScript Framework:")
            info_pr(keyword, "Keyword:")
            info_pr(waf, "Waf:")
            other_info = set(arr_info).difference(set(match_info))
            for i in other_info:
                if len(i) > 40:
                    other_info.pop()
            # print("\033[34m[INFO]\033[0m Other: %s" % ", ".join(str(i) for i in list(set(other_info))))
            file.write("Other: %s" % ", ".join(str(i) for i in list(set(other_info))) + '\n')
            file.write('\n')
            file.close()

    def one_arr_res(self, target_url):
        info = []
        version_info = []
        result = self.analyzer(target_url=target_url)
        if result != "" and result != None:
            for i in result:
                name = i['name']
                origin = i['origin']
                try:
                    version = i['version']
                    version_info.append(name.lower() + version)
                except:
                    pass
                if origin == "fofa":
                    info.append(name.lower())
                elif origin == "wappalyzer":
                    info.append(name.lower())
                elif origin == "whatweb":
                    info.append(name.lower())
                elif origin == "implies":
                    if len(name) > 2:
                        info.append(name.lower())
            # print(version_info)
            for i in version_info:
                info.append(i)
            arr_info = list(set(info))
            # keywords
            web_framework = self.web_framework
            web_servers = self.web_servers
            web_language = self.web_language
            javascript_framework = self.javascript_framework
            keyword = self.keyword
            cms = self.cms
            operating_systems = self.operating_systems
            waf = self.waf
            match_info = []
            ## cms_info
            # print()
            # print("\033[34m[TARG]\033[0m Target: %s " % target_url)
            try:
                cms_info = list(set(arr_info).intersection(set(cms)))[0]  # 两个列表交集
                print("\033[32m[INFO]\033[0m CMS: %s" % cms_info)
                match_info.append(cms_info)
            except:
                print("\033[31m[WARN]\033[0m CMS: UnKnow")

            def info_pr(mc, text):
                """
                :param mc:  match 匹配到的banner
                :param text: 需要输出的信息
                :return:
                """
                mc_info = list(set(arr_info).intersection(set(mc)))
                if len(mc_info) > 0:
                    for i in mc_info:
                        match_info.append(i)
                    print("\033[32m[INFO]\033[0m " + text + " %s " % ", ".join(str(i) for i in mc_info))

            info_pr(web_servers, "Web Server:")
            info_pr(operating_systems, "Operating Systems:")
            info_pr(web_language, "Programming Language:")
            info_pr(web_framework, "Web Framework:")
            info_pr(javascript_framework, "JavaScript Framework:")
            info_pr(keyword, "Keyword:")
            info_pr(waf, "Waf:")
            other_info = set(arr_info).difference(set(match_info))
            for i in other_info:
                if len(i) > 40:
                    other_info.pop()
            print("\033[34m[INFO]\033[0m Other: %s" % ", ".join(str(i) for i in list(set(other_info))))