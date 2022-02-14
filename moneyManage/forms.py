from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['expense_date', 'item', 'category', 'price']
        widgets = {
            'expense_date': forms.DateInput(attrs={'class': 'el_formInput hp_bt30'}),
            'item': forms.TextInput(attrs={'placeholder': 'item', 'class': 'el_formInput hp_bt30'}),
            'price': forms.NumberInput(attrs={'placeholder': 'price', 'class': 'el_formInput hp_bt30'})
        }
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(queryset=Category.objects.filter(owner=user), initial=Category.objects.all()[0], widget=forms.Select(attrs={'class': 'el_formInput hp_bt30'}))
        for field in self.fields.values():
            field.label = ''

class FixedForm(forms.ModelForm):
    class Meta:
        model = Fixed
        fields = ['content', 'price']
        widgets = {
            'content': forms.TextInput(attrs={'placeholder': 'content', 'class': 'el_formInput hp_bt15'}),
            'price': forms.NumberInput(attrs={'placeholder': 'price', 'class': 'el_formInput hp_bt15'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''