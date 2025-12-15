from django.shortcuts import render
from app1.forms import inputform
def home(request):
    if request.method == "POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input1",1)
            n2=data.get("input2",1)
            result=n1+n2
            return render(request, 'app2/index.html', {'param1':result})
    else:
        form1=inputform()
    return render(request, 'app2/index.html', {'form1':form1})

