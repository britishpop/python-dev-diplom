from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import WebshopUserCreationForm, ProfileForm, WebshopAuthForm
from django.contrib.auth import login, authenticate, logout
from .models import Product, ProductInfo, Shop, Parameter, Category
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    products = Product.objects.all().prefetch_related('productinfo')
    shops = Shop.objects.all()
    parameters = Parameter.objects.all().prefetch_related('productparameter_set')
    categories = Category.objects.all()

    context = {
        'products': products,
        'shops': shops,
        'parameters': parameters,
        'categories': categories,
    }
    return render(request, 'index.html', context)

def shop_signup(request):
    if request.method == 'POST':
        user_form = WebshopUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = user_form.save()
            
            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()
            
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('webshop:index')
    else:
        user_form = WebshopUserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})

def shop_login(request):
    if request.method == 'POST':
        form = WebshopAuthForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
            else:
                return redirect('webshop:index')
    else:
        form = WebshopAuthForm()
    
    return render(request, 'login.html', {'form': form})

def shop_logout(request):
    logout(request)
    return render(request, 'logout.html')

@login_required
def cart(request):
    if not request.session.session_key: # если нет сессии - создать ее
        request.session.save()

    if not request.session.get('cart_contents'): # если нет корзины в сессии - создать ее
        request.session['cart_contents'] = {}

    cart_contents = request.session['cart_contents']

    if request.method == 'POST': # запрос приходит после нажатия кнопки "Добавить в корзину"
        product_id = request.POST['product_id'] # смотрим какой товар пользователь добавил через кнопку
        product_count = int(request.POST['quantity'])
        shop_id = request.POST['shop']
        if not cart_contents.get(product_id): # если этого товара еще не было в корзине - его кол-во станет 1
            cart_contents[product_id] = [product_count, shop_id]
        else:
            cart_contents[product_id][0] += product_count # если товар в корзине уже лежал - увеличить на 1
        request.session.modified = True # сохранить корзину в сессии

    object_list = [] # этот список товаров уйдет на рендер
    cart_count = 0 # отдельная переменная для подсчета кол-ва предметов в корзине
    shop_list = [] # здесь собираются все магазины, чтобы потом узнать длину списка для расчета доставки
    price_total = 0 # сюда прибавляется цена каждого продукта

    for product in cart_contents:
        product_object = Product.objects.get(pk=product) # получим из базы объект товара
        quantity = int(cart_contents[product][0]) # получим количество товара из корзины
        cart_count += quantity # увеличим общий счетчик товаров в корзине
        price_product_total = product_object.productinfo.price_rrc * quantity
        price_total += price_product_total
        shop = Shop.objects.get(pk=cart_contents[product][1])
        if shop not in shop_list:
            shop_list.append(shop)
        object_list.append([product_object, shop, quantity, price_product_total]) # добавим товар и количество в список на рендер

    context = {
        'cart_contents': object_list,
        'cart_count': cart_count,
        'delivery_count': len(shop_list) * 100,
        'price_total': price_total,
    }

    return render(request, 'cart.html', context)

@login_required
def order_list(request):
    return HttpResponse('OrderList soon')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    