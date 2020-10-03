
from django.urls import path,re_path
from . import views,views_order
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf import settings

app_name = 'cms'

urlpatterns = [
    path("",views.show_goods,name="index"),
    path("imageupdata",views.imageupdata,name="imageupdata"),
    path("writeIndatabase",views.writeIndatabase,name="writeIndatabase"),
    path("shopView",views.shopView,name="shopView"),
    path("delete",views.delete,name="delete"),
    path("goodsEditer",views.goodsEditer,name="goodsEditer"),
    path("goods_filter",views.goods_filter,name="goods_filter"),
    path("get_delete",views.get_delete,name="get_delete"),
    path("goods_list_show",views.goods_list_show,name="goods_list_show"),
    path("edit",views.edit,name="edit"),
    path("goods_update",views.goods_update,name="goods_update"),
    path("shopadd",views.shopadd,name="shopadd"),
    path("get_goods",views.get_goods,name="get_goods"),
    path("show_goods",views.show_goods,name="show_goods"),
]


urlpatterns += [
    path("orderview",views_order.orderview,name="orderview"),
    path("orderedit",views_order.orderedit,name="orderedit"),
    path("orderupdate",views_order.orderupdate,name="orderupdate"),
    path("orderdelete",views_order.orderdelete,name="orderdelete"),
    path("order_filter",views_order.order_filter,name="order_filter"),
    path("update_order",views_order.update_order,name="update_order"),
]

urlpatterns += [
                  # url(r'^upload', views.uploadImg,name="upload"),
                  # url(r'^show', views.showImg,name="show"),
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  这句话是用来指定和映射静态文件