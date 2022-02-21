import requests
import re
import time
import os
import datetime
import random
import string


class Img:
    def __init__(self, imgurl):
        self.imgurl = imgurl
        self.id = self.randomid()
        self.imgtype = self.imgtype()
        self.path = self.download()

    def imgtype(self):
        return re.search(".*?\.(jpg|png|gif|jpeg|svg|webp)", self.imgurl).group(1)

    def randomid(self):
        return str(datetime.datetime.now().strftime("%Y%m%d")) + '-' + ''.join(
            random.sample(string.ascii_lowercase + string.digits, 12))

    def download(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
        try:
            with open(f"img/{self.id}.{self.imgtype}", 'wb') as f:
                f.write(requests.get(self.imgurl, headers=headers).content)
            f.close()
            return f"img/{self.id}.{self.imgtype}"
        except:
            try:
                # 重下一次
                time.sleep(3)
                with open(f"img/{self.id}.{self.imgtype}", 'wb') as f:
                    f.write(requests.get(self.imgurl, headers=headers).content)
                f.close()
                return f"img/{self.id}.{self.imgtype}"
            except:
                os.remove(f"img/{self.id}.{self.imgtype}")
                return None
