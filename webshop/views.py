from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import WebshopUserCreationForm, ProfileForm, WebshopAuthForm
from django.contrib.auth import login, authenticate, logout
from .models import Product, ProductInfo, Shop, Parameter, Category, Order, OrderItem, Cart, CartItem
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

            cart = Cart(user=new_user)
            cart.save()
            
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
    cart = request.user.cart
    
    if request.method == 'POST':
        product = Product.objects.get(pk=request.POST['product_id'])
        quantity = int(request.POST['quantity'])
        if {'product': product.pk} in cart.cartitem_set.values('product').distinct():
            current_cart_item = cart.cartitem_set.get(product=product)
            current_cart_item.quantity += quantity
            current_cart_item.save()
        else:
            shop = Shop.objects.get(pk=request.POST['shop'])
            new_cart_item = CartItem(
                cart=cart,
                product=product,
                quantity=quantity,
                shop=shop
            )
            new_cart_item.save()

    context = {
        'cart': cart,
    }

    return render(request, 'cart.html', context)

@login_required
def create_order(request):
    if request.method == 'POST' and request.POST['order_action'] == 'create':
        cart = request.user.cart
        
        if len(cart.cartitem_set.all()) == 0:
            return redirect('webshop:cart')


        new_order = Order(
            user=request.user,
            status='новый',
        )
        new_order.save()

        for cart_item in cart.cartitem_set.all():
            new_order_item = OrderItem(
                quantity=cart_item.quantity,
                order=new_order,
                product=cart_item.product,
                shop=cart_item.shop,
            )
            new_order_item.save()
            cart_item.delete()

    return redirect('webshop:order_list')

@login_required
def order_list(request):
    order_dataset = Order.objects.filter(user=request.user)

    context = {
        'orders': order_dataset,
    }

    return render(request, 'order_list.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    