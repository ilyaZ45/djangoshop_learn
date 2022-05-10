from django.shortcuts import render
from .models import Order

# Create your views here.
def first_page(request):
    object_list = Order.objects.all()
    return render(request, './index.html', {'object_list': object_list})

def thanks(request):
    # name = request.GET['name']
    # phone = request.GET['phone']
    name = request.POST['name']
    phone = request.POST['phone']
    el = Order(order_name = name, order_phone = phone)
    el.save()
    return render(request, './thanks.html', { 'name': name,
                                              'phone': phone })