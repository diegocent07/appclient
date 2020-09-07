from django.db import models
from PIL import Image


# Create your models here.

class Datosclientes(models.Model):
    Title = models.CharField(max_length=20)
    # CI_x002f_DNI_x002f_RG_x002f_RUC = models.IntegerField()
    Direcc = models.CharField(max_length=35)
    DireccFact = models.CharField(max_length=40)
    Facturaranombrede = models.CharField(max_length=20)
    comprobantep = models.ImageField(upload_to='images',blank=True)
    def __str__(self):
        return self.Title

