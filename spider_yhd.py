import requests
from lxml import html

def spider(sn, book_list=[]):
    """爬取一号店数据"""
    #获取URL地址
    url = 'https://search.yhd.com/c0-0/k{sn}/'.format(sn=sn)
    #获取HTML内容
    html_neirong = requests.get(url)
    #获取XPATH对象
    neirong = html.fromstring(html_neirong.text)
    #找到商品列表
    ul_list = neirong.xpath('//div[@id="itemSearchList"]/div')
    for li in ul_list:
        #标题

        title = li.xpath('div//p[@class="proName clearfix"]/a/@title')
        print(title[0])
        #链接
        link = li.xpath('div//p[@class="proName clearfix"]/a/@href')
        print(link[0])
        #价格
        price = li.xpath('div//p[@class="proPrice"]/em/@yhdprice')
        print(price[0])
        #商家
        shangjia = li.xpath('div//p[@class="storeName limit_width"]/a/@title')
        print(shangjia[0])

        book_list.append({
            'title': title[0],
            'price': price[0],
            'link': link[0],
            'store': shangjia[0]
        })



if __name__ == '__main__':
    spider(sn)