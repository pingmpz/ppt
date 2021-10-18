from django.shortcuts import render, redirect
from .models import Employee, Order, Serial, Path
from django.http import JsonResponse

def index(request):
    context = {
    }
    return render(request, 'index.html', context)

def change_location(request):
    context = {
    }
    return render(request, 'change_location.html', context)

def new_workorder(request):
    context = {
    }
    return render(request, 'new_workorder.html', context)

def validate_order_no(request):
    order_no = request.GET.get('order_no')
    data = {
        'is_exist': Order.objects.filter(no=order_no).exists()
    }
    return JsonResponse(data)

def new_workorder_save(request):
    # COLLECT DATA
    order_no = request.POST.get('order_no')
    drawing_no = request.POST.get('drawing_no')
    fg_code = request.POST.get('fg_code')
    emp_id = request.POST.get('emp_id')
    location = request.POST.get('location')
    serial_code_list = []
    serial_code_count = int(request.POST.get('serial_code_count'))
    for i in range(serial_code_count):
        serial_code = request.POST.get('serial_code_' + str(i))
        serial_code_list.append(serial_code)
    # PREPARE DATA
    status = 'CREATED'
    # SAVE DATA
    #-- WORK ORDER
    order_new = Order(no=order_no,drawing_no=drawing_no,fg_code=fg_code,emp_id=emp_id)
    order_new.save()
    for i in range(serial_code_count):
        #-- SERIAL CODE
        serial_new = Serial(code=serial_code_list[i],order=order_new)
        serial_new.save()
        #-- PATH
        path_new = Path(serial=serial_new,emp_id=emp_id,location=location,status=status)
        path_new.save()
    context = {
    }
    return redirect('/order/' + order_new.no)

def order_master(request):
    orders = Order.objects.all()
    items = []
    for order in orders:
        serials = Serial.objects.filter(order=order)
        items.append(len(serials))
    context = {
        'orders' : orders,
        'items' : items,
    }
    return render(request, 'order_master.html', context)

def emp_master(request):
    context = {
    }
    return render(request, 'emp_master.html', context)

def fg_master(request):
    context = {
    }
    return render(request, 'fg_master.html', context)

def order(request, order_no):
    order = Order.objects.get(no=order_no)
    serial_codes = Serial.objects.filter(order=order)
    path_list = []
    last_status = []
    last_receivers = []
    last_locations = []
    last_timestamps = []
    for serial_code in serial_codes:
        paths = Path.objects.filter(serial=serial_code).order_by('date_published')
        path_list.append(paths)
        if len(paths) > 0:
            last_path = paths[len(paths) - 1]
            last_status.append(last_path.status)
            last_receivers.append(last_path.emp_id)
            last_locations.append(last_path.location)
            last_timestamps.append(last_path.date_published)
        else:
            last_status.append('-')
            last_receivers.append('-')
            last_locations.append('-')
            last_timestamps.append('-')
    context = {
        'order' : order,
        'serial_codes' : serial_codes,
        'path_list' : path_list,
        'last_status' : last_status,
        'last_receivers' : last_receivers,
        'last_locations' : last_locations,
        'last_timestamps' : last_timestamps,
    }
    return render(request, 'order.html', context)

def create_serial(request):
    # COLLECT DATA
    order_no = request.GET.get('order_no')
    serial_code = request.GET.get('serial_code')
    emp_id = request.GET.get('emp_id')
    location = request.GET.get('location')
    # PREPARE DATA
    order = Order.objects.get(no=order_no)
    status = 'CREATED'
    # SAVE DATA
    #-- SERIAL CODE
    serial_new = Serial(code=serial_code,order=order)
    serial_new.save()
    #-- PATH
    path_new = Path(serial=serial_new,emp_id=emp_id,location=location,status=status)
    path_new.save()
    data = {
    }
    return JsonResponse(data)

def multiple_receive(request):
    # COLLECT DATA
    serial_code_list = request.GET.getlist('serial_code_list[]')
    emp_id = request.GET.get('emp_id')
    location = request.GET.get('location')
    # PREPARE DATA
    status = 'RECEIVED'
    # SAVE DATA
    for i in range(len(serial_code_list)):
        serial = Serial.objects.get(id=serial_code_list[i])
        path_new = Path(serial=serial,emp_id=emp_id,location=location,status=status)
        path_new.save()
    data = {
    }
    return JsonResponse(data)

def serial_receive(request):
    # COLLECT DATA
    serial_code_id = request.GET.get('serial_code_id')
    emp_id = request.GET.get('emp_id')
    location = request.GET.get('location')
    # PREPARE DATA
    serial = Serial.objects.get(id=serial_code_id)
    status = 'RECEIVED'
    # SAVE DATA
    path_new = Path(serial=serial,emp_id=emp_id,location=location,status=status)
    path_new.save()
    data = {
    }
    return JsonResponse(data)

def serial_reject(request):
    # COLLECT DATA
    serial_code_id = request.GET.get('serial_code_id')
    emp_id = request.GET.get('emp_id')
    location = request.GET.get('location')
    # PREPARE DATA
    serial = Serial.objects.get(id=serial_code_id)
    status = 'REJECTED'
    # SAVE DATA
    path_new = Path(serial=serial,emp_id=emp_id,location=location,status=status)
    path_new.save()
    data = {
    }
    return JsonResponse(data)

def serial_edit(request):
    # COLLECT DATA
    serial_code_id = request.GET.get('serial_code_id')
    new_serial_code = request.GET.get('new_serial_code')
    # PREPARE DATA
    serial = Serial.objects.get(id=serial_code_id)
    # SAVE DATA
    serial.code = new_serial_code
    serial.save()
    data = {
    }
    return JsonResponse(data)
