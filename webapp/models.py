from django.db import models

# Create your models here.
class utilisateurs(models.Model):
	prenom=models.CharField(max_length=20)
	nom=models.CharField(max_length=20)
	tel=models.IntegerField()

	def __str__(self):
		return self.prenom
		