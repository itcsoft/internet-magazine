from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render, redirect
from marketplace.models import Category2, Product
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

def cart(request):
    return render(request, 'cart.html', {'title':'Корзина'} )

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

    return HttpResponse('КОрзина')




    