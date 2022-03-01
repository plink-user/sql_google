import requests
from lxml import etree
import time
import sys
import base64
proxies = {
   'http': ''
}
headers={
        'Host': 'www.google.com.hk',
        'Connection': 'close',
        'Cache-Control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'X-Client-Data': 'CIm2yQEIo7bJAQjBtskBCKmdygEI+MfKAQiR28oBCNGaywEI3fLLAQiU9csB',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'CGIC=IocBdGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2UvYXZpZixpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIzO3E9MC45; OTZ=5982609_24_24__24_; 1P_JAR=2021-06-08-15; NID=216=lVLlhzfbZuohnzKrsHH0QykSFF4ct6DCe1Cxk1sfLPW5Z43G-3cDXjC2iSDjDed9BeRAM5qDUMlCnhtAjQrKCu1rRxm3LJEHIYgowVOj9NMzZ3-BxTihfyrKCXwWzGKglMdbq12Oa0fq5rT9CwPxT7MO1buspatuxm5RzKU5y3HzRzeq8TpXhnYE7Q; DV=g5SylvR6FOUs4OgbEydFW6hJAH_FnpeKpsw9cz05QgMAAAA'
    }

shuju="inurl:php?id="
data="/search?q="+shuju+"&newwindow=1&safe=strict&hl=zh-CN&as_qdr=all&tbs=ctr:countryCN&ei=N5O_YNfVNNLq-gSg9JuABA&start="
for yeshu in range(0, 30):
    page=10*yeshu
    print('正在提取第'+str(yeshu+1)+'页\n')
    url='https://www.google.com.hk/'+data+str(page)+'&sa=N&ved=2ahUKEwjQp6iX5fvwAhXL6J4KHeBFAwo4ChDy0wN6BAgBEDU&biw=1366&bih=241'
    print(url)
    try:
        result=requests.get(url, headers=headers, proxies=proxies).content
        #print(result.decode('utf-8'))
        soup =etree.HTML(result)
        ip_data = soup.xpath('//div[@class="yuRUbf"]/a/@href')
        ip_data='\n'.join(ip_data)
        print(ip_data)
        with open(r'ip.txt','a+') as f:
            f.write(ip_data+'\n')
            f.close()
    except Exception as f:
        print(f)
        time.sleep(0.5)
