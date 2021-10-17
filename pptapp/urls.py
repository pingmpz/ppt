from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('new_workorder/', views.new_workorder, name='new_workorder'),
    path('order_master/', views.order_master, name='order_master'),
    path('emp_master/', views.emp_master, name='emp_master'),
    path('fg_master/', views.fg_master, name='fg_master'),
]
