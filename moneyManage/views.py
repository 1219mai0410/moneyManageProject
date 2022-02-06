from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

# Create your views here.
class CategoryView(TemplateView, LoginRequiredMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.params = {
            'form': CategoryForm()
        }

    def get(self, request):
        return render(request, 'moneyManage/category.html', self.params)

    def post(self, request):
        model = Category()
        model.owner = request.user
        form = CategoryForm(request.POST, instance=model)
        form.save()
        return render(request, 'moneyManage/category.html', self.params)

class ExpenseView(TemplateView, LoginRequiredMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.params = {}

    def get(self, request):
        self.params['form'] = ExpenseForm(request.user)
        return render(request, 'moneyManage/expense.html', self.params)

    def post(self, request):
        self.params['form'] = ExpenseForm(request.user)
        model = Expense()
        model.owner = request.user
        form = ExpenseForm(request.user, request.POST, instance=model)
        form.save()
        return render(request, 'moneyManage/expense.html', self.params)