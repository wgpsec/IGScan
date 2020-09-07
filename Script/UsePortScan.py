from Core.PortScan import Nmapscan
from Core.PortScan import Masscan


class PortScan:

    def __init__(self):
        pass

    def nmapscan(self, hosts):
        nmapscan = Nmapscan(hosts)
        nmapscan.nmapscan()

    def masscan(self, hosts):
        masscan = Masscan(hosts)
        masscan.masscan()