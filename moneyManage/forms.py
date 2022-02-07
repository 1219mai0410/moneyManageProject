from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']

class ExpenseForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.filter(owner=user))

    class Meta:
        model = Expense
        fields = ['expense_date', 'item', 'category', 'price']

class FixedForm(forms.ModelForm):
    class Meta:
        model = Fixed
        fields = ['content', 'price']