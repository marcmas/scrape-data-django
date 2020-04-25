from django.db import models



class Path(models.Model):
    path = models.CharField(max_length=200, default="M:/Uklady/PLX")

    def __str__(self):
        return self.path


# Create your models here.
class Files(models.Model):
    path = models.CharField(max_length=200, default="path")
    column_one = models.CharField(max_length=50, default="PLX")
    column_two = models.CharField(max_length=50, default="PLX_FGK")
    file_name = models.CharField(max_length=50, null=True, blank=True)
    column_three = models.CharField(max_length=50, default="N")
    column_four = models.CharField(max_length=50, default="1")

    def __str__(self):
        return "Name: " + self.file_name
    
