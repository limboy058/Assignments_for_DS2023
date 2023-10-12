import pymssql, requests
from lxml import etree


def get_data(url):
    head = {
        "User-Agent":
        "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }
    html = requests.get(url, headers=head)
    selector = etree.HTML(html.text)
    infos = selector.xpath(
        "/html/body/div[3]/div[1]/div/div[1]/ol/li[*]/div/div[2]/div[1]/a")
    res = []
    for info in infos:
        s = []
        err = ""
        for sp in info.xpath("./span"):
            tmp = sp.xpath(".//text()")[0].replace(u"\xa0", '')
            tmp = tmp.replace('\'', '\'\'')
            s.append(tmp.replace('/', ''))
        res.append(s)
    return res


def push_to_sql(datas: list):
    for data in datas:
        l = len(data)
        if l == 3:
            sql_command = "insert into test.dbo.douban_top_movies(title,normal_title,others) values(N'%s',N'%s','%s')" % (
                data[0], data[1], data[2])
        elif l == 2:
            sql_command = "insert into test.dbo.douban_top_movies(title,normal_title) values(N'%s',N'%s')" % (
                data[0], data[1])
        cursor.execute(sql_command)
    conn.commit()


def main():
    urls = [
        "https://movie.douban.com/top250?start={}&filter=".format(str(i))
        for i in range(0, 250, 25)
    ]
    global conn, cursor
    conn = pymssql.connect("(local)", "sa", "你的密码", "test")
    cursor = conn.cursor()
    for url in urls:
        datas = get_data(url)
        push_to_sql(datas)
    print("succeeded...")


if __name__ == "__main__":
    main()
