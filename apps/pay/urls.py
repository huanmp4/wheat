from . import views
from django.urls import path
urlpatterns = [

  path("",views.Pay.as_view,name="pay"),
  path("receive",views.receive,name="receive"),
]