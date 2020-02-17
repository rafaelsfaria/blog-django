from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=50, default='Tecnologia')

	class Meta():
		verbose_name_plural = "categories"

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.title