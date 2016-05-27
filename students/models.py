from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    AK_points = models.IntegerField()
    IT_points = models.IntegerField()
    KU_points = models.IntegerField()
    NL_points = models.IntegerField()
    RE_points = models.IntegerField()
    EN_points = models.IntegerField()
    GE_points = models.IntegerField()
    MA_points = models.IntegerField()

    def __str__(self):
        return self.name