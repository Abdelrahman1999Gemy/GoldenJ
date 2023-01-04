from django.shortcuts import render,redirect
from .models import Player,Transaction,Sport
from django.contrib import messages
from datetime import datetime
# Create your views here.
def index(request):
    x={'name':'lovely gemy'}
    return render(request,'pages/index.html',x)
#def soon(request):
 #   return render(request,'pages/soon.html')
def dash(request):
    xr=request.POST.get('playername')
    if xr==None:
        return render(request,'pages/dash.html',{'player':Player.objects.get(Name='hima')})
    else:
        dicty=Player.objects.get(Name=xr)
        prices=[]
        #today = datetime.today()
        #dat = datetime(today.year, today.month, today.day)
        #dar=today.month()
        #dar=str(dar)
        #mont={'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'May','6':'Jun','7':'Jul','8':'Aug','9':'Sep','10':'Oct','11':'Nov','12':'Dec'}
        add=0
        for p in dicty.sport.all():
            prices.append(Sport.objects.get(SpName=p))
        if dicty.Type=='Civil':
            for s in prices:
                add=add+s.PricCivil
            if dicty.Brother == True:
                add=float(add)-(float(add)*0.35)
                add2=str(add)
                return render(request,'pages/dash.html',{'add':add2})
            else:
                return render(request,'pages/dash.html',{'add':add})
        else:
            for s in prices:
                add=add+s.PricMil
            if dicty.Brother == True:
                add=float(add)-(float(add)*0.25)
                add2=str(add)
                return render(request,'pages/dash.html',{'add':add2})
            else:
                return render(request,'pages/dash.html',{'add':add})

def ftab(request):
    return render(request,'pages/ftab.html')
def ktab(request):
    return render(request,'pages/ktab.html')
def swtab(request):
    return render(request,'pages/swtab.html')
def mustab(request):
    return render(request,'pages/mustab.html')
def artab(request):
    return render(request,'pages/artab.html')
def fitab(request):
    return render(request,'pages/fitab.html')
def sc(request):
    return render(request,'pages/sc.html')
def pc(request):
    return render(request,'pages/pc.html')
def attendance(request):
    return render(request,'pages/attendance.html')
def fa(request):
    return render(request,'pages/fa.html')
def ka(request):
    return render(request,'pages/ka.html')
def fitnessa(request):
    return render(request,'pages/fitnessa.html')
def aa(request):
    return render(request,'pages/aa.html')
def ma(request):
    return render(request,'pages/ma.html')
def sa(request):
    return render(request,'pages/sa.html')
def renew(request):
    return render(request,'pages/renew.html')