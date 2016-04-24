from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):

	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	tekst = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
			
	def publish(self):
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self):
		return self.title
		
class Klub(models.Model):

	id_klubu = models.IntegerField()
	nazwa_klubu = models.CharField(max_length=200)
	skrot_nazwy_klubu = models.CharField(max_length=200)
	wartosc_skladu = models.CharField(max_length=200)
	url_logo = models.URLField()
	
	def publish(self):
		self.save()
		
	def __str__(self):
		return self.title

