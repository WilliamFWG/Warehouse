import requests
import json

if __name__ == '__main__':
    url='http://192.168.1.100/php/api_jsonrpc.php'
    header={'Content-Type':'application/json-rpc'}
    # data={
    #     "jsonrpc": "2.0",
    #     "method": "user.login",
    #     "params": {
    #         "user": "Admin",
    #         "password": "zabbix"
    #     },
    #     "id": 1,
    #     "auth": None
    # }
    data={
        "jsonrpc": "2.0",
        "method": "host.create",
        "params": {
            "host": "Linux server",
            "interfaces": [
                {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": "192.168.1.1",
                    "dns": "",
                    "port": "10050"
                }
            ],
            "groups": [
                {
                    "groupid": "50"
                }
            ],
            "templates": [
                {
                    "templateid": "20045"
                }
            ],
            "inventory_mode": 0,
            "inventory": {
                "macaddress_a": "01234",
                "macaddress_b": "56768"
            }
        },
        "auth": "0940930566ff5d217abb594883d92f84",
        "id": 1
    }
    r=requests.post(url,data=json.dumps(data),headers=header)
    print(r.json())