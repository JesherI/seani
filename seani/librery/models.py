from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Module(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=100)
    description = models.CharField(verbose_name="Descripción", max_length=200)

    def num_cuestion(self):
        return self.question_set.count()

    num_cuestion.short_descrition = "Número de preguntas"

    def __str__(self):
        return f"{ self.name } - { self.id }"

    class Meta:
        verbose_name = 'módule'
        verbose_name_plural = 'módulos'


class Question(models.Model):
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, verbose_name="Modulo")
    question_text = models.TextField(
        verbose_name="Texto de la Pregunta", null=True, blank=True)
    question_image = CloudinaryField(
        verbose_name="Imagen de la Pregunta",
        null=True, blank=True,
        resource_type="image",
        folder="questions"
    )
    # question_image = models.ImageField(
    #     verbose_name="Imagen de la pregunta",
    #     upload_to='questions',
    #     null=True, blank=True)
    answer1 = models.CharField(
        verbose_name="Pregunta A", max_length=200)
    answer2 = models.CharField(
        verbose_name="Pregunta B", max_length=200)
    answer3 = models.CharField(
        verbose_name="Pregunta C", max_length=200, null=True, blank=True)
    answer4 = models.CharField(
        verbose_name="Pregunta D", max_length=200, null=True, blank=True)
    correct = models.CharField(verbose_name="Respuesta Pregunta", max_length=5)

    def __str__(self):
        return f"{ self.module } - { self.id }"

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'
