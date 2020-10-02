from django import template

register = template.Library()


@register.filter()
def lists(value):
  if value:
    li = value.replace("[",'').replace("]",'')
    list = [x.replace("'",'').replace(" ",'') for x in li.split(',')]
    print("list",list)
    return list
  else:
    return value

@register.filter()
def extra(value):
  return value[0]

