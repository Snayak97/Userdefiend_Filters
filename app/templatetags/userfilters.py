from django import template
register =template.Library()

@register.filter()
def swap(data):
    return data.swapcase()

#register.filter('swap',swap)
@ register.filter()
def remove(data,arg):
    return data.replace(arg,"")

@register.filter()
def slice(data):
    x=data.split()
    y=[]
    for i in range(len(x)):
        if i==0:
            y.append(x[i])
        elif i==len(x)-1:
            y.append(x[i])
        else:
            y.append(x[i].upper())
    return " ".join(y)
       


@register.filter()
def count(data,arg):
    c=0
    for i in range(len(data)):
        if data[i:i+len(arg)]==arg:
            c+=1
    return c
  