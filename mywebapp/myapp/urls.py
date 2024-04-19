from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('form/', views.form_submission_page, name='form_submission_page'),
]