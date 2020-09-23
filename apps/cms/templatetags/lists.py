from django import template

register = template.Library()


@register.filter()
def lists(value):
  li = value.replace("[",'').replace("]",'')
  list = [x.replace("'",'').replace(" ",'') for x in li.split(',')]
  print("list",list)
  return list