from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserRegistrationViewSet, AboutAppView # Додали імпорт AboutAppView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'register', UserRegistrationViewSet, basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('about/', AboutAppView.as_view(), name='about'), # Додали цей рядок
]