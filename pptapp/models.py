from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100, default="-")
    section = models.CharField(max_length=50, default="-")
    position = models.CharField(max_length=50, default="-")
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    no = models.CharField(max_length=20, primary_key=True)
    drawing_no = models.CharField(max_length=20, default="-")
    fg_code = models.CharField(max_length=20, default="-")
    emp_id = models.CharField(max_length=20, default="-") # CREATOR
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

class Serial(models.Model):
    id = models.AutoField(primary_key=True)
    # type = models.IntegerField(default=1) # Type 1, 2, 3
    code = models.CharField(max_length=20, default="-")
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    po_no = models.CharField(max_length=20, default="-")
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

class Path(models.Model):
    id = models.AutoField(primary_key=True)
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=20, default="-")  # ACTOR
    location = models.CharField(max_length=100, default="-")
    status = models.CharField(max_length=20, default="-")
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

class MoveHistory(models.Model):
    id = models.AutoField(primary_key=True)
    serial_code = models.CharField(max_length=20, default="-")
    old_order_no = models.CharField(max_length=20, default="-")
    new_order_no = models.CharField(max_length=20, default="-")
    emp_id = models.CharField(max_length=20, default="-")
    reason = models.TextField(max_length=500, default="-")
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

class DeleteHistory(models.Model):
    id = models.AutoField(primary_key=True)
    serial_code = models.CharField(max_length=20, default="-")
    order_no = models.CharField(max_length=20, default="-")
    emp_id = models.CharField(max_length=20, default="-")
    reason = models.TextField(max_length=500, default="-")
    path_history = models.TextField(max_length=1000, default="-")
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
