import requests
import json
import time
url = 'https://api.weixin.qq.com/tcb/databasemigrateexport?access_token=ACCESS_TOKEN'

#我的
appid = "wx5a6465866d81821c"
secret = "525ebf1fd169c0690e366df865ac1d73"
env = "bubble-zi95u"
#他们的
appid1 = "wx4df25ad915c7b761"
secret1 = "e2b34a530f0176206ca9bd6d45a28ca0"
env1 = "first-1w1h4"


get_token = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=" + appid1 + "&secret=" + secret1

res = requests.get(get_token)
print("res",)
time.sleep(1)
token = res.json()["access_token"]

delete_table = "https://api.weixin.qq.com/tcb/databasecollectiondelete?access_token=" + token
add = "https://api.weixin.qq.com/tcb/databaseadd?access_token=" + token
update = "https://api.weixin.qq.com/tcb/databaseupdate?access_token=" + token
query = "https://api.weixin.qq.com/tcb/databasequery?access_token="+ token
new_table = "https://api.weixin.qq.com/tcb/databasecollectionadd?access_token=" + token

form_data2 = {'env':env1,'collection_name':'order'}
#
# form_update = {
#     "env":env,
#         "query": "db.collection(\"goods\").get()"
# }

# update_data = {"pic": "https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2393842080,3667201553&fm=26&gp=0.jpg", "shop":"汽车专卖", "num": "985", "fare": "12",
#                  "standarsname": "[[12,13,14]]", "status": "1"}
# form_data = {
#     "env": env1,
#     "query": "db.collection(\"orders\").add({data:[%s]})"%(update_data)
# }



headers = {'content-type': "application/json"}
res2 = requests.post(new_table,data=json.dumps(form_data2),headers = headers)

data = eval(res2.text)
print("data",data)