from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('logon/', Logon.as_view(), name='logon'),
    path('index/', Index.as_view(), name="index"),
]