import requests, random as rd, csv,re
from lxml import etree

f1 = open(f"final\B站每周必看2023_data_tmp.csv", mode="w", encoding='utf-8-sig', newline='')
f2 = open(f"final\B站每周必看2023_label_tmp.csv", mode="w", encoding='utf-8-sig', newline='')
csvwrite1 = csv.writer(f1)
csvwrite2 = csv.writer(f2)

csvwrite1.writerow(['title','bvid','link','up','play','bulletchat','reply','like','coin','favorite','share','labels','length'])
csvwrite2.writerow(['labels'])


IP_list = [
    '103.152.132.29:3128', '103.46.8.46:8080', '43.163.195.38:3128',
    '43.153.52.223:3128'
]


def get_time_and_label(link: str,proxie):
    head = {
        "User-Agent":
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edge/90.0.818.66'
    }
    html = requests.get(link, headers=head,proxies=proxie)
    ret = 0
    try:
        ret = re.findall(r'"timelength":(\d+),', html.text)[0][:-3]
    except:
        ret = 0
    selector = etree.HTML(html.text)
    data = selector.xpath(
        "/html/body/div[2]/div[2]/div[1]/div[4]/div[2]/div//*")
    labellist = []
    for item in data:
        if item.text != None:
            labellist.append(item.text)
    return [labellist, ret]


def get_data(url):
    head = {
        "User-Agent":
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edge/90.0.818.66'
    }
    proxie = {'http://': rd.choice(IP_list)}
    html = requests.get(url, headers=head)
    htmljs = html.json()
    htmllist = htmljs['data']['list']
    print("使用ip:" + str(proxie['http://']))
    for video in htmllist:
        tmp = get_time_and_label(video['short_link_v2'],proxie)
        video_info = {
            'title': video['title'],
            'bvid': video['bvid'],
            'link': video['short_link_v2'],
            'up': video['owner']['name'],
            'view': video['stat']['view'],
            'bulletchat': video['stat']['danmaku'],
            'reply': video['stat']['reply'],
            'like': video['stat']['like'],
            'coin': video['stat']['coin'],
            'favorite': video['stat']['favorite'],
            'share': video['stat']['share'],
            'labels': tmp[0],
            'length': tmp[1]
        }
        csvwrite1.writerow(video_info.values())
        for item in video_info['labels']:
            csvwrite2.writerow([item])
        print('爬取:\t\t'+video['title']+"\t\t成功")


if __name__ == "__main__":
    urls = [
        "https://api.bilibili.com/x/web-interface/popular/series/one?number={}"
        .format(str(i)) for i in range(244, 197, -1)
    ]
    for url in urls:
        print("爬取" + url + "中......")
        get_data(url)
        print("爬取" + url + "完毕")
        print()
    f1.close()
    f2.close()
