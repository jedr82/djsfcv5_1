from django.urls import path
from .views import BaseView

app_name = 'base'

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
]