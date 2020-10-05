from django.shortcuts import render
from . import models
from utils import restful
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
import datetime,time


"""  小程序专用函数"""
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

delete = "https://api.weixin.qq.com/tcb/databasedelete?access_token="
new = "https://api.weixin.qq.com/tcb/databasecollectionadd?access_token="
add = "https://api.weixin.qq.com/tcb/databaseadd?access_token="
update = "https://api.weixin.qq.com/tcb/databaseupdate?access_token="
query = "https://api.weixin.qq.com/tcb/databasequery?access_token="

def get_token():
  get_token = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=" + appid1 + "&secret=" + secret1
  res = requests.get(get_token)
  time.sleep(0.2)
  token = res.json()["access_token"]
  return token

"""  ====================== """


def orderview(request):
  token = get_token()
  _query = query + token

  form_update = {
    "env": env1,
    "query": "db.collection(\"order\").get()"
  }
  headers = {'content-type': "application/json"}
  res2 = requests.post(_query, data=json.dumps(form_update), headers=headers)
  data = eval(res2.text)["data"]
  # data = eval(res2)
  print("="*30)
  print("orderdata:,",data)
  print("=" * 30)
  orders = []
  for d in data:
    d = dict(json.loads(d))
    id = d["_id"]
    d["id"] = id
    d.pop("_id")

    orders.append(d)
  content = {
    "orders": orders
  }

  # orders = models.orders.objects.all()
  # content = {
  #   "orders": orders
  # }
  return render(request, "cms/order_list.html", content)


def orderedit(request):
  token = get_token()
  _query = query + token
  id = request.GET.get('id')
  print("=" * 30)
  print("id:", id)
  print("=" * 30)
  form_data = {
    "env": env1,
    "query": "db.collection(\"order\").where({orderid:\"%s\"}).get()" % id,
  }
  header = {"content-type": "Application/json"}
  res = requests.post(_query, data=json.dumps(form_data), headers=header)
  data = eval(res.text)["data"]
  order = []
  for d in data:
    print("=" * 30)
    d = dict(json.loads(d))
    # print("d:", d)
    # id = d["_id"]
    # d["id"] = id
    order.append(d)
  # goods = models.Goods.objects.filter(id=id).values()

  content = {"order": order}

  # id = request.GET.get("id")
  # orders = models.orders.objects.filter(id=id)

  return  render(request,"cms/orderEdit.html",content)

def orderupdate(request):
  token = get_token()
  _update = update + token
  print("添加中")
  orderid = request.POST.get("orderid")
  pic = request.POST.get("pic")
  shop = request.POST.get("shop")
  fare = request.POST.get("fare")
  num = request.POST.get("num")
  standarsname = request.POST.get("standarsname")
  status = request.POST.get("status")

  # models.orders.objects.filter(id=orderid).update(pic=pic,shop=shop,fare=fare,num=num,
  #                                                      standarsname=standarsname,status=status)


  update_data = {"pic": pic, "shop":shop, "num": num, "fare": fare,
                 "standarsname": standarsname, "status": status}

  form_data = {
    "env": env1,
    "query": "db.collection(\"order\").where({orderid:\"%s\"}).update({data:%s})" % (orderid,update_data)
  }
  headers = {"content-type": "Application/json"}
  res = requests.post(_update, data=json.dumps(form_data), headers=headers)
  print("*" * 30)
  print("res", res)
  print("res", res.text)
  print("*" * 30)


  return restful.ok()


def orderdelete(request):
  id = request.GET.get('id')
  token = get_token()
  _delte = delete + token
  delete_form = {
  "env":env1,
  "query": "db.collection(\"order\").where({orderid:\"%s\"}).remove()"%id
  }
  headers = {"content-type": "Application/json"}
  res = requests.post(_delte,data=json.dumps(delete_form),headers=headers)
  print("*" * 30)
  print("res", res)
  print("res", res.text)
  print("*" * 30)

  # models.orders.objects.filter(id=id).delete()
  return HttpResponseRedirect(reverse("cms:orderview"))


def order_filter(request):
  token = get_token()
  _query = query + token
  start = request.GET.get("start")
  end = request.GET.get("end")
  title = request.GET.get("title")
  print("start:",start)
  print("end:",end)
  print("title:",title)

  # form_update = {
  #   "env": env1,
  #   "query": "db.collection(\"order\").where({creattime:_.and(_.gt(%s),_.tl(%s)),goodname:%s,shop:%s,orderid:%s}).get()" % (
  #   start, end, title, title,title)
  # }
  form_update = {
      "env": env1,
      "query": "db.collection(\"order\").where({goodname:\"%s\"}).get()" % (title)
  }
  headers = {'content-type': "application/json"}
  res2 = requests.post(_query, data=json.dumps(form_update), headers=headers)
  data = eval(res2.text)["data"]
  # data = eval(res2)
  print("=" * 30)
  print("orderdata:,", data)
  print("=" * 30)
  orders = []
  for d in data:
    d = dict(json.loads(d))
    id = d["_id"]
    d["id"] = id
    d.pop("_id")

    orders.append(d)
  content = {
    "orders": orders
  }

  # orders = models.orders.objects.all()
  # content = {
  #   "orders": orders
  # }
  return render(request, "cms/order_list.html", content)


  # start = request.GET.get("start")
  # end = request.GET.get("end")
  # title = request.GET.get("title")
  # print("start:",start)
  # print("end:",end)
  # print("title:",title)
  # order_data = models.orders.objects.all()
  # if start or end:
  #   if start:
  #     start = time.strptime(start, '%Y/%m/%d')
  #   else:
  #     start = datetime.datetime(year=2018, month=6, day=1)
  #   if end:
  #     end = time.strptime(end, '%Y/%m/%d')
  #   else:
  #     end = datetime.datetime.now()
  # # order_data = order_data.filter(creattime__gte=start, creattime__lte=end)
  # if title:
  #   order_data = order_data.filter(Q(shop__contains=title) | Q(goodname__contains=title) | Q(goodid__contains=title) | Q(orderid__contains=title))
  #
  # return render(request,"cms/order_list.html",{"orders":order_data})

def update_order(request):
  if request.method == "POST":
    orderid = request.POST.get("orderid")
    pic = request.POST.get("pic")
    shop = request.POST.get("shop")
    goodid = request.POST.get("goodid")
    goodname = request.POST.get("goodname")
    fare = request.POST.get("fare")
    num = request.POST.get("num")
    standarsname = request.POST.get("standarsname")
    status = request.POST.get("status")
    models.orders.objects.create(pic=pic, shop=shop, fare=fare, num=num, goodid=goodid, goodname=goodname,orderid=orderid,
                                 standarsname=standarsname, status=status)
    return restful.ok()

  else:

    orderid = request.GET.get("orderid")
    goodid = request.GET.get("goodid")
    goodname = request.GET.get("goodname")
    pic = request.GET.get("pic")

    shop = request.GET.get("shop")

    fare = int(request.GET.get("fare"))

    num = int(request.GET.get("num"))

    standarsname = request.GET.get("standarsname")
    status = request.GET.get("status")
    models.orders.objects.create(pic=pic,shop=shop,fare=fare,num=num,goodid=goodid,goodname=goodname,orderid=orderid,
                                                         standarsname=standarsname,status=status)
    return restful.ok()
