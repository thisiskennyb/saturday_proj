from .views import AllBikes
from django.urls import path

urlpatterns = [
    path('', AllBikes.as_view(), name='all_bikes')
]