from django.contrib import admin
from .models import Employee, Order, Serial, Path, MoveHistory, DeleteHistory

admin.site.register(Employee)
admin.site.register(Order)
admin.site.register(Serial)
admin.site.register(Path)
admin.site.register(MoveHistory)
admin.site.register(DeleteHistory)
