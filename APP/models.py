from django.db import models

# Create your models here.
class AdminLogin(models.Model):
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=20)


class createcontest(models.Model):
    theme = models.CharField(max_length=100)
    startdate = models.DateField()
    enddate = models.DateField()

    class Meta:
        'db_table' == 'createcontest'   

class register(models.Model):
    username = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    conpass = models.CharField(max_length=20)
    
    class Meta:
        'db_table' == 'register'        



    