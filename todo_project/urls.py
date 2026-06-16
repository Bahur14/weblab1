from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main_app.urls')), # Підключаємо маршрути нашого додатку
    path('api-auth/', include('rest_framework.urls')), 
    
    # Автоматична документація Redoc (вимога лаби)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]