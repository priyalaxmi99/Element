from django.db import models

# Create your models here.
class RequestCallBack(models.Model):
	user_names=models.TextField()
	user_mails=models.TextField()
	user_numbers=models.TextField()
	user_elements=models.TextField()
	user_messages=models.TextField()


	def __str__(self):
		return self.user_names

class SubscribeNow(models.Model):
	customer=models.TextField()

	def __str__(self):
		return self.customer