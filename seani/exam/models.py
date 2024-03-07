from django.db import models
from django.contrib.auth.models import User 

from career.models import Career
from librery.models import Module, Question

class Stage(models.Model):
    stage = models.IntegerField(
        verbose_name = "Estapa"
    )
    application_date = models.DateField(
        verbose_name = "Fecha de Aplicación"
    )
    
    @property
    def year(self):
        return self.application_date.year
    
    @property
    def month(self):
        months = ['enero', 'febrero', 'marzo', 'abril', 'mayo',
                  'junio', 'julio','agosto', 'septiembre','octubre', 'noviembre', 'diciembre']
        return months[self.application_date.month -1]
        
    def __str__(self):
        return f"{ self.stage }-{ self.month } { self.year }"
    
    class Meta:
        verbose_name = "etapa"
        verbose_name_plural = "etapas"
        
class Exam(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuario")
    career = models.ForeignKey(Career, on_delete=models.CASCADE, verbose_name="Carrera")
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, verbose_name="Etapa")
    modules = models.ManyToManyField(Module, through='ExamModule')
    questions = models.ManyToManyField(
        Question,
        through='Breakdown'
    )
    score = models.FloatField(verbose_name = "Calificación", default = 0.0 )
    created = models.DateTimeField(verbose_name = "Fecha de creación", auto_now_add=True)
    update = models.DateTimeField(verbose_name = "Fecha de actualización", auto_now =True)

    def set_modules(self):
        for module in Module.objects.all():
            self.modules.add(module)

    def set_questions(self):
        for module in self.modules.all():
            for question in module.question_set.all():
                #self.questions.add(question)
                Breakdown.objects.create(
                    exam = self, 
                    question = question,
                    correct = question.correct)
    
    def __str__(self):
        return f"{ self.user.username }-{ self.score }"
    
    class Meta:
        verbose_name = "exam"
        verbose_name_plural = "examenes"
    
class ExamModule(models.Model):
    exam = models.ForeignKey(Exam, on_delete = models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    active =  models.BooleanField(default=True)
    score = models.FloatField(default=0.0)

class Breakdown(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=5, default='-')
    correct = models.CharField(max_length=5, default='-')