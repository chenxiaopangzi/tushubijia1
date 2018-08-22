import requests
from lxml import html


def spider(sn, book_list = []):
    """爬取京东数据"""
    #获取url
    url = 'https://search.jd.com/Search?keyword={sn}'.format(sn=sn)
    #获取HTML内容
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    html_neirong = resp.text
    #xpath对象
    neirong = html.fromstring(html_neirong)
    #找到书的列表
    ul_list = neirong.xpath('//ul[@class="gl-warp clearfix"]/li')


    for li in ul_list:
        #获取标题
        title = li.xpath('div/div[@class="p-name"]/a/em/text()')
        print(title[0])
        #获取购买链接
        link = li.xpath('div/div[@class="p-name"]/a/@href')
        print(link[0])
        #获取价格
        price = li.xpath('div/div[@class="p-price"]/strong/i/text()')
        print(price[0])
        #获取商家
        shangjia = li.xpath('div/div[@class="p-shopnum"]/a/@title')
        print(shangjia[0])

        book_list.append({
            'title': title[0],
            'price': price[0],
            'link': link[0],
            'store': shangjia[0]
        })

if __name__ == '__main__':

    spider(sn)