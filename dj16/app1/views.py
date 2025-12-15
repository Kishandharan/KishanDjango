from django.shortcuts import render

def home(request):
    list1=[]
    list2=[]
    for i in range(1, 6, 1):
        sqr = square(i)
        list1.append(sqr)

    for i in range(1, 6, 1):
        result=fact(i) 
        list2.append(result)

    return render(request, 'app1/index.html', {'param1':list1, 'param2':list2})

def square(num):
    return num*num

def fact(num):
    result=1
    for i in range(1, num+1, 1):
        result=result*i
    return result
