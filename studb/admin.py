from django.contrib import admin
from .models import(Textbook)
from .models import(Question)

admin.site.register(Textbook)
admin.site.register(Question)