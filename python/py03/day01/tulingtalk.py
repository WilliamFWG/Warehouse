
import requests
import json

def tuling_reply(url, apikey, msg):
    data = {     # 这个是在帮助手册上直接复制过来的
        "reqType":0,
        "perception": {
            "inputText": {
                "text": msg
            },
            "selfInfo": {
                "location": {
                    "city": "上海",
                    "province": "上海",
                    "street": "三泉路"
                }
            }
        },
        "userInfo": {
            "apiKey": apikey,      # 你注册的apikey
            "userId": "26464323"      # 随便填点
        }
    }
    headers = {'content-type': 'application/json'}     # 必须是json
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()

if __name__ == '__main__':
    apikey = ''  #图令机器人网站上得到的apikey
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    while True:
        try:
            msg = input('(输入quit结束)> ').strip()
        except UnicodeDecodeError as e:
            print(e)
            continue
        else:
            if not msg:
                continue
            if msg == 'quit':
                break
            reply = tuling_reply(url, apikey, msg)
            print(reply["results"][0]["values"]["text"])    # 可以直接打印reply






































