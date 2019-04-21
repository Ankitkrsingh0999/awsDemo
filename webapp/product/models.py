from django.db import models

# Create your models here.
class Product(models.Model):
	title 		= models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	pricing 	= models.DecimalField(max_digits=100,decimal_places=2)
	summary 	= models.TextField(default='this id cool')
	featured  	= models.BooleanField(default=False) #null =True, default=True
	email		= models.EmailField(default=False)