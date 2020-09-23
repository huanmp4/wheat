from rest_framework import serializers
from . import models
class GoodsSerializer(serializers.ModelSerializer):

  class Meta:
    model = models.Goods
    fields = "__all__"
