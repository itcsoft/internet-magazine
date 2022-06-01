from django.shortcuts import render
from marketplace.models import Category, Product

# Create your views here.
def base(request):
    return render(request, 'base.html')

def homepage(request):
    categories = Category.objects.all()
    count_cat = categories.count()   
    print(count_cat)
    return render(request, 'index.html', {'categories':categories, 'count_category':count_cat})

def suit(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    title = 'Костюмы'
    return render(request, 'suit.html', {'title':title, 'products':products, 'categories':categories})

def cart(request):
    return render(request, 'cart.html', {'title':'Корзина'} )