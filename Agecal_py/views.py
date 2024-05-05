from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request,'home.html')
def menupage(request):
    return render(request,'menu.html')

def menuorder(request):
    
    name=name=request.POST['name']
    phone=request.POST['phone']
    dish=request.POST['dish']
    quantity=int(request.POST['quantity'])
    if dish=='idly':
        price=quantity*20
    elif dish=='dosa':
        price=quantity*50
    else:
        price=quantity*30
    return render(request,'menuorder.html',context=
            {'name':name,'phone':phone,'dish':dish,'quantity':quantity,'price':str(price)}      
                  )