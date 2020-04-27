from django.contrib import admin
from .models import Contact,Article,Faq
# Register your models here.
admin.site.site_header='AmritSoft Point'

admin.site.register(Faq)
admin.site.register(Article)

admin.site.register(Contact)
