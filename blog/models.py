from __future__ import unicode_literals
from django.db import models
from django.db.models import permalink



# Create your models here.

class Category(models.Model):
	tittle = models.CharField(max_length = 100, unique = True)	
	# slug = models.SlugField(max_length = 100, unique = True)

	def __unicode__(self):
			return '%s' % self.tittle

	# def get_absolute_url(self):
	# 	return ("view_blog_category", [self.slug,])

class Post(models.Model):

	tittle = models.CharField(max_length = 100, unique = True)
	# slug = models.SlugField(max_length = 100, unique = True)
	text = models.TextField()
	posted = models.DateField(db_index = True, auto_now_add = True)
	category = models.ForeignKey(Category)	
	image = models.ImageField(blank = True)
		
	def __unicode__(self):
		return '%s' % self.tittle

	# def get_absolute_url(self):
 #    	return ("view_blog_category", [self.slug,])


