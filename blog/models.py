from django.db import models
import markdown

class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)  # Nuevo campo para enlaces de YouTube
    audio = models.FileField(upload_to='audios/', blank=True, null=True)

    def contenido_html(self):
        """Convierte el contenido en Markdown a HTML"""
        return markdown.markdown(self.contenido)

    def get_embedded_video(self):
        """Convierte una URL de YouTube en una URL embebida"""
        if self.video_url:
            return self.video_url.replace("watch?v=", "embed/")
        return None

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name="comentarios")
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.nombre} en {self.articulo.titulo}"

class Seguidor(models.Model):
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.correo
