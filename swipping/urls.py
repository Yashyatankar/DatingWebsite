from django.urls import path, include
from . import views

urlpatterns = [
    path('swipping/', views.swipping_view ,name='swipping')
]
