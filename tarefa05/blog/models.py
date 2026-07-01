from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='post/')
    data_publicacao = models.DateField()

    def __str__(self):
        return self.titulo