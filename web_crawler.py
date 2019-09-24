import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin
def func(list3, url):
    if url in list3:
        return
    r=requests.get(url)
    t=r.text
    parse = BeautifulSoup(t, 'html.parser')
    arr=[r.url]
    par = urlparse(url)
    dom=par.netloc
    
    for link in parse.find_all('a'):
        arr.append(link.get('href'))
    
    urls=[]
    for item in arr:
        urls.append((urljoin(url,item)))
    urls_withoutduplicates= list(set(urls))
    
    clean =[]
    
    for item in urls_withoutduplicates:
        q = urlparse(item)
        list1=q.netloc.split('.')
        list2=dom.split('.')
        new1=""
        new2=""
        for i in list1:
            if i==list1[0]:
                continue
            else:
               new1=new1+i
        for i in list2:
            if i==list2[0]:
                continue
            else:
               new2=new2+i
        if new1==new2:
            clean.append(item)
    
    
    for item in clean:
        for j in clean:
            if item == j+"/" or j==item +"/":
                clean.remove (item)
    decide=""
    print ("Scraped: ", url)
    list3.append(url)
    
    for item in clean:
            
            func (list3, item)
        
t ="https://www.syedfaaizhussain.com"
l=[]
func (l,t)

