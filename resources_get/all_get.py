#养生加心理健康问答爬虫（暂存在列表里，方便之后存入excel）
import requests
from bs4 import BeautifulSoup
import re
import time     #避免不够数目的返回

url_all = []
#所有网址
name_all = []
#所有名字
content_all = []
#所有内容

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}

def get_all(url_list):
#所有网址以列表形式存放后，添加名字和内容
    for w in range(len(url_list)):
        url = url_all[w]
        sc = requests.get(url,headers)
        sc.encoding = 'gbk'
        #根据网址选择编码格式
        soup = BeautifulSoup(sc.text,'lxml')
        #规整化处理标签
        get_td = BeautifulSoup(str(soup.td),'html.parser').get_text()
        #去标签
        getd = re.findall('(.*?)',get_td)
        #去除多余部分
        gets = ''
        for i in getd:
            i = re.sub('\s','',i)
            gets += i
        content_all.append(gets)
        #加进去内容
        name = re.findall('<h1>(.*?)</h1>',sc.text,re.S)
        p = ''
        for k in name[0]:
            if k != '\r' and k != '\n':
                p += k
        name_all.append(p)
        #加进去名字
        print(w + 1)
        time.sleep(0.5)

def get_url(question):
#得到所有的网址
    k = 0
    for i in range(1,46):
        url = 'https://ks.pclady.com.cn/lady_cms.shtml?q=' + question + str(i)
        content = requests.get(url,headers)
        content.encoding = 'gbk'
        first = re.findall('<i class="i-pic"><a href="(.*?)" title',content.text,re.S)
        for j in range(len(first)):
            url = 'https:' + first[j]
            url_all.append(url)
            time.sleep(0.5)
            k += 1
            print(k)

def all_main():
#养生知识爬虫的总函数
    get_url('%D1%F8%C9%FA&clusterCategory=%BD%A1%BF%B5&pageNo=')
    print('养生网站爬取完成')
    print('*********************')
    get_url('%D0%C4%C0%ED%BD%A1%BF%B5&clusterCategory=%BD%A1%BF%B5&pageNo=')
    print('心里健康网站爬取完成,即将进入具体爬取阶段')
    print('*********************')
    get_all(url_all)
    print('全部爬取完成')
    print('*********************')
    return name_all,content_all
