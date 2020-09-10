from django.db import models
from PIL import Image
from django.core.files.storage import FileSystemStorage


# Create your models here.

class Datosclientes(models.Model):
    Title = models.CharField(max_length=20)
    Docnro = models.CharField(max_length=15)
    telefono = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    Direcc = models.CharField(max_length=35)
    DireccFact = models.CharField(max_length=40)
    Facturaranombrede = models.CharField(max_length=20)
    comprobantep = models.FileField(upload_to='images/')
    def __str__(self):
        return self.Title

