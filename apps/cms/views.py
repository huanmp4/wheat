from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from django.urls import reverse
from django.http import HttpResponse
from . import serializers
from utils import restful
from django.conf import settings
import datetime,time
from django.db.models import Q
from .models import IMG

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

delete_url = "https://api.weixin.qq.com/tcb/databasedelete?access_token="
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



def show_goods(request):
    token = get_token()
    _query = query + token

    form_update = {
        "env":env1,
            "query": "db.collection(\"goods\").get()"
    }
    headers = {'content-type': "application/json"}
    res2 = requests.post(_query,data=json.dumps(form_update),headers = headers)
    data = eval(res2.text)["data"]
    goods = []
    for d in data:
        d = dict(json.loads(d))
        id = d["_id"]
        d["id"] = id
        d.pop("_id")

        goods.append(d)
    content = {
        "goods":goods
    }
    return render(request,"cms/goods_list.html",content)



def goodsEditer(request):
    token = get_token()
    _query = query + token

    id = request.GET.get('id')
    form_data = {
        "env":env1,
        "query":"db.collection(\"goods\").where({_id:\"%s\"}).get()"%id,
    }
    header= {"content-type":"Application/json"}
    res = requests.post(_query,data=json.dumps(form_data),headers=header)
    data = eval(res.text)["data"]
    goods = []
    for d in data:

        d = dict(json.loads(d))
        id = d["_id"]
        d["id"] = id
        goods.append(d)
    # goods = models.Goods.objects.filter(id=id).values()

    content = {"goods": goods}
    return render(request, "cms/goods_edit.html", content)


def goods_update(request):
    token = get_token()
    _update = update + token

    id = request.POST.get("good_id")
    url0 = request.POST.get("file_p0")
    url10 = [url0]
    url1 = request.POST.get("file_p1")
    url2 = request.POST.get("file_p2")
    url3 = request.POST.get("file_p3")
    url4 = request.POST.get("file_p4")
    url5 = request.POST.get("file_p5")
    name = request.POST.get("name")
    price = request.POST.get("price")
    fare = request.POST.get("fare")
    shop = request.POST.get("shop")
    standars = request.POST.get("standars")
    businessImage = request.POST.get("businessImage")
    print("businessImage:",businessImage)
    toppicture = [url1, url2, url3, url4]

    update_data = {"detail":url10, "shoplogo":url5, "name":name, "price":price, "shop":shop,"fare":fare, "standars":standars, "toppicture":toppicture,"businessImage":businessImage}
    form_data = {
        "env":env1,
        "query":"db.collection(\"goods\").where({_id:\"%s\"}).update({data:%s})"%(id,update_data)
    }

    headers = {"content-type": "Application/json"}
    res = requests.post(_update,data=json.dumps(form_data),headers=headers)
    print("*"*30)
    print("res",res.text)
    print("*" * 30)
    print("goods,更新成功")
    return restful.ok()





def index(request):
    order = models.orders.objects.all()
    return render(request, "cms/order_list.html",{"orders":order})



def shopadd(request):
    return render(request, "cms/goods_add.html")

def imageupdata(request):
    file = request.FILES.get("file")
    filename1 = request.FILES.get("file").name
    suffix = filename1.split(".")[-1]
    filename = str(int(time.mktime(datetime.datetime.now().timetuple()))) + '.' +suffix
    file.name = filename
    url = request.build_absolute_uri(settings.MEDIA_URL + "img/" + filename)
    IMG.objects.create(img=file, name=filename, url=url)

    return restful.result(200, data=url)


def writeIndatabase(request):
    token = get_token()
    _add = add + token

    url0 = request.POST.get("file_p0")
    url10 = [url0]
    url1 = request.POST.get("file_p1")
    url2 = request.POST.get("file_p2")
    url3 = request.POST.get("file_p3")
    url4 = request.POST.get("file_p4")
    url5 = request.POST.get("file_p5")
    name = request.POST.get("name")
    price = request.POST.get("price")
    fare = request.POST.get("fare")
    shop = request.POST.get("shop")
    businessImage = request.POST.get("businessImage")
    print("businessImage",businessImage)
    standars = request.POST.get("standars")
    toppicture = [url1, url2, url3, url4]
    update_data = {"detail": url10, "shoplogo": url5, "name": name, "price": price, "shop": shop, "fare": fare,
                   "standars": standars, "toppicture": toppicture,"businessImage":businessImage}
    form_data = {
        "env": env1,
        "query": "db.collection(\"goods\").add({data:[%s]})"%update_data
    }
    headers = {"content-type": "Application/json"}
    res = requests.post(_add, data=json.dumps(form_data), headers=headers)
    print("*" * 30)
    print("res", res.text)
    print("*" * 30)




    # url0 = request.POST.get("file_p0")
    # url1 = request.POST.get("file_p1")
    # url2 = request.POST.get("file_p2")
    # url3 = request.POST.get("file_p3")
    # url4 = request.POST.get("file_p4")
    # url5 = request.POST.get("file_p5")
    # name = request.POST.get("name")
    # price = request.POST.get("price")
    # fare = request.POST.get("fare")
    # shop = request.POST.get("shop")
    # standars = request.POST.get("standars")
    #
    #
    #
    # print("shop",shop)
    # toppicture = [url1,url2,url3,url4]
    # models.Goods.objects.create(detail=url0,shoplogo=url5,name=name,price=price,shop=shop,
    #                             fare=fare,standars=standars,toppicture=toppicture)
    return restful.ok()

