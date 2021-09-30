from django.urls import path
from .views import *

urlpatterns = [
    path((''), home, name='home'),
    
    #услуги, контакты, товары, сотрудники, etc.
    path(('services/'), services, name='services'),
    path(('contacts/'), contacts, name='contacts'),
    path(('goods/'), goods, name='goods'),
    path(('staff/'), staff, name='staff'),
    path(('cabinet/'), cabinet, name='cabinet'),

]

