# accounts/urls.py

from django.urls import path
from .views import error_accounts, check_account, register_user, user_login, user_logout

urlpatterns = [
    path('', check_account,name="check_account"),
    path('error', error_accounts ,name="error_accounts"),
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
