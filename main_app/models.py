from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# Створюємо власний менеджер користувачів
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email є обов'язковим")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=False, blank=True, null=True)
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=150, verbose_name="Ім'я")
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Чоловіча'), ('Female', 'Жіноча')],
        blank=True,
        null=True,
        verbose_name="Стать"
    )
    birth_date = models.DateField(blank=True, null=True, verbose_name="Дата народження")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    # Вказуємо Django використовувати наш новий менеджер!
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255, verbose_name="Назва завдання")
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    is_completed = models.BooleanField(default=False, verbose_name="Виконано")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    def __str__(self):
        return self.title