from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title