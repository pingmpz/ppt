from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),

    path('new_workorder/', views.new_workorder, name='new_workorder'),
    path('validate_order_no/', views.validate_order_no, name='validate_order_no'),
    path('new_workorder_save/', views.new_workorder_save, name='new_workorder_save'),

    path('order_master/', views.order_master, name='order_master'),
    path('emp_master/', views.emp_master, name='emp_master'),
    path('fg_master/', views.fg_master, name='fg_master'),

    path('order/<str:order_no>', views.order, name='order'),
    path('serial_reject/', views.serial_reject, name='serial_reject'),
    path('serial_receive/', views.serial_receive, name='serial_receive'),
    path('serial_edit/', views.serial_edit, name='serial_edit'),
]
