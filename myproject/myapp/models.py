from django.db import models

# Create your models here.
class PizzaModel(models.Model):
	name = models.CharField(max_length = 10)
	price = models.CharField(max_length = 10)
class OrderModel(models.Model):
	username = models.CharField(max_length = 20)
	#phoneno = models.CharField(max_length = 10,null=True)
	address = models.CharField(max_length = 1000)
	ordereditems = models.CharField(max_length = 1000)
	status = models.CharField(max_length = 20)
