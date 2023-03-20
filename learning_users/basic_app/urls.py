#from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from basic_app import views

# SET THE NAMESPACE!
app_name = 'basic_app'

urlpatterns=[
    path('relative/$',views.register,name='register'),
    path('user_login/$',views.user_login,name='user_login'),
]
