from django.db import models

# Create your models here.

class IMG(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=20)
    url = models.URLField(max_length=200,default='')

class Goods(models.Model):
  name = models.CharField(max_length=100)
  price = models.CharField(max_length=200)
  fare = models.CharField(max_length=200)
  shop = models.CharField(max_length=200)
  toppicture = models.CharField(max_length=2000)
  detail = models.CharField(max_length=500)
  shoplogo = models.CharField(max_length=200)
  standars = models.CharField(max_length=200,default='')
  addTime = models.DateTimeField(auto_now_add=True)


class orders(models.Model):
  fare = models.IntegerField()
  goodid = models.CharField(max_length=200)
  goodname = models.CharField(max_length=200)
  num = models.IntegerField()
  orderid = models.CharField(max_length=200)
  pic = models.CharField(max_length=500)
  shop = models.CharField(max_length=200)
  standarsname = models.CharField(max_length=200)
  status = models.BooleanField(default=False)
  creattime = models.DateTimeField(auto_now_add=True)
