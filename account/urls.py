from django.urls import path
from . import views



app_name = 'account'
urlpatterns = [
    path('login', views.UserLogin.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('chekotp', views.CheckView.as_view(), name='checkotp'),

]