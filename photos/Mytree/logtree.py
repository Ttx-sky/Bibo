import json
import queue


class Tree:  # 路径导航
    def __init__(self, l=None, pic_response=None, pic_path=None, group=None):
        if l is None:
            l = {}
        self.pic_response = pic_response
        self.pic_path = pic_path
        self.group = group
        self.q = queue.Queue()
        self.l = l

    def main(self):
        lr: list = [{self.group: {"socket": self.pic_response, "Mylog": self.pic_path}}]
        self.l[f"{self.group}"] = {"网络地址": f"{self.pic_response}", "本地地址": f"{self.pic_path}"}
        # print(self.l)
        return self.l
