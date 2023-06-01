from django.shortcuts import render

# Create your views here.
def gyana(request):
    d={'a':20,'b':30}
    return render(request,'gyana.html',context=d)