from django.urls import path
from .views import *

urlpatterns = [
    path((''), home, name='home'),
    
    #услуги, товары, сотрудники, etc.
    #path((''), home, name='home'),
    #path((''), home, name='home'),
    #path((''), home, name='home'),
    #path((''), home, name='home'),
]
