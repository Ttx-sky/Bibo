import os

import requests
from bs4 import BeautifulSoup as be
import json
md_url = "https://ys.mihoyo.com/content/ysCn/getContentList?pageSize=20&pageNum=1&order=asc&channelId=150"
ly_url = "https://ys.mihoyo.com/content/ysCn/getContentList?pageSize=20&pageNum=1&order=asc&channelId=151"
dq_url = "https://ys.mihoyo.com/content/ysCn/getContentList?pageSize=20&pageNum=1&order=asc&channelId=324"


"""
The mhy.py has a problem.
It can not complete automatic discovery of new data.
If new data is found, delete mhy. JSON, mhy.py gets the new data and stores it on the second boot.

Welcome to q.w.e.a.s@icloud.com
"""


def get_json(_url_):
    req = requests.get(url=_url_)
    if req.status_code == 200:
        return req.json()['data']
    else:
        return None


def clean_data(_data_):
    _return_ = []
    for key in _data_['list']:
        ext = key["ext"]
        data = {key['title']: {
            "角色ICON": ext[0]["value"][0]["url"],
            "电脑端立绘": ext[1]["value"][0]["url"],
            "手机端立绘": ext[15]["value"][0]["url"],
            "角色名字": key['title'],
            "角色属性": ext[3]["value"][0]["url"],
            "角色语言": ext[4]["value"],
            "声优1": ext[5]["value"],
            "声优2": ext[6]["value"],
            "简介": be(ext[7]["value"], "lxml").p.text.strip(),
            "台词": ext[8]["value"][0]["url"],
            "音频": {
                ext[9]["value"][0]["name"]: ext[9]["value"][0]["url"],
                ext[10]["value"][0]["name"]: ext[10]["value"][0]["url"],
                ext[11]["value"][0]["name"]: ext[11]["value"][0]["url"],
                ext[12]["value"][0]["name"]: ext[12]["value"][0]["url"],
                ext[13]["value"][0]["name"]: ext[13]["value"][0]["url"],
                ext[14]["value"][0]["name"]: ext[14]["value"][0]["url"],
            },
        }
        }
        _return_.append(data[key['title']])
    return _return_


def data():
    _json_ = {}
    for url in [md_url, ly_url, dq_url]:
        jsonlist = clean_data(get_json(url))
        for json in jsonlist:
            _json_[json['角色名字']] = json
    return _json_


def lookup(name):
    global a
    a = []
    bag = os.path.exists(f"Mytree/js2/mhy.json")
    if bag is True:
        with open(f"Mytree/js2/mhy.json", "r") as summ:
            bag = summ.read()
        a = json.loads(bag)[0]
        # print(a) -> mhy.json
        __json = a[name]

    elif bag is not True:
        # print("检查到资源未下载,正在下载中...")
        __json = data()[name]
    # print("查找角色：", name)
    for key, value in __json.items():
        if key == "音频":
            for keys, values in __json[key].items():
                print(f"{keys}：{values}")
        else:
            print(f"{key}：{value}")
    with open(f"Mytree/js2/mhy.json", "w") as summ:
        summ.write(json.dumps([data()]))


class ys:
    # name = input('查询角色：')
    def lookup(name):
        json = data()[name]
        print("查找角色：", name)
        for key, value in json.items():
            if key == "音频":
                for keys, values in json[key].items():
                    print(f"{keys}：{values}")
            else:
                print(f"{key}：{value}")

