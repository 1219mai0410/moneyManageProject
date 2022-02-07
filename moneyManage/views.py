from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

# Create your views here.
class IndexView(TemplateView, LoginRequiredMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.params = {}

    def get(self, request):
        self.params['fxed'] = Fixed.objects.filter(owner=request.user)
        self.params['expense'] = Expense.objects.filter(owner=request.user)
        return render(request, 'moneyManage/index.html', self.params)

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

class FixedView(TemplateView, LoginRequiredMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.params = {
            'form': FixedForm()
        }

    def get(self, request):
        return render(request, 'moneyManage/fixed.html', self.params)

    def post(self, request):
        model = Fixed()
        model.owner = request.user
        form = FixedForm(request.POST, instance=model)
        form.save()
        return render(request, 'moneyManage/fixed.html', self.params)