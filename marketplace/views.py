from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')

def homepage(request):
    return render(request, 'index.html')

def suit(request):
    title = 'Костюмы'
    return render(request, 'suit.html', {'title':title})