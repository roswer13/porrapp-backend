from django.urls import path
from core import views


app_name = 'core'

urlpatterns = [
    path('seed/', views.SeedView.as_view(), name='seed'),
]
