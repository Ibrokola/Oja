from django.db import models




class Product(models.Model):
	title 		= models.CharField(max_length=120)
	description = models.TextField(blank=True, null=True)
	price 	 	= models.DecimalField(decimal_places=2, max_digits=20)	
	active		= models.BooleanField(default=True)
	#slug 		=
	#inventory	=

	def __str__(self):
		return self.title



# Prodcut Images


# Product Category