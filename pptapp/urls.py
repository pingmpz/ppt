from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('track_serial/', views.track_serial, name='track_serial'),

    path('change_location/', views.change_location, name='change_location'),
    path('exc_change_location/', views.exc_change_location, name='exc_change_location'),

    path('new_workorder/', views.new_workorder, name='new_workorder'),
    path('validate_order_no/', views.validate_order_no, name='validate_order_no'),
    path('validate_serial_code/', views.validate_serial_code, name='validate_serial_code'),
    path('new_workorder_save/', views.new_workorder_save, name='new_workorder_save'),

    path('order_master/', views.order_master, name='order_master'),
    path('emp_master/', views.emp_master, name='emp_master'),
    path('fg_master/', views.fg_master, name='fg_master'),

    path('move_history/', views.move_history, name='move_history'),
    path('del_history/', views.del_history, name='del_history'),

    path('order/<str:order_no>', views.order, name='order'),
    path('create_serial/', views.create_serial, name='create_serial'),
    path('multiple_receive/', views.multiple_receive, name='multiple_receive'),
    path('add_po_no/', views.add_po_no, name='add_po_no'),
    path('serial_receive/', views.serial_receive, name='serial_receive'),
    path('serial_reject/', views.serial_reject, name='serial_reject'),
    path('serial_edit/', views.serial_edit, name='serial_edit'),
    path('serial_move/', views.serial_move, name='serial_move'),
    path('serial_delete/', views.serial_delete, name='serial_delete'),

    path('import_data/', views.import_data, name='import_data'),
]