def shopView(request):
    goods = models.Goods.objects.all()
    token = get_token()
    _query = query + token

    form_update = {
        "env": env1,
        "query": "db.collection(\"goods\").get()"
    }
    headers = {'content-type': "application/json"}
    res2 = requests.post(_query, data=json.dumps(form_update), headers=headers)
    data = eval(res2.text)["data"]
    goods = []
    for d in data:
        d = dict(json.loads(d))
        id = d["_id"]
        d["id"] = id
        d.pop("_id")

        goods.append(d)
    content = {
        "goods": goods
    }
    return render(request, "cms/view.html", content)


def goods_list_show(request):
    # goods = models.Goods.objects.all()

    # return render(request, "cms/goods_list.html", {"goods": goods})
    return HttpResponseRedirect(reverse("cms:goods_list_show"))






def goods_filter(request):
  start = request.GET.get("start")
  end = request.GET.get("end")
  title = request.GET.get("title")
  print("start:",start)
  print("end:",end)
  print("title:",title)
  order_data = models.Goods.objects.all()
  if start or end:
    if start:
      start = time.strptime(start, '%Y/%m/%d')
    else:
      start = datetime.datetime(year=2018, month=6, day=1)
    if end:
      end = time.strptime(end, '%Y/%m/%d')
    else:
      end = datetime.datetime.now()
  # order_data = order_data.filter(creattime__gte=start, creattime__lte=end)
  if title:
    order_data = order_data.filter(Q(name__contains=title) | Q(shop__contains=title) )

  return render(request,"cms/goods_list.html",{"goods":order_data})


def delete(request):
    id = request.POST.get('id')
    token = get_token()
    _delte = delete_url + token
    delete_form = {
        "env": env1,
        "query": "db.collection(\"goods\").where({_id:\"%s\"}).remove()" % id
    }
    headers = {"content-type": "Application/json"}
    res = requests.post(_delte, data=json.dumps(delete_form), headers=headers)
    print("*" * 30)
    print("res", res)
    print("res", res.text)
    print("*" * 30)

    # id = request.POST.get("id")
    # print("id,",id)
    # models.Goods.objects.get(id=id).delete()
    return restful.ok()


def get_delete(request):
    id = request.GET.get('id')
    token = get_token()
    _delte = delete_url + token
    delete_form = {
        "env": env1,
        "query": "db.collection(\"goods\").where({_id:\"%s\"}).remove()" % id
    }
    headers = {"content-type": "Application/json"}
    res = requests.post(_delte, data=json.dumps(delete_form), headers=headers)
    print("*" * 30)
    print("res", res)
    print("res", res.text)
    print("*" * 30)

    # id = request.GET.get("id")
    # print("id,", id)
    # models.Goods.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse("cms:show_goods"))

def edit(request):
    token = get_token()
    _query = query + token

    id = request.POST.get('id')

    print("=" * 30)
    print("id:", id)
    print("=" * 30)
    form_data = {
        "env": env1,
        "query": "db.collection(\"goods\").where({_id:\"%s\"}).get()" % id,
    }
    header = {"content-type": "Application/json"}
    res = requests.post(_query, data=json.dumps(form_data), headers=header)
    data = eval(res.text)["data"]
    goods = {}
    for d in data:
        print("=" * 30)
        d = dict(json.loads(d))
        print("d:", d)
        standars = json.dumps(d["standars"])
        d["standars"] = standars
        id = d["_id"]
        d["id"] = id
        goods.update(d)
    print("good_dict:",goods)
    # goods = models.Goods.objects.filter(id=id).values()

    return restful.result(200, data=goods)


    # id = request.POST.get("id")
    # print("id",id)
    # good = models.Goods.objects.get(id=id)
    # data = serializers.GoodsSerializer(good).data
    # return restful.result(200,data=data)




def get_goods(request):
  goods = models.Goods.objects.all()
  goods = serializers.GoodsSerializer(goods,many=True).data
  content = {"goods":goods}
  return restful.result(code=200,data=content)