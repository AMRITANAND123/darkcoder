from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name='home'),
    path('latestpost',views.latestpost,name='latestpost'),
    path('about',views.about,name='about'),
    path('achivement',views.achivement,name='achivement'),

    path('faq',views.faq,name='faq'),
    path('contact',views.contact,name='contact'),
    path('post/<str:slug>',views.blogpost,name='blopgpost'),



    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
