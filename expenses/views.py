from datetime import datetime 
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Transaction
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .forms import TransactionForm, CategoryForm, UserRegisterForm, UserUpdateForm
from django.core.paginator import Paginator
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

#dashboard functions
@login_required
def index(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    
  
    available_months = Transaction.objects.filter(user=request.user).dates('date', 'month', order='DESC')

    filter_month = request.GET.get('month')
    
    if filter_month:
        selected_date = datetime.strptime(filter_month, "%Y-%m-%d")
        
        transactions = transactions.filter(
            date__year=selected_date.year, 
            date__month=selected_date.month
        )

    total_income = transactions.filter(category__type='Income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = transactions.filter(category__type='Expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense

    context = {
        'transactions': transactions[:5], 
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'available_months': available_months,
        'filter_month': filter_month
    }
    return render(request, 'index.html', context)

#add transaction
@login_required
def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST, user=request.user)
        
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save() 
            return redirect('index')
    else:
        form = TransactionForm(user=request.user)

    return render(request, 'add_transaction.html', {'form': form})

#edit transaction
@login_required
def edit_transaction(request,id):
    transaction=get_object_or_404(Transaction,id=id)
    if request.method=="POST":
        form=TransactionForm(request.POST,instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
         form=TransactionForm(instance=transaction)
    return render(request,'add_transaction.html',{'form':form})

#delete transaction
@login_required
def delete_transaction(request,id):
    transaction=get_object_or_404(Transaction,id=id)   
    transaction.delete()
    return redirect('index')

#function for adding category
@login_required
def category(request):
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            category=form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('index')
    else:
        form=CategoryForm()
    return render(request,'add_category.html',{'form':form})

#Displaying list of all transaction
@login_required
def Transaction_list(request):
    list_data=Transaction.objects.filter(user=request.user).order_by('-id')
    paginator = Paginator(list_data, 10) 
    
    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number)

    return render(request,'transaction_list.html', {'page_obj': page_obj})

#sign up section
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


#profile section
@login_required
def profile(request):
    user = request.user
    
    total_income = Transaction.objects.filter(user=user, category__type='Income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = Transaction.objects.filter(user=user, category__type='Expense').aggregate(Sum('amount'))['amount__sum'] or 0
    current_balance = total_income - total_expense

    context = {
        'total_income': total_income,
        'total_expense': total_expense,
        'current_balance': current_balance,
    }
    
    return render(request, 'profile.html', context)

#edit profile
@login_required
def edit_profile(request):
    if request.method == 'POST':
        
        form = UserUpdateForm(request.POST, instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('profile') 
            
    else:
        
        form = UserUpdateForm(instance=request.user)

    return render(request,'edit_profile.html', {'form': form})

#about section
def about(request):
    return render(request,'about.html')


   


