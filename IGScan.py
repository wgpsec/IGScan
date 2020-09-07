import argparse
from Controller.Start import IGScan
from Script.Welcome import WgpBanner
"""
@auther: ro4lsc 
@version: v0.8
@descript: GetSubdomain模块: 获取子域名
           CheckURL模块: 判断存活链接
           PortScan模块: 端口扫描
           Anaylzer模块: Web容器指纹扫描
@time: 2020-08-09
"""
# Usage: python3 IGScan.py -u testphp.vulnweb.com -m subdomain,checkurl,webanaylzer
#        python3 IGScan.py -f targets.txt -m subdomain,checkurl,webanaylzer
#        python3 IGScan.py -i 127.0.0.1

parser = argparse.ArgumentParser(description="IGScan (Information Gathering Scan)")
parser.add_argument('-u', '--url', help='Taget URL')
parser.add_argument('-f', '--file', help='Place files for all domain names')
parser.add_argument('-i', '--ip', help='192.168.2.1 or CIDR 192.168.2.0/24')
parser.add_argument('-m', '--module', help='Select the module to detect the target', default='sudomain,checkurl,webanalyzer')  # 选择模块对目标进行探测

args = parser.parse_args()  # 实例化
targets_file = args.file
hosts = args.ip
url = args.url
module = args.module
print(WgpBanner())

IGScan = IGScan(url, targets_file, hosts, module)
IGScan.Start()

