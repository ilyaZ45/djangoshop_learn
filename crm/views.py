from django.shortcuts import render
from .models import Order
from .forms import Orderform

# Create your views here.
def first_page(request):
    object_list = Order.objects.all()
    form = Orderform()
    return render(request, './index.html', {'object_list': object_list,
                                            'form': form})

def thanks(request):
    # name = request.GET['name']
    # phone = request.GET['phone']
    name = request.POST['name']
    phone = request.POST['phone']
    el = Order(order_name = name, order_phone = phone)
    el.save()
    return render(request, './thanks.html', { 'name': name,
                                              'phone': phone })