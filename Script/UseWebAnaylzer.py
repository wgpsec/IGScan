from Utils.Webanaylzer import Webanalyzer
import queue
import threading
import time
q = queue.Queue()
class Anaylzer:
    def __init__(self):
        self.webanalyzer = Webanalyzer()
        self.link_file = "Output/link.txt"

    def anaylzer(self, total_num):
        starttime = time.time()
        while not q.empty():
            get_url = q.get()
            endtime = time.time()
            program_time = (endtime-starttime)
            threading.Thread(target=self.progress, args=(total_num, program_time)).start()  # 应该放到get后面，不然就会显示18
            w = self.webanalyzer
            w.arr_res(target_url=get_url)

    def progress(self, total_num, time):
        get_num = total_num - q.qsize()  # 获取当前已探测的链接数
        Remaining_time = (total_num * time / get_num) - time  # 程序剩余运行时间 预计总时间-已运行时间
        print('\r\033[34m[PROG]\033[0m Detected: %d Progress: %.2f %% Time: %.1fs The Remaining time: %.2fs' % (get_num, (get_num / total_num * 100), time, Remaining_time), end="")



    def one_module_start(self, target_url):
        print('\033[34m[INFO]\033[0m Webanaylzer Module Running!')
        w = self.webanalyzer
        w.one_arr_res(target_url)

    def url_start(self):
        thread_list = []
        print('\033[34m[INFO]\033[0m Webanaylzer Module Running!')
        with open(self.link_file, 'r') as f:
            for i in f.readlines():
                q.put(i.strip('\n'))
        total_num = q.qsize()  # 获取所有链接数目 http/https
        print('\033[34m[INFO]\033[0m The total number of targets to be detected is: %d' % total_num)  # 要获取的链接总数为
        for i in range(15):
            t = threading.Thread(target=self.anaylzer, args=(total_num, ))
            thread_list.append(t)
        for t in thread_list:
            time.sleep(0.01)
            t.start()
        for t in thread_list:
            t.join()
        print('\n\033[032m[SUCC]\033[0m Webanaylzer Module Has Finished Running!')

    def file_start(self, targets_file):
        thread_list = []
        print('\033[34m[INFO]\033[0m Webanaylzer Module Running!')
        with open(targets_file, 'r') as f:
            for i in f.readlines():
                q.put(i.strip('\n'))
        total_num = q.qsize()  # 获取所有链接数目 http/https
        print('\033[34m[INFO]\033[0m The total number of targets to be detected is: %d' % total_num)  # 要获取的链接总数为
        for i in range(15):
            t = threading.Thread(target=self.anaylzer, args=(total_num,))
            thread_list.append(t)
        for t in thread_list:
            time.sleep(0.01)
            t.start()
        for t in thread_list:
            t.join()
        print('\n\033[032m[SUCC]\033[0m Webanaylzer Module Has Finished Running!')