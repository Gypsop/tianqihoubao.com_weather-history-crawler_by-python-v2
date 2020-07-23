# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests, time
import numpy as np
from fake_useragent import UserAgent
import random
import time

ua = UserAgent()


f = open("output.txt","w")
log = open("log.txt", "a")

url_file = open("link_county.txt", "r", 1, 'gbk').read().split("\n")

years = ['2011','2012','2013','2014','2015','2016','2017','2018','2019']
months = ['01','02','03','04','05','06','07','08','09','10','11','12']

def gethtml(url):
    i = 0
    while i < 10:
        try:
            response = requests.get(url, headers = {'User-Agent': ua.random}, timeout = 20)
            return response
        except requests.exceptions.RequestException:
            i += 1
            print(url + "超时，即将在休息之后进行第" + str(i) + "次尝试…\n")
            log.write(str(time.strftime('%Y-%m-%d %H:%M:%S')) + " [FAIL] " + url + "失败，即将重试！次数：" + str(i) + "\n")
            log.flush()
            for j in range(50):
                print("休息中，" + str(j + 1) + "/" + str(50) + "…")
                time.sleep(1)
    while 1:
        try:
            response = requests.get(url, headers = {'User-Agent': ua.random}, timeout = 20)
            return response
        except requests.exceptions.RequestException:
            i += 1
            print(url + "超时，即将在休息之后进行第" + str(i) + "次尝试…\n")
            log.write(str(time.strftime('%Y-%m-%d %H:%M:%S')) + " [FAIL] " + url + "失败，即将重试！次数：" + str(i) + "\n")
            log.flush()
            for j in range(10 * i):
                print("休息中，" + str(j + 1) + "/" + str(10 * i) + "…")
                time.sleep(1)

def spider(cityname, url2):
    response = gethtml(url2)
    response.encoding = "GB2312"
    soup = BeautifulSoup(response.text, 'lxml')
    trs = soup.find_all('tr')
    dates = soup.select('td > a')
    del(trs[0])
    for tr0, date0 in zip(trs, dates):
        print(cityname + "||" + date0.get_text().strip().replace(" ", "").replace("\t", "").replace("\r\n", ""), end = "|")
        f.write(str(cityname + "||" + date0.get_text().strip().replace(" ", "").replace("\t", "").replace("\r\n", "") + "|"))
        for td0 in tr0:
            print(str(td0.string).strip().replace(" ", "").replace("\t", "").replace("\r\n", ""), end = "|")
            f.write(str(str(td0.string).strip().replace(" ", "").replace("\t", "").replace("\r\n", "") + "|"))
        print("")
        f.write("\n")
        f.flush() # 把之前在缓存中等待写入文件的内容立刻落盘

for county_url in url_file:
    for year in years:
        for month in months:
            print(str(time.strftime('%Y-%m-%d %H:%M:%S')) + "\n" + "当前开始url：" + county_url.split(",")[1].replace(".html", "") + "/month/" + year + month + ".html")
            log.write(str(time.strftime('%Y-%m-%d %H:%M:%S')) +" [START] " + "当前开始url：" + county_url.split(",")[1].replace(".html", "") + "/month/" + year + month + ".html" + "\n")
            log.flush()
            spider(county_url.split(",")[0], county_url.split(",")[1].replace(".html", "") + "/month/" + year + month + ".html") 
            print("刚才完成的url：" + county_url.split(",")[1].replace(".html", "") + "/month/" + year + month + ".html")
            log.write(str(time.strftime('%Y-%m-%d %H:%M:%S')) +" [SUCCESS] " + "刚才完成的url：" + county_url.split(",")[1].replace(".html", "") + "/month/" + year + month + ".html" + "\n")
            log.flush()
            for i in range(40):
                print("休息中，" + str(i + 1) + "…")
                time.sleep(1)
                
log.close()
f.close()