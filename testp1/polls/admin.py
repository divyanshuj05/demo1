from django.contrib import admin

# Register your models here.
from .models import Question, choice

admin.site.register(Question)
admin.site.register(choice)