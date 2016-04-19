# coding=utf-8

import os
import ftplib


class Ftp(ftplib.FTP):

    def exists(self, url):
        if url == "":
            return True
        arr = []
        self.dir(os.path.dirname(url), arr.append)
        arr = map(lambda x: x.split()[-1], arr)
        return os.path.basename(url) in arr

    def mkds(self, url):
        dirUrl = os.path.dirname(url)
        if not self.exists(dirUrl):
            self.mkds(dirUrl)
        self.mkd(url)

    def rmds(self, url):
        arr = []
        self.dir(url, arr.append)
        for v in arr:
            sub = v.split()
            if sub[0].startswith("d"):
                self.rmds(url + "/" + sub[-1])
            else:
                self.delete(url + "/" + sub[-1])
        self.rmd(url)
