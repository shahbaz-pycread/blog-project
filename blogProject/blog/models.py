from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager # for tags
from ckeditor.fields import RichTextField 

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=100)
	category_img = models.ImageField(upload_to='category_photo', null=True, blank=True)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=255)
	content = RichTextField()
	category = models.ForeignKey(Category,null=True, on_delete=models.PROTECT)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post_image = models.ImageField(upload_to='post_image', null=True, blank=True)
	featured_image = models.ImageField(upload_to='featured_photo', null=True, blank=True)
	tags = TaggableManager()
	
	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'

	def __str__(self):
		return f'{self.title} by {self.author}'

