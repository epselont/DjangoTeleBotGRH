from .views import GetList, GetText
from django.urls import path, include

urlpatterns = [
    path('button', GetList.as_view(), name='button-list'),
]
