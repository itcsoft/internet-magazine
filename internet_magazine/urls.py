"""internet_magazine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from marketplace.views import base, homepage, products, cart, search, signup, signin, signout, detail, addToCart, remove_from_url, order, thanks, order_data
from internet_magazine.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('base', base, name='base'),
    path('', homepage, name='homepage'),
    path('products/<int:pk>', products, name='products'),
    path('cart', cart, name='cart'),
    path('search/', search, name='search'),
    path('users/', include('users.urls')),
    path('accounts/', include( 'django.contrib.auth.urls')),
    path('signup', signup, name='signup'),    # регистрация 
    path('signin', signin, name='signin'),    # войти
    path('signout', signout, name='signout'), # выход
    path('detail/<int:pk>', detail, name='detail'),
    path('addToCart/<int:pk>', addToCart, name='addToCart'),
    path('remove_from_url/<int:pk>', remove_from_url, name='remove_from_url'),
    path('order/', order, name='order'),
    path('order_data/', order_data, name='order_data'),
    path('thanks/', thanks, name='thanks'),
    path('admin/', admin.site.urls),
]


urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)