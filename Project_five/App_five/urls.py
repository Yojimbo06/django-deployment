from django.conf.urls import url,include
from App_five import views
from django.urls import path

# TEMPLATE URLS
app_name= 'basic_app'

urlpatterns=[
path('register/', views.register, name='register'),
path('user_login/', views.user_login, name='user_login'),
]
