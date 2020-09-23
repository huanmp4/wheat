from django.shortcuts import render
from . import models
from utils import restful
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
import datetime,time


def orderview(request):
  orders = models.orders.objects.all()
  content = {
    "orders": orders
  }
  return render(request, "cms/order_list.html", content)


def orderedit(request):
  order_id = request.GET.get("order_id")
  print("orderedit:", order_id)
  orders = models.orders.objects.filter(orderid=order_id)

  return  render(request,"cms/orderEdit.html",{"order":orders})

def orderupdate(request):
  print("添加中")
  orderid = request.POST.get("orderid")
  pic = request.POST.get("pic")
  shop = request.POST.get("shop")
  fare = request.POST.get("fare")
  num = request.POST.get("num")
  standarsname = request.POST.get("standarsname")
  status = request.POST.get("status")
  models.orders.objects.filter(orderid=orderid).update(pic=pic,shop=shop,fare=fare,num=num,
                                                       standarsname=standarsname,status=status)
  return restful.ok()


def orderdelete(request):
  id = request.GET.get('orderid')
  models.orders.objects.filter(orderid=id).delete()
  return HttpResponseRedirect(reverse("cms:orderview"))


def order_filter(request):
  start = request.GET.get("start")
  end = request.GET.get("end")
  title = request.GET.get("title")
  print("start:",start)
  print("end:",end)
  print("title:",title)
  order_data = models.orders.objects.all()
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
    order_data = order_data.filter(Q(shop__contains=title) | Q(goodname__contains=title) | Q(goodid__contains=title) | Q(orderid__contains=title))

  return render(request,"cms/order_list.html",{"orders":order_data})

def update_order(request):
  # orderid = request.POST.get("orderid")
  # pic = request.POST.get("pic")
  # shop = request.POST.get("shop")
  # print("orderid:",orderid)
  # fare = request.POST.get("fare")
  # num = request.POST.get("num")
  # standarsname = request.POST.get("standarsname")
  # status = request.POST.get("status")

  orderid = request.GET.get("orderid")
  print("orderid: ", orderid)
  pic = request.GET.get("pic")
  print("pic: ", pic)
  shop = request.GET.get("shop")
  print("shop: ", shop)
  fare = int(request.GET.get("fare"))
  print("fare: ", fare)
  num = int(request.GET.get("num"))
  print("num: ", num)
  standarsname = request.GET.get("standarsname")
  status = request.GET.get("status")
  models.orders.objects.create(pic=pic,shop=shop,fare=fare,num=num,
                                                       standarsname=standarsname,status=status)
  return restful.ok()
