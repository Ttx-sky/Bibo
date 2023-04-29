import json
import re
import requests
import os
from Mytree.logtree import Tree
import mhy


class Whire:
    def __init__(self):
        self.url = "https://ys.mihoyo.com/main/"
        self.image_path = os.path.join(r"E:\Mytools.main\Mytools\photos\\Mytree\imgaes")
        # os.mkdir(image_path)
        self.headers = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1 Edg/98.0.4758.102"
        }
        self.response = requests.get(self.url)
        self.my_re = re.compile(r'contentId:".*?",title:"(?P<city_name>.*?)",key:"(?P<city_name_en>.*?)",home:', re.S)
        # print('[\n', end='')
        self.num = 0
        self.l = {}

    def mian(self):
        for it in self.my_re.finditer(self.response.text):
            new_image_path = os.path.join(self.image_path, it.group("city_name"))  # 获取蒙德，璃月，稻妻文件夹路径
            try:
                os.mkdir(new_image_path)  # 根据文件夹路径，创建对应文件
            except:
                pass
            # 通过f''字符串，得到各个城市角色链接
            # print(it.group("city_name_en"))
            new_url = f'https://ys.mihoyo.com/main/character/{it.group("city_name_en")}?char=0'
            # 对new_url进行请求，得到role_response, 并设置编码格式，未来拿取到各个国家角色的中文名称
            role_response = requests.get(new_url)
            role_response.encoding = "utf-8"
            new_my_re = re.compile(r'{title:"(?P<name>.*?)",icon.*?cover1:"(?P<pic_url>.*?)",cover2:', re.S)
            for it1 in new_my_re.finditer(role_response.text.replace(r"\u002F", r"/")):
                self.num += 1
                # print(f'   "{it1.group("name")}":"{it.group("city_name_en")}",\n', end='')
                # 得到全身图链接
                pic_response = requests.get(it1.group("pic_url"), headers=self.headers)
                # 得到下载图片路径
                pic_path = os.path.join(new_image_path, it1.group("name") + ".png")
                # 写入文件
                with open(pic_path, "wb") as f:
                    self.l = Tree(self.l, pic_response.url, pic_path, it1.group("name")).main()
                    f.write(pic_response.content)
        with open(f"Mytree/js2/main.json", "w") as summ:
            summ.write(json.dumps([self.l]))
        return json.dumps([self.l])


def read():
    with open(f"Mytree/js2/main.json", "r") as summ:
        return summ.read()


def write_json(jsonbag):
    with open(f"Mytree/js2/mhy.json", "w") as summ:
        summ.write(jsonbag)
    return 0



def main():
    bag = os.path.exists(f"Mytree/js2/main.json")
    if bag is True:
        with open(f"Mytree/js2/main.json", "r") as summ:
            bag = summ.read()
        a = json.loads(bag)
    elif bag is not True:
        print("检查到资源未下载,正在下载中...")
        a = json.loads(Whire().mian())
    while True:
        n = input(">>>")
        name = n
        main = a[0][n]
        print(f"人物:{name}\n网络地址:{main['网络地址']}\n本地地址:{main['本地地址']}")
        try:
            __json = mhy.lookup(name=name)
        except KeyError:
            print("角色最新消息未更新")
if __name__ == '__main__':
    """try:
        a = read()
        a = json.loads(a)
        try:
            with open(f"Mytree/js2/mhy.json", "r") as summ:
                 json_bag = summ.read()
        except FileNotFoundError:
            print("角色最新消息未更新")
            pass
        while True:
            n = input(">>>")
            name = n
            main = a[0][n]
            print(f"人物:{name}\n网络地址:{main['网络地址']}\n本地地址:{main['本地地址']}")
            lookup(json_bag, name)
    except:"""
    main()

