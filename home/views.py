from django.shortcuts import render,HttpResponse
from .models import Faq,Article, Contact

# Create your views here.
def home(request):
    l=Article.objects.all().order_by('-time')[:6]
    a=Article.objects.filter(popular='yes').order_by('-time')[:6]
    context={'post':l,'article':a}
    return render(request,'home/home.html',context)

def about(request):
    return render(request,'home/about.html')

def achivement(request):
    return render(request,'home/achivement.html')

def faq(request):
    a=Faq.objects.all()
    context={'faq':a}
    return render(request,'home/faq.html',context)

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        s=Contact(name=name,email=email,mobile=phone,message=message)
        s.save()
        
    return render(request,'home/contact.html')

def latestpost(request):
    l=Article.objects.all().order_by('-time')
    context={'post':l}
    return render(request,'home/latestpost.html',context)

def blogpost(request,slug):
    l=Article.objects.filter(slug=slug)
    la=Article.objects.all().order_by('-time')[:5]
    p=Article.objects.filter(popular='yes').order_by('-time')[:5]
    context={'post':l,'latest':la,'popular':p}
    return render(request,'home/blogpost.html',context)
    