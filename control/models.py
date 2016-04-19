from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Participant(models.Model):
	"""
	Description: Model Description
	"""
	name = models.CharField(max_length=100)
	alt_phone = models.CharField(max_length=100)
	phone = models.CharField(max_length=100, unique=True)
	how_know = models.CharField(max_length=100)
	organisation = models.CharField(max_length=100)
	occupation = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	def __unicode__(self):
		return self.name