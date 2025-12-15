from django.shortcuts import render

def home(request):
    num1 = 10
    result = cs_calc(num1)
    return render(request, 'app1/index.html', {'param1':result})

def cs_calc(num):
    list1=[]
    list1.append(num*num)
    list1.append(num*num*num)
    return list1
