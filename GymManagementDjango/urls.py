from django.contrib import admin
from django.urls import path, include
from gym.views import health_check

urlpatterns = [
    path('health/', health_check),
    path('admin/', admin.site.urls),
    path('', include('gym.urls')),
]
