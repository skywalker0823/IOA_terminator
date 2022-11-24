from django.urls import path
from . import views
 
urlpatterns = [
    #url(r'^$', views.hello),
    path('index/', views.hello),
]