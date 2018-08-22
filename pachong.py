from lxml import html
def parse():
    #读取文件内容
    f = open('./static/index.html', 'r', encoding='utf-8')
    s = f.read()
    neirong = html.fromstring(s)
    #解析H3标题
    h3 = neirong.xpath('/html/body/h3/text()')
    print(h3[0])
    #解析UL下面的内容
    ul = neirong.xpath('/html/body/ul/li')
    for li in ul:
        print(li.xpath('text()')[0])
    #解析ul下指定的元素值
    li3 = neirong.xpath('/html/body/ul/li[@class="important"]/text()')
    print(li3[0])
    #解析a标签下的内容
    #a = neirong.xpath('/html/body/div[@id="container"]/a')

    #print(a[0].xpath('text()')[0])
    #print(a[0].xpath('@href')[0])
    a = neirong.xpath('/html/body/div[@id="container"]/a/text()')
    print(a[0])
    href = neirong.xpath('/html/body/div[@id="container"]/a/@href')
    print(href[0])
    #解析P标签
    p = neirong.xpath('/html/body/p[last()]/text()')
    print(p[0])


    f.close()
if __name__ == '__main__':
    parse()