from django.conf import settings
from django.db import models



class UserCheckout(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True) #not required
	email = models.EmailField()


	#merchant_id


	def __str__(self):
		return self.email


class Order(models.Model):
	pass







