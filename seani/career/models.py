from django.db import models

# Create your models here.


class Career(models.Model):
    LEVELS = [
        ('TSU', 'Técnico superior  Universitario'),
        ('Ing', 'Ingenieía'),
        ('Lic', 'Licenciatura'),
        ('M', 'Maestria')
    ]
    name = models.CharField(
        verbose_name='Nombre',
        max_length=200,
    )
    short_name = models.CharField(
        verbose_name='Abreviatura',
        max_length=10,
    )
    level = models.CharField(
        verbose_name='Nivel',
        max_length=10,
        choices=LEVELS,
    )

    def __str__(self) -> str:
        return self.short_name

    class Meta:
        verbose_name = 'carrera'
        verbose_name_plural = 'carreras'
