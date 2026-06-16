from rest_framework import viewsets, permissions
from .models import Task, CustomUser
from .serializers import TaskSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class AboutAppView(APIView):
    permission_classes = [permissions.AllowAny] # Доступно всім

    def get(self, request):
        return Response({
            "name": "To-Do List API",
            "description": "Зручний додаток для створення та керування списком справ. Дозволяє користувачам зберігати свої завдання та відслідковувати їх виконання.",
            "logo_url": "https://cdn-icons-png.flaticon.com/512/2098/2098402.png" # Просто посилання на тематичну іконку
        })
class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated] # Доступ тільки для залогінених

    def get_queryset(self):
        # Користувач бачить ТІЛЬКИ свої завдання
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # При створенні завдання автоматично прив'язуємо його до автора
        serializer.save(user=self.request.user)