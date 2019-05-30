import requests
import re

# 招聘信息
url1 = 'http://job.hust.edu.cn/searchJob.jspx?type=2&fbsj='

# 实习信息
url2 = 'http://job.hust.edu.cn/searchJob.jspx?type=4&fbsj='

# 招聘会信息
url3 = 'http://job.hust.edu.cn/searchJob.jspx?type=0&fbsj=0'

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}

res1 = requests.get(url1,headers)
res2 = requests.get(url2,headers)
res3 = requests.get(url3,headers)

content_li1 = re.findall("<a href=(.*)</a><br>",res1.text)[4:-1]
time_li = re.findall('<td width="120" valign="top">(.*)</td>',res1.text)[4:]
print('今日招聘信息：')
print('*'*30)
for n,i in enumerate(content_li1):
    name = re.findall('title="(.*?)"',i)[0]
    url = 'http://job.hust.edu.cn/'+re.findall('"/(.*?)"',i)[0]
    time = time_li[n]
    print(time+'_'+name+':'+url)
print('*'*30)


content_li2 = re.findall("<a href=(.*)</a><br>",res2.text)[:-1]
time_li = re.findall('<td width="120" valign="top">(.*)</td>',res2.text)
print('今日实习信息：')
print('*'*30)
for n,i in enumerate(content_li2):
    name = re.findall('title="(.*?)"',i)[0]
    url = 'http://job.hust.edu.cn/'+re.findall('"/(.*?)"',i)[0]
    time = time_li[n]
    print(time+'_'+name+':'+url)
print('*'*30)

content_li3 = re.findall("<a href=(.*)class=''>",res3.text)
time_place_li = re.findall("<td><span>(.*)</span>",res3.text)
print('今日招聘会信息：')
print('*'*30)
for n,i in enumerate(content_li3):
    name = re.findall('title="(.*?)"',i)[0]
    url = 'http://job.hust.edu.cn/'+re.findall('"/(.*?)"',i)[0]
    time = time_place_li[3*n]
    place = time_place_li[3*n+1]
    print('['+time+']'+',['+place+'],'+name+':'+url)
print('*'*30)

quit = input('按回车退出')
