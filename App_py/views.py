from django.shortcuts import render

# Create your views here.
def MarksResponse(request):
    return render(request,'marks.html')

def Resultresponse(request):
    name=request.GET['name']
    regno=request.GET['regno']
    phone=request.GET['phone']
    tam=int(request.GET['tam'])
    eng=int(request.GET['eng'])
    mat=int(request.GET['mat'])
    sci=int(request.GET['sci'])
    soc=int(request.GET['soc'])
    total=tam+eng+mat+sci+soc
    per=total/5
    if per>90:
        Grade='A'
    elif 81<=per<=90:
        Grade='B'
    elif 61<=per<=80:
        Grade='C'
    else:
        Grade='F'
    return render(request,'result.html',context=
                  {'name':name,'regno':regno,'phone':phone,'total':str(total),'per':str(per),'grade':Grade})