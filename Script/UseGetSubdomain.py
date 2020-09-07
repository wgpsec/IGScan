import time
from Core.GetSubdomain import GetSubdomain
import queue
import threading


class GetDomain:

    def __init__(self):
        self.subdomain_num = 0
        self.targets_queue = queue.Queue()
        self.arr_subdomain = []  # 去重后的域名
        self.subdomain_filename = 'Output/subdomain.txt'  # 子域名result
        self.GetSubdomain = GetSubdomain()

    # -u参数
    def url_Getdomain(self, url):
        print('\033[034m[INFO]\033[0m GetDomain Module Running!')
        open_subdomainfile = open(self.subdomain_filename, 'w')
        arr_subdomain = self.arr_subdomain
        url = url.strip('\n')
        GetSubdomain = self.GetSubdomain
        for i in GetSubdomain.all2one(url):
            arr_subdomain.append(i)
        arr_subdomain = list(set(arr_subdomain))
        self.subdomain_num = len(arr_subdomain)
        for i in arr_subdomain:
            open_subdomainfile.write(i+'\n')
        open_subdomainfile.close()
        print('\033[034m[INFO]\033[0m Number of subdomains: %s' % (self.subdomain_num))
        print('\033[032m[SUCC]\033[0m GetDomain Module Has Finished Running!')

    # -f参数
    def file_Getdomain(self, targets_filename):
        # --定义header头
        starttime = time.time()
        targets_queue = self.targets_queue
        print('\033[034m[INFO]\033[0m GetDomain Module Running!')
        open_subdomainfile = open(self.subdomain_filename, 'w')  # 写入subdomain.txt文件
        arr_subdomain = self.arr_subdomain
        with open(file=targets_filename, mode='r') as domain:
            for url in domain.readlines():
                url = url.strip('\n')
                targets_queue.put(url)
        total_num = targets_queue.qsize()
        print('\033[34m[INFO]\033[0m The total number of targets to be detected is: %d' % total_num)
        GetSubdomain = self.GetSubdomain
        thread_list = []
        def thread_file_Getdomain():
            while not targets_queue.empty():
                get_url = targets_queue.get()
                endtime = time.time()
                program_time = (endtime - starttime)
                threading.Thread(target=self.file_Getdomain_progress, args=(total_num, program_time,)).start()
                for i in GetSubdomain.all2one(get_url):
                    arr_subdomain.append(i)
        for i in range(15):
            t = threading.Thread(target=thread_file_Getdomain)
            thread_list.append(t)
        for t in thread_list:
            time.sleep(0.01)
            t.start()
        for t in thread_list:
            t.join()
        # --- 域名去重
        arr_subdomain = list(set(arr_subdomain))
        self.subdomain_num = len(arr_subdomain)
        for i in arr_subdomain:
            open_subdomainfile.write(i+'\n')
        open_subdomainfile.close()
        print('\n\033[034m[INFO]\033[0m Number of subdomains: %s' % (self.subdomain_num))
        print('\033[032m[SUCC]\033[0m GetDomain Module Has Finished Running!')

    # 进度条
    def file_Getdomain_progress(self, total_num, time):
        """
        :param total_num: 所有需要探测的域名数量
        :param time: 程序已运行时长
        :return:
        """
        get_num = total_num - self.targets_queue.qsize()
        Remaining_time = (total_num * time / get_num) - time  # 程序剩余运行时间 预计总时间-已运行时间
        print('\r\033[34m[PROG]\033[0m Detected: %d Progress: %.2f %% Time: %.2fs The Remaining time: %.2fs' % (
            get_num, (get_num / total_num * 100), time, Remaining_time), end="")