from django.db import models

# Create your models here.

class blood(models.Model):
	Fname=models.CharField(max_length=20)
	Lname=models.CharField(max_length=20)
	age=models.IntegerField(null=True)
	Gender=models.CharField(max_length=10)
	Mobile=models.CharField(max_length=10)
	email=models.EmailField(null=True)
	group=models.CharField(max_length=4)
	class Meta:
		db_table = "students_blood_data"
	
	def __str__(self):
		return self.Fname