from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Loch
from .models import CartItem
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def loch_list(request):
    user = request.user 
    lochs = Loch.objects.all()
    keyword = request.GET.get('q')
    if keyword:
        lochs = Loch.objects.filter(Q(LochName__icontains=keyword) | Q(LochCode__icontains=keyword))
    else:
        lochs = Loch.objects.all()
    per_page = 10
    paginator = Paginator(lochs, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, 'lochs/loch_list.html', {'page_obj' : page_obj,'user': user})

def loch_detail(request, id):
    user = request.user 
    loch = get_object_or_404(Loch, id=id)
    return render(request, 'lochs/loch_detail.html', {'loch' : loch,'user': user})
def index(request):
    user = request.user 
    lochs = Loch.objects.all()
    return render(request, 'lochs/index.html', {'lochs' : lochs,'user': user})

def your_view_function(request):
    user = request.user 
    all_lochs = Loch.objects.all()
    per_page = 20
    
    # 创建分页器对象
    paginator = Paginator(all_lochs, per_page)
    
    # 获取当前页数
    page_number = request.GET.get('page')
    
    # 获取当前页的对象列表
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    # 将分页后的结果传递给模板
    return render(request, 'lochs/loch_list.html', {'page_obj': page_obj,'user': user})

# 购物车相关代码

# 这个代码用于添加购物车这个动作，并进行跳转
@login_required
def add_to_cart(request, loch_id):
    loch = Loch.objects.get(pk=loch_id)
    cart_item = CartItem.objects.create(loch=loch)
    return redirect('cart')

# 这个代码负责将添加的购物车进行展示
@login_required
def cart(request):
    user = request.user 
    cart_items = CartItem.objects.all()
    return render(request, 'lochs/cart.html', {'cart_items': cart_items,'user': user})
@login_required
def delete_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart_item.delete()
    return redirect('cart')