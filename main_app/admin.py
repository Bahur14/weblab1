from django.contrib import admin
from .models import CustomUser, Task

# Реєструємо наші моделі, щоб вони з'явилися в адмінці
admin.site.register(CustomUser)
admin.site.register(Task)