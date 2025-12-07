from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

class Category(models.Model):
    category_types=[
        ('Income','Income'),
        ('Expense','Expense')
    ]

    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200)
    type=models.CharField(max_length=30,choices=category_types,default='Expense')
    icon=models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        prefix = "🟢" if self.type == "Income" else "🔴"
        return f"{prefix}  {self.name} {self.icon or ''}"

class Transaction(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    amount=models.IntegerField()
    notes=models.TextField(null=True,blank=True)
    def __str__(self):
        return f'{self.user},{self.category},{self.amount}'
    


