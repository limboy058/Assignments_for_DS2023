import requests, random as rd, csv
from lxml import etree

import re


IP_list = [
    '81.70.187.80:8080', '43.153.41.35:3128', '43.153.52.223:3128',
    '43.157.8.79:8888', '43.156.236.69:3128'
]


def get_time(url):
    head = {
        "User-Agent":
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edge/90.0.818.66'
    }
    proxie = {'http://': rd.choice(IP_list)}
    html = requests.get(url, headers=head, proxies=proxie)
    ret = re.findall(r'"timelength":(\d+),', html.text)[0][:-3]
    return ret


if __name__ == "__main__":
    print(get_time('https://b23.tv/BV12H4y1q7bx'))
