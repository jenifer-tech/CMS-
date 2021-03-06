from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify
from django.conf import settings


class BlogPost(models.Model):
	title 				= models.CharField(max_length=50, null=False, blank=True)
	body 				= models.TextField(max_length=5000, null=False, blank=True)
	image 				= models.ImageField(upload_to='static', null=False, blank=True)
	date_published 		= models.DateTimeField(auto_now_add=True, verbose_name="date published")
	date_updated 		= models.DateTimeField(auto_now=True, verbose_name="date updated")
	author 				= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	

	def __str__(self):
		return self.title