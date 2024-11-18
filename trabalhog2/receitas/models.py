from django.db import models

class receita(models.Model):
    ingredientes = models.CharField(max_length=1000)
    receita_criada = models.CharField(max_length= 10000)
    
    def __str__(self) -> str:
        return f"Receita: {self.id}"