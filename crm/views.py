from django.shortcuts import render
from .models import Order
from .forms import Orderform
from price.models import PriceCard, PriceTable
# from cms.models import CmsSlider


# Create your views here.
def first_page(request):
    object_list = Order.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = Orderform()
    return render(request, './index.html', {'object_list': object_list,
                                            'form': form,
                                            'pc_1': pc_1,
                                            'pc_2': pc_2,
                                            'pc_3': pc_3,
                                            'price_table': price_table,
                                            })

def thanks(request):
    # name = request.GET['name']
    # phone = request.GET['phone']
    name = request.POST['name']
    phone = request.POST['phone']
    el = Order(order_name = name, order_phone = phone)
    el.save()
    return render(request, './thanks.html', { 'name': name,
                                              'phone': phone })