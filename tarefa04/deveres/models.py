from django.db import models

class Dever(models.Model):

    STATUS = [
        ("P", "Pendente"),
        ("C", "Concluída"),
    ]

    nome = models.CharField(max_length=150)
    status = models.CharField(max_length=1, choices=STATUS)
    prazo = models.DateField()
    
    def __str__(self):
        return self.nome
    
    
    class Meta:
        verbose_name = "Dever"
        verbose_name_plural = "Deveres"