from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=500)
    img=models.ImageField(upload_to='home/atricle')
    body=models.TextField(max_length=5000)
    postedBy=models.CharField(max_length=100)
    time=models.DateTimeField()
    slug=models.SlugField(max_length=100,default='')
    popular=models.CharField(max_length=10,default='yes')


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=100)
    message=models.CharField(max_length=1000)


class Faq(models.Model):
    code=models.CharField(max_length=10,default='')
    question=models.CharField(max_length=1000)
    answer=models.CharField(max_length=1000)
