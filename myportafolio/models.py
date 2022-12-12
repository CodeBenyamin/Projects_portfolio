from django.db import models

# Create your models here.
class Tags(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self): return self.nombre
class PortafolioModel(models.Model):
    titulo=models.CharField(max_length=100)
    foto = models.URLField(max_length=500)
    descripcion=models.TextField(max_length=100)
    url=models.URLField(max_length=100)
    #tags=models.CharField(max_length=100)
    tags = models.ForeignKey(Tags, on_delete=models.PROTECT)

    def __str__(self): return self.titulo