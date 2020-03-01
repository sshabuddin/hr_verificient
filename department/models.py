from django.db import models

# Create your models here.


class department(models.Model):
   manager_id = models.IntegerField(primary_key=True)
   manager_name = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()
   joining_date = models.DateField()
   manager_email = models.CharField(max_length = 50)
   managing_department = models.CharField(max_length = 50)
   
   class Meta:
      db_table = "department"
