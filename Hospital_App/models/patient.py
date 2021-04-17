from django.db import models

class Patient(models.Model):

    name = models.CharField(max_length = 20, null = True)
    age = models.CharField(max_length = 3, null = True)
    city = models.CharField(max_length = 20, null = True)
    phone = models.CharField(max_length = 10, null = True)
    date = models.CharField(max_length = 20,null=True)

    def __str__(self):
        return str(self.name)