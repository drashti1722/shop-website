from django.urls import path
from .views import shopping


urlpatterns = [
    path('a/',shopping)
]