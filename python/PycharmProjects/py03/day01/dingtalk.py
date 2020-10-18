import json
import requests

if __name__ == '__main__':
    url='https://oapi.dingtalk.com/robot/send?access_token=e88a5dfb80118f073ddae0534d9daa4ea0d5049917d7768b12753e2e9ef649c3'
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    # data={
    #     "msgtype": "text",
    #     "text": {
    #         "content": "通知：测试钉钉机器人，你好，你好，我是Joe"   #文本内容
    #     },
    #     "at": {
    #         "atMobiles": [           #@谁，填入手机号
    #             "156xxxx8827",
    #             "189xxxx8325"
    #         ],
    #         "isAtAll": False   #是否@所有人
    #     }
    # }

    # data={
    #     "msgtype": "link",
    #     "link": {
    #         "text": "通知：这个即将发布的新版本，创始人xx称它为红树林。而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是红树林",
    #         "title": "时代的火车向前开",
    #         "picUrl": "https://img03.sogoucdn.com/app/a/07/f13b5c3830f02b6db698a2ae43ff6a67",
    #         "messageUrl": "https://www.dingtalk.com/s?__biz=MzA4NjMwMTA2Ng==&mid=2650316842&idx=1&sn=60da3ea2b29f1dcc43a7c8e4a7c97a16&scene=2&srcid=09189AnRJEdIiWVaKltFzNTw&from=timeline&isappinstalled=0&key=&ascene=2&uin=&devicetype=android-23&version=26031933&nettype=WIFI"
    #     }
    # }


    data={
         "msgtype": "markdown",
         "markdown": {
             "title":"通知：杭州天气",
             "text": "#### 杭州天气 @150XXXXXXXX \n> 9度，西北风1级，空气良89，相对温度73%\n> ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)\n> ###### 10点20分发布 [天气](https://www.dingtalk.com) \n"
         },
          "at": {
              "atMobiles": [
                  "150XXXXXXXX"
              ],
              "isAtAll": False
          }
    }

    r=requests.post(url,data=json.dumps(data),headers=headers)     #data参数要求一定要是json格式
    print(r.json())