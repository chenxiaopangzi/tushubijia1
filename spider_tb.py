import requests
from lxml import html
import json


def spider(sn, book_list=[]):
    """抓取淘宝数据"""
    #获取URL
    url = 'https://s.taobao.com/api?&ajax=true&m=customized&q={sn}'.format(sn=sn)

    #获取HTML内容
    html_neirong = requests.get(url).json()
    #xpath对象
    neirong = html_neirong["API.CustomizedApi"]["itemlist"]["auctions"]

    #找到出售列表
    for li in neirong:
        title = li['raw_title']
        print('\n' + title)
        link = li['detail_url']
        print(link.replace('//', 'https://'))
        price = li['view_price']
        print(price)
        shangjia = li['nick']
        print(shangjia)

        book_list.append({
            'title': title,
            'price': price,
            'link': link,
            'store': shangjia
        })


if __name__ =='__main__':
    spider(sn)