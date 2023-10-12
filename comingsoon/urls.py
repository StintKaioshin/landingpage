from django.urls import path
from . import views

app_name = 'comingsoon'

urlpatterns = [
    path('', views.home, name='home'),
    path('terms-of-use/', views.terms_of_use, name='terms_of_use'),

]


