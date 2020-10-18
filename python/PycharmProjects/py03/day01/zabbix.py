import requests
import json

if __name__ == '__main__':
    url='http://192.168.1.100/php/api_jsonrpc.php'
    header={"Content-Type":"application/json-rpc"}
    ###############################################################
    #查看非隐私信息不需要认证，可以直接获取
    # data={
    #     "jsonrpc": "2.0",           #zabbix 使用的协议， 固定值
    #     "method": "apiinfo.version",  #获取软件版本的方法
    #     "params": [],                   # 参数
    #     "id": 1                         #随便填个数字，表示作业号
    # }
    ##############################################################
    # data={
    #     "jsonrpc": "2.0",
    #     "method": "user.login",
    #     "params": {
    #         "user": "Admin",
    #         "password": "zabbix"
    #     },
    #     "id": 1
    # }
    #以上命令获取token=3a443223baeabedee93075bf244f3140

    ##############################################################
    #获取主机信息
    # data={
    #     "jsonrpc": "2.0",
    #     "method": "host.get",
    #     "params": {
    #         "output": "extend",
    #         "filter": {
    #             "host": [
    #                 # "Zabbix server",
    #                 # "Linux server"
    #             ]
    #         }
    #     },
    #     "auth": "3a443223baeabedee93075bf244f3140",
    #     "id": 1
    # }

    ##############################################################
    #删除主机  通过上述步骤可以获得主机id 进而对该主机进行操作
    # data={
    #     "jsonrpc": "2.0",
    #     "method": "host.delete",
    #     "params": [
    #         # "10260",   #为hostid号
    #         # "32"
    #     ],
    #     "auth": "3a443223baeabedee93075bf244f3140",
    #     "id": 1
    # }
    ##############################################################
    #根据参数获取组groupid =2
    # data={
    #     "jsonrpc": "2.0",
    #     "method": "hostgroup.get",
    #     "params": {
    #         "output": "extend",
    #         "filter": {
    #             "name": [
    #                # "Zabbix servers",
    #                 "Linux servers"
    #             ]
    #         }
    #     },
    #     "auth": "0940930566ff5d217abb594883d92f84",
    #     "id": 1
    # }
    ##############################################################
    #获取模板 templete.get
    # data={
    #     "jsonrpc": "2.0",
    #     "method": "template.get",
    #     "params": {
    #         "output": "extend",
    #         "filter": {
    #             "host": [
    #                 "Template OS Linux",
    #                 #"Template OS Windows"
    #             ]
    #         }
    #     },
    #     "auth": "0940930566ff5d217abb594883d92f84",
    #     "id": 1
    # }
    ###############################################################
    #创建主机
    data = {
        "jsonrpc": "2.0",
        "method": "host.create",
        "params": {
            "host": "testLinux",
            "interfaces": [
                {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": "192.168.1.101",
                    "dns": "",
                    "port": "10050"
                }
            ],
            "groups": [
                {
                    "groupid": "02"
                }
            ],
            "templates": [
                {
                    "templateid": "10001"
                }
            ],
            "inventory_mode": 0,            #资产清单
            "inventory": {
                "macaddress_a": "01234",
                "macaddress_b": "56768"
            }
        },
        "auth": "0940930566ff5d217abb594883d92f84",
        "id": 1
    }
    ###############################################################
    r=requests.post(url,headers=header,data=json.dumps(data))
    print(r.json())  #返回的消息，只要关注result即可