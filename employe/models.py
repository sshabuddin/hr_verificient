from django.db import models

# Create your models here.

class employe(models.Model):
   emp_id = models.IntegerField(primary_key=True)
   emp_name = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()
   joining_date = models.DateTimeField()
   emp_email = models.CharField(max_length = 50)
   reporting_manager = models.CharField(max_length = 50)
   
   class Meta:
      db_table = "employe"
