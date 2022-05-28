from django.urls import path
from . import views

urlpatterns = [
    # /candidates/
    path('', views.candidates, name='candidates'),
    path('create/', views.create_candidate, name='create candidates')
]