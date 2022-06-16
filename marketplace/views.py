from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render, redirect
from marketplace.models import Category2, Product, Order, OrderData
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def base(request):
    # products_all = Product.objects.all()
    # products_filter = Product.objects.filter(name='Футболка ТВОЕ').values()
    # products_get = Product.objects.get(pk=1)
    # products_exclude = Product.objects.exclude(pk=2).values()
    # products_contains = Product.objects.filter(name__contains='о').values()

    return render(request, 'base.html') 

    #{'products_all':products_all, 'products_filter':products_filter,
    # 'products_get':products_get, 'products_exclude':products_exclude, 'products_contains':products_contains}
    # )


def homepage(request):
    categories = Category2.objects.all()
    count_cat = categories.count()   
    print(count_cat)
    return render(request, 'index.html', {'categories':categories, 'count_category':count_cat})

def products(request, pk):
    # products = Product.objects.all()
    categories = Category2.objects.all()
    title = Category2.objects.get(pk=pk)
    products_cat = Product.objects.filter(category=pk)
    return render(request, 'products.html', {'title':title, 'products':products_cat, 'categories':categories})

def search(request):
    if request.method == 'POST':
        searched_value = request.POST.get('search')
        searched_products = Product.objects.filter(name__contains = searched_value)
        count_of_products = searched_products.count()
        return render(request, 'search.html', {'searched_value':searched_value, 'searched_products':searched_products, 'count_of_products':count_of_products})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    else:
        form = UserCreationForm()

    return render(request, 'user.html', {'form':form})    
        

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return redirect('homepage')
    else:
        form = AuthenticationForm()

    return render(request, 'user.html', {'form':form})



def signout(request):
    logout(request)

    return render(request, 'index.html')


def detail(request, pk):
    detail_product = Product.objects.get(pk=pk)
    print(detail_product)

    return render(request, 'detail.html', {'detail_product':detail_product})





def addToCart(request, pk):

    cart_session = request.session.get('cart_session', [])
    cart_session.append(pk)
    request.session['cart_session'] = cart_session
    print(cart_session)
    return redirect('/cart')

def cart(request):
    cart_session = request.session.get('cart_session', [])
    all_product_count = len(cart_session)
    products_inCart = Product.objects.filter(id__in=cart_session)
    print(products_inCart)    
    all_product_total_sum = 0
    for product_cart in products_inCart:
        product_cart.count = cart_session.count(product_cart.id)
        product_cart.sum = product_cart.count * product_cart.price
        all_product_total_sum += product_cart.sum

    return render(request, 'cart.html', {'title':'Корзина', 'products_inCart':products_inCart, 'all_product_count':all_product_count, 'all_product_total_sum':all_product_total_sum} )


def remove_from_url(request, pk):
    cart = request.session.get('cart_session', [])
    cart.remove(pk)
    request.session['cart_session'] = cart

    return redirect('cart')

    
def order(request):
    return render(request, 'order.html')

def order_data(request):
    cart_session = request.session.get('cart_session', [])
    products_inCart = Product.objects.filter(id__in=cart_session)
    print(products_inCart)    
    all_product_total_sum = 0
    for product_cart in products_inCart:
        product_cart.count = cart_session.count(product_cart.id)
        product_cart.sum = product_cart.count * product_cart.price
        all_product_total_sum += product_cart.sum

    if request.method == 'POST':
        orderc = OrderData()
        orderc.name = request.POST.get('c_name')
        orderc.number = request.POST.get('c_number')
        orderc.address = request.POST.get('c_address')
        orderc.email = request.POST.get('c_email')
        orderc.message = request.POST.get('c_message')
        orderc.save()
    
        for i in products_inCart:
            order = Order()
            order.product = i.name
            order.price = i.price
            order.count = i.count
            order.total_sum = i.sum
            order.customer = orderc
            order.save()
    
    cart_session = request.session.get('cart_session', [])
    cart_session.clear()
    request.session['cart_session'] = cart_session
    all_product_count = len(cart_session)

    return redirect('thanks')
    

def thanks(request):
    return render(request, 'thanks.html')




