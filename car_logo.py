# -*-coding:utf-8 -*-

#urllib模块提供了读取Web页面数据的接口
import urllib2,urllib,random

from bs4 import BeautifulSoup


headers=[
            'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
            'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)',
            'Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50',
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)'
    ]
start_URL='http://www.chebiaow.com'

def getEachPage(url):
    


    request=urllib2.Request(url, headers={"User-Agent":random.choice(headers)})

    number_html=urllib2.urlopen(request).read()

    soup=BeautifulSoup(number_html,"lxml")

    page_number=soup.find('div',{'class':'mainnavshow'}).find('div',{'class':'right'})

    #print 'page_number',page_number

    if page_number is not None:

        for link in page_number.find_all('a'):
            #print link.get('href')
            page_link=link.get('href')

            getSoup(page_link)




        



def getSoup(p_link):

    header={
        "User-Agent":random.choice(headers)
    }

    page_url=start_URL+p_link

    print 'url',page_url

    req=urllib2.Request(page_url, headers=header)
    html=urllib2.urlopen(req).read()
    soup=BeautifulSoup(html)

    getContent(soup)


def getContent(b_soup):

    ul=b_soup.find('div',{'class':'zxsf'}).find('ul')

    for img in ul.find_all('img'):
        print 'src===>',img.get('src')
        print 'title===>',img.get('alt')

        getImg(img.get('src'),img.get('alt'))

#下载图片并重命名
def getImg(imgUrl,imgName):
    urllib.urlretrieve(start_URL+imgUrl,'/Users/longjiang/Desktop/Logo/%s.jpg' % imgName)

def main():
    getEachPage(start_URL)

if __name__ == '__main__':
    main()




