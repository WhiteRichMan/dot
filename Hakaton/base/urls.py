from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('groups/', Groups.as_view(), name='groups'),

    path('<int:group_id>/join/', join, name='join'),
    path('<int:group_id>/leave/',leave, name='leave'),
]