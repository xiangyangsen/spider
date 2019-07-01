import requests
import json
import time
from bs4 import BeautifulSoup
import csv


url = 'http://www.woshipm.com/__api/v1/stream-list/page/'
header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
               'Cache-Control': 'max-age=0',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
               'Connection': 'keep-alive',
               'Host': 'www.woshipm.com',
               'Cookie' : 't=MHpOYzlnMmp6dkFJTEVmS3pDeldrSWRTazlBOXpkRjBzRXpZOU4yVkNZWWl5QVhMVXBjMU5WcnpwQ2NCQS90ZkVsZ3lTU2Z0T3puVVZFWFRFOXR1TnVrbUV2UFlsQWxuemY4NG1wWFRYMENVdDRPQ1psK0NFZGJDZ0lsN3BQZmo%3D; s=Njg4NDkxLCwxNTQyMTk0MTEzMDI5LCxodHRwczovL3N0YXRpYy53b3NoaXBtLmNvbS9XWF9VXzIwMTgwNV8yMDE4MDUyMjE2MTcxN180OTQ0LmpwZz9pbWFnZVZpZXcyLzIvdy84MCwsJUU1JUE0JUE3JUU4JTk5JUJF; Hm_lvt_b85cbcc76e92e3fd79be8f2fed0f504f=1547467553,1547544101,1547874937,1547952696; Hm_lpvt_b85cbcc76e92e3fd79be8f2fed0f504f=1547953708'
               }


def get_garp(url):
    # mark ="'"
    # new_url = mark+url+mark
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    art = soup.find(class_="grap").get_text().strip()
    time.sleep(1)
    return art

with open(r'/Users/flu/Downloads/woshipm1.csv', 'w', encoding='utf-8',newline='') as csvfile:
    fieldnames = ['article_id', 'title', 'author', 'author_id', 'permalink', 'view', 'like', 'bookmark','date', 'garp']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for page_num in range(1,10):

        page_url = 'http://www.woshipm.com/__api/v1/stream-list/page/{}'.format(page_num)
        print('正在抓取第'+str(page_num)+'页')
        resp = requests.get(page_url,headers=header)
        print(resp)
        print(resp.text)
        pydata = json.loads(resp.text)
        print(pydata)

        article = pydata['payload']

        print(article)
        print(type(article[0]))
        print(type(pydata))

        for n in article:
            article_id = n['id']
            title = n['title']
            author = n['author']['name']
            author_id = n['author']['id']
            permalink = n['permalink']
            view = n['view']
            like = n['like']
            bookmark =n['bookmark']
            date = n['date']
            garp = get_garp(permalink)

            print(article_id,'|',title,'|',permalink,'|',like,'|',view,'|',bookmark,'|',author,'|',author_id,'|',date,'|',garp)
            writer.writerow({'article_id': article_id, 'title': title, 'author': author, 'author_id': author_id, 'permalink': permalink,
                             'view': view, 'like': like, 'bookmark': bookmark, 'date': date,
                             'garp': garp})


        time.sleep(2)

