import http.cookiejar
import urllib
import requests
def start():

    #这里填学号
	Num = "180628050405"

	payload = 'province=xxxxxx'   #这里填抓包获得的地址数据把抓到的数据粘贴到这

    #获取cookie

	urltwo = "https://fxgl.jx.edu.cn/4136012943/public/homeQd?loginName="+Num+"&loginType=0"

	#声明一个CookieJar对象实例来保存cookie
	cookie = http.cookiejar.CookieJar()
	#创建对象
	handler=urllib.request.HTTPCookieProcessor(cookie)
	#构建opener
	opener=urllib.request.build_opener(handler)
	#get访问保存cookie到cookiejar
	response=opener.open(urltwo)
	#标准格式打印
	cookieStr = ""
	for item in cookie:
		cookieStr = cookieStr + item.name + "=" +item.value + ";"
	print(cookieStr[:-1])
	#全局
	urllib.request.install_opener(opener)     
	#准备数据
	headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8','Cookie':cookieStr+"JSESSIONID=F558FDFD9BA3DC4AEB0912DF5AFF3C9D","Referer":"https://fxgl.jx.edu.cn/4136012943/user/qdbp","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"}
	url = "https://fxgl.jx.edu.cn/4136012943/studentQd/saveStu"
	rq = requests.request("POST",url=url,headers=headers,data=payload)
	re = requests.request("GET",url="https://fxgl.jx.edu.cn/4136012943/qdcg.html")
	#print(response.text.encode('utf-8'))
	SCKEY = ''        #Server酱 key 留空则不推送
	url_push = 'https://sc.ftqq.com/' + SCKEY + '.send?text=' + '打卡成功'   #返回结果推送到微信
	requests.get(url_push)

def main_handler(event, context):
    return start()


if __name__ == '__main__':
    start()
   
