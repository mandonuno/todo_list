from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('check_off/<list_id>', views.check_off, name='check_off'),
    path('check_on/<list_id>', views.check_on, name='check_on'),
    path('edit/<list_id>', views.edit, name='edit'),

]