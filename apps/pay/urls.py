from django.urls import path
from . import views
urlpatterns = [
  path("",views.Pay.as_view,"pay"),
  path("receive",views.receive,"receive"),
]