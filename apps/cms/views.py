from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from django.urls import reverse
# Create your views here.
from django.http import HttpResponse
from . import serializers
from utils import restful
from django.conf import settings
import datetime,time

from django.db.models import Q


from .models import IMG



#
# def uploadImg(request):
#     """
#     图片上传
#     :param request:
#     :return:
#     """
#     if request.method == 'POST':
#         filename = request.FILES.get('img').name
#         new_img = IMG(
#             img=request.FILES.get('img'),
#             name=request.FILES.get('img').name
#         )
#         name = request.build_absolute_uri(settings.MEDIA_URL + filename)
#         print("filename:",name)
#         new_img.save()
#     return render(request, 'cms/home.html')
#
#
# def showImg(request):
#     """
#     图片显示
#     :param request:
#     :return:
#     """
#     imgs = IMG.objects.all()
#     content = {
#         'imgs': imgs,
#     }
#     for i in imgs:
#         print(i.img.url)
#     return render(request, 'cms/img.html', content)

# def imageupdata(request):
#     file = request.FILES.get("file")
#     filename = request.FILES.get("file").name
#     url = request.build_absolute_uri(settings.MEDIA_URL + "img/" + filename)
#     IMG.objects.create(img=file,name=filename,url=url)
#
#     return restful.result(200,data=url)

def index(request):
    order = models.orders.objects.all()
    return render(request, "cms/order_list.html",{"orders":order})



def shopadd(request):
    return render(request,"cms/home.html")

def imageupdata(request):
    file = request.FILES.get("file")
    filename1 = request.FILES.get("file").name
    suffix = filename1.split(".")[-1]
    filename = str(int(time.mktime(datetime.datetime.now().timetuple()))) + '.' +suffix
    file.name = filename
    print("file:", file)
    url = request.build_absolute_uri(settings.MEDIA_URL + "img/" + filename)
    IMG.objects.create(img=file, name=filename, url=url)

    return restful.result(200, data=url)


def writeIndatabase(request):
    url0 = request.POST.get("file_p0")
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
    print("shop",shop)
    toppicture = [url1,url2,url3,url4]
    models.Goods.objects.create(detail=url0,shoplogo=url5,name=name,price=price,shop=shop,
                                fare=fare,standars=standars,toppicture=toppicture)
    return restful.ok()

def shopView(request):
    goods = models.Goods.objects.all()
    return render(request, "cms/view.html", {"goods":goods})


def goods_list_show(request):
    goods = models.Goods.objects.all()
    return render(request, "cms/goods_list.html", {"goods": goods})


def goodsEditer(request):
    id = request.GET.get('id')

    goods = models.Goods.objects.filter(id=id).values()

    print("id",id)
    print("goods:",goods)
    return render(request, "cms/goods_edit.html", {"goods": goods})


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
    id = request.POST.get("id")
    print("id,",id)
    models.Goods.objects.get(id=id).delete()
    return restful.ok()


def get_delete(request):
    id = request.GET.get("id")
    print("id,", id)
    models.Goods.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse("cms:goods_list_show"))

def edit(request):
    id = request.POST.get("id")
    print("id",id)
    good = models.Goods.objects.get(id=id)
    data = serializers.GoodsSerializer(good).data
    return restful.result(200,data=data)

def update(request):
    id = request.POST.get("good_id")
    url0 = request.POST.get("file_p0")
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
    print("更改id",id)
    toppicture = [url1,url2,url3,url4]

    models.Goods.objects.filter(id=id).update(detail=url0, shoplogo=url5, name=name, price=price, shop=shop,
                                fare=fare, standars=standars, toppicture=toppicture)
    return restful.ok()


def get_goods(request):
  goods = models.Goods.objects.all()
  goods = serializers.GoodsSerializer(goods,many=True).data
  content = {"goods":goods}
  return restful.result(code=200,data=content)