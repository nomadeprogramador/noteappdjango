from django.db import models

# Create your models here.
class Note(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=1000)
    data = models.DateTimeField(auto_now_add=True)
    marcado = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.titulo