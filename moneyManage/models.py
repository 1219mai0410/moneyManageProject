from django.db import models
from accounts.models import User
from datetime import date

# Create your models here.
class Category(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category_owner')
    category = models.CharField(max_length=25)

    def __str__(self):
        return self.category

class Expense(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expense_owner')
    expense_date = models.DateField(default=date.today())
    item = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='expense_category')
    price = models.IntegerField()

    class Meta:
        ordering = ('-expense_date',)

class Fixed(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fixed_owner')
    content = models.CharField(max_length=50)
    price = models.IntegerField()