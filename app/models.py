from django.db import models
from django.utils import timezone

class Post(models.Model):
	name = models.CharField(max_length=30)
	title = models.CharField(max_length=50)			
	body = models.TextField()
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
	 	return self.title

	
	

	


