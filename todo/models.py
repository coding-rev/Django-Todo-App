from django.db import models

# Create your models here.
class TodoModel(models.Model):
	todo_body 			= models.CharField(max_length=50)
	finished 			= models.BooleanField(default=False)
	date_created 		= models.DateTimeField(auto_now_add=True)
	date_updated 		= models.DateTimeField(auto_now=True)

	class Meta:
		ordering =['-id']
	

	