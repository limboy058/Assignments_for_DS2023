import requests, random as rd, csv
from lxml import etree

f1 = open(f"final\B站每周必看2023按周流量.csv", mode="w", encoding='utf-8-sig', newline='')
csvwrite1 = csv.writer(f1)

csvwrite1.writerow(['index','sum','max_cnt','max_title'])

IP_list = [
    '81.70.187.80:8080', '43.153.41.35:3128', '43.153.52.223:3128',
    '43.157.8.79:8888', '43.156.236.69:3128'
]

def get_data(url):
    head = {
        "User-Agent":
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edge/90.0.818.66'
    }
    proxie = {'http://': rd.choice(IP_list)}
    html = requests.get(url, headers=head, proxies=proxie)
    htmljs = html.json()
    htmllist = htmljs['data']['list']
    sum=0
    ma=0
    ma_title=""
    for video in htmllist:
        if ma<int(video['stat']['view']):
            ma=int(video['stat']['view'])
            ma_title=video['title']
        sum+=int(video['stat']['view'])
    
    csvwrite1.writerow([url[-3:],sum,ma,ma_title])


if __name__ == "__main__":
    urls = [
        "https://api.bilibili.com/x/web-interface/popular/series/one?number={}"
        .format(str(i)) for i in range(244, 197, -1)
    ]
    for url in urls:
        print("爬取"+url+"中......",end='')
        get_data(url)
        print("成功")
    f1.close()
