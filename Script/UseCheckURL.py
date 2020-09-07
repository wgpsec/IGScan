from Core.CheckURL import RequestsURL

class CheckURL:
    def __init__(self):
        self.RequestsURL = RequestsURL()
    def url_start(self):
        RequestsURL = self.RequestsURL
        RequestsURL.url_start()
    def file_start(self, targets_file):
        RequestsURL = self.RequestsURL
        RequestsURL.file_start(targets_file)