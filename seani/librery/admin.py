from .models import Module, Question
from django.contrib import admin

from .models import Module, Question


class QuestionInline(admin.StackedInline):
    model = Question


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'num_cuestion']
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_text', 'module', 'correct']
    list_filter = ['module']