from django.db import models

# Create your models here.


class State(models.Model):
    state = models.IntegerField(
        verbose_name="Etapa"
    )
    applicatio_date = models.DateTimeField(
        verbose_name="Fecha de Aplicación"
    )

    @property
    def year(selft):
        return selft.applicatio_date.year

    @property
    def month(selft):
        months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
                  'julio', 'agosto', 'septiembre', 'octubre',  'noviembre', 'diciembre']
        return selft.applicatio_date.month
    
    def __str__(self):
        return  f'{self.state}-{self.month}{ self.year }'
    
    class Meta:
        verbose_name = "etapa"
        verbose_name_plural = "etapas"
