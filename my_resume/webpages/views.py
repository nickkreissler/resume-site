from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'webpages/home.html',context = None)

def about(request):
    return render(request,'webpages/about.html',context = None)
def resume(request):
    return render(request,'webpages/resume.html',context = None)
