from urllib import request
from urllib import parse
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import http.cookiejar

#post 提交
def post(url,values):
    data = parse.urlencode(values).encode('utf-8')  # 提交类型不能为str，需要为byte类型
    request1 = request.Request(url, data)
    response = urlopen(request1)
    return response.read().decode()
#get 提交
def get(url,values):
    data = parse.urlencode(values)
    geturl = url + "?" + data
    request1 = request.Request(geturl)
    response = urlopen(request1)
    return response.read().decode()

'''
values = {'username': '962457839@qq.com', 'password': 'XXXX'}
data = parse.urlencode(values).encode('utf-8')  # 提交类型不能为str，需要为byte类型
url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
request = request.Request(url, data)
response = urlopen(request)
print(response.read().decode())#post 提交

values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
data = parse.urlencode(values).encode('utf-8')
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = request.Request(url,data)
response = urlopen(request)
print(response.read().decode())

#get 提交
values={}
values['username'] = "1016903103@qq.com"
values['password']="XXXX"
data = parse.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
request = request.Request(geturl)
response = urlopen(request)
print(response.read().decode())

#设置Headers
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
data = parse.urlencode(values).encode('utf-8')
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = request.Request(url,data,headers,10)#10=(timeout=10)
response = urlopen(request)
print(response.read().decode())
#代理
proxy_support = request.ProxyHandler({'sock5': 'localhost:1080'})
opener = request.build_opener(proxy_support)
request.install_opener(opener)
a = request.urlopen("http://www.111cn.net ").read().decode("utf8")
print(a)

#http认证
# create a password manager
password_mgr = request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.

# If we knew the realm, we could use it instead of None.

top_level_url = "https://www.python.org/"

password_mgr.add_password(None, top_level_url, 'rekfan', 'xxxxxx')

handler = request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)

opener =request.build_opener(handler)
# use the opener to fetch a URL

a_url = "https://www.python.org/"

x = opener.open(a_url)

print(x.read())
 # Install the opener.

# Now all calls to urllib.request.urlopen use our opener.
request.install_opener(opener)
a = urlopen(a_url).read().decode('utf8')
print(a)

#异常1
req = request.Request('http://www.python.org/')
try:
   response = urlopen(req)
except HTTPError as e:
      print("The (www.python.org)server couldn't fulfill the request.")
      print('Error code: ', e.code)
except URLError as e:
      print('We failed to reach a server.')
      print('Reason: ', e.reason)
else:
     print("good!")
     print(response.read().decode("utf8"))
#异常2
req = request.Request("http://www.python.org/")
try:
   response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
         print('We failed to reach a server.')
         print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
         print("The server couldn't fulfill the request.")
         print('Error code: ', e.code)
else:
    print("good!")
    print(response.read().decode("utf8"))


'''
