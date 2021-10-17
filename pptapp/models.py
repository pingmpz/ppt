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
    code = models.CharField(max_length=20, primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=20, default="-") # CREATOR
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)

class Path(models.Model):
    id = models.AutoField(primary_key=True)
    serial = models.ForeignKey(Order, on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=20, default="-")  # ACTOR
    location = models.CharField(max_length=100, default="-")
    status = models.CharField(max_length=20, default="-") # CREATE, REJECT, RECEIVE
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
