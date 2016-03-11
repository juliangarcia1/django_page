#from bson.json_util import default
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.

class PublicadaAdmin(models.Manager):
     def get_queryset(self):
        return super(PublicadaAdmin,self).get_queryset()\
                          .filter(estado)

class Entrada(models.Model):
    ESTADOS_ELEGIR = (
        ('editando', 'Editando'),
        ('publicado', 'Publicado'),
    )
    titulo = models.CharField(max_length=200, default='')
    autor = models.CharField(max_length=250)
    fecha = models.DateField(auto_now_add = True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_publicacion = models.DateTimeField(default=timezone.now(), blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, default=timezone.now)
    contenido = models.TextField()
    estado = models.CharField(max_length=9,
                              choices=ESTADOS_ELEGIR,
                              default='editando')

    def get_absolute_url(self):
        return reverse('blog:entrada_detalle',\
                       args=[self.autor])
    def __unicode__(self):
        return self.autor
