from django.urls import path
from users.views import users


urlpatterns = [
    path('home', users, name='users')
]

