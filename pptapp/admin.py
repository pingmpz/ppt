from django.contrib import admin
from .models import Employee, Order, Serial, Path

admin.site.register(Employee)
admin.site.register(Order)
admin.site.register(Serial)
admin.site.register(Path)
