from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('category/', CategoryView.as_view(), name="category"),
    path('expense/', ExpenseView.as_view(), name="expense"),
    path('fixed/', FixedView.as_view(), name="fixed"),
]