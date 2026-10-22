from django.db import models

class Album(models.Model):
    titulo = models.CharField(max_length=150, verbose_name="Título del Álbum")
    descripcion = models.TextField(verbose_name="Descripción / Reseña")
    precio = models.IntegerField(verbose_name="Precio (CLP)")
    disponible = models.BooleanField(default=True, verbose_name="¿Disponible para venta?")
    fecha_lanzamiento = models.DateField(verbose_name="Fecha de Lanzamiento")
    # Imagen de la portada del vinilo
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True, verbose_name="Portada del Vinilo")
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Álbum"
        verbose_name_plural = "Álbumes"
        ordering = ['-fecha_lanzamiento']

    def __str__(self):
        return self.titulo


class Cancion(models.Model):
    album = models.ForeignKey(
        Album, 
        on_delete=models.CASCADE, 
        related_name='canciones',
        verbose_name="Álbum"
    )
    titulo = models.CharField(max_length=150, verbose_name="Título de la Canción")
    duracion_segundos = models.IntegerField(help_text="Duración en segundos", verbose_name="Duración (seg)")
    track_numero = models.IntegerField(verbose_name="N° de Pista")

    class Meta:
        verbose_name = "Canción"
        verbose_name_plural = "Canciones"
        ordering = ['album', 'track_numero']

    def __str__(self):
        return f"{self.track_numero}. {self.titulo} - {self.album.titulo}"