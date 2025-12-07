from django import forms
from .models import Transaction,Category
from django.db.models import  Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#django form creation for adding transaction
class TransactionForm(forms.ModelForm):
    
    class Meta:
        model = Transaction
        fields = ['category', 'amount', 'date', 'notes'] 
        

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full bg-gray-800 text-white border border-gray-700 rounded p-2 focus:outline-none focus:border-green-500'}),
            'amount': forms.NumberInput(attrs={'class': 'w-full bg-gray-800 text-white border border-gray-700 rounded p-2 focus:outline-none focus:border-green-500'}),
            'notes': forms.Textarea(attrs={'class': 'w-full bg-gray-800 text-white border border-gray-700 rounded p-2 focus:outline-none focus:border-green-500', 'rows': 3}),
            'category': forms.Select(attrs={'class': 'w-full bg-gray-800 text-white border border-gray-700 rounded p-2 focus:outline-none focus:border-green-500'}),
        }

    def __init__(self,*args,**kwargs):
        user=kwargs.pop('user',None)
        super().__init__(*args,**kwargs)
        self.fields['category'].empty_label = "--- Choose a Category ---"
        if user:
            self.fields['category'].queryset = Category.objects.filter(
                Q(user=None) | Q(user=user)
            )
    

        

#form for adding catagory
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type','icon']
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full bg-gray-800 text-white border border-gray-700 rounded p-2 focus:outline-none focus:border-green-500',
                'placeholder': 'Ex: Gym, Netflix, Salary...'
            }),
            'type': forms.Select(attrs={
                'class': 'w-full bg-gray-800 text-white border border-gray-700 rounded p-2 focus:outline-none focus:border-green-500'
            }),
              'icon': forms.TextInput(attrs={
                'class': 'w-full bg-gray-800 text-white border border-gray-700 rounded p-2 focus:outline-none focus:border-green-500',
                'placeholder': 'Ex: Food🍔...'
            }),
            

        }
   


#sign up form
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
       
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'w-full bg-gray-800 text-white border border-gray-700 rounded p-3 focus:outline-none focus:border-green-500 mb-2',
                'placeholder': f'Enter {field}'
            })


#update user info
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'w-full bg-gray-800 text-white border border-gray-700 rounded p-3 focus:outline-none focus:border-green-500 mb-2',
                'placeholder': f'Enter {field}'
            })