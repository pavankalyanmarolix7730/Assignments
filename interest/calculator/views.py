from django.shortcuts import render

# Create your views here.

def principal(request):
    principal_1=request.GET.get("num1") if request.GET.get("num1") else 0
    Interest_1=request.GET.get("num2") if request.GET.get("num2") else 0
    Time_1=request.GET.get("num3") if request.GET.get("num3") else 0
    product=(int(principal_1)*int(Interest_1)*int(Time_1))//100
    context={"product":product}
    return render(request,"base.html",context)
#app name is interest
#project name is calucalator