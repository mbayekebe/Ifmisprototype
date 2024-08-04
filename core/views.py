from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Budget, BudgetTransaction, Entity, Account, GeneralLedger, BankAccount, CashFlow

# Define the index view
def index(request):
    return render(request, 'core/index.html')

def register(request):
    from .forms import UserRegisterForm  # Import here to avoid circular dependency
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})

def user_login(request):
    from .forms import UserLoginForm  # Import here to avoid circular dependency
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('budget_list')
            else:
                return render(request, 'core/login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = UserLoginForm()
    return render(request, 'core/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def budget_list(request):
    budgets = Budget.objects.all()
    return render(request, 'core/budget_list.html', {'budgets': budgets})

@login_required
def budget_detail(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    transactions = BudgetTransaction.objects.filter(budget=budget)
    return render(request, 'core/budget_detail.html', {'budget': budget, 'transactions': transactions})

@login_required
def budget_create(request):
    from .forms import BudgetForm  # Import here to avoid circular dependency
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('budget_list')
    else:
        form = BudgetForm()
    return render(request, 'core/budget_form.html', {'form': form})

@login_required
def budget_update(request, pk):
    from .forms import BudgetForm  # Import here to avoid circular dependency
    budget = get_object_or_404(Budget, pk=pk)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('budget_list')
    else:
        form = BudgetForm(instance=budget)
    return render(request, 'core/budget_form.html', {'form': form})

@login_required
def budget_delete(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    if request.method == 'POST':
        budget.delete()
        return redirect('budget_list')
    return render(request, 'core/budget_confirm_delete.html', {'budget': budget})

@login_required
def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'core/account_list.html', {'accounts': accounts})

@login_required
def account_detail(request, pk):
    account = get_object_or_404(Account, pk=pk)
    ledgers = GeneralLedger.objects.filter(account=account)
    return render(request, 'core/account_detail.html', {'account': account, 'ledgers': ledgers})

@login_required
def account_create(request):
    from .forms import AccountForm  # Import here to avoid circular dependency
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm()
    return render(request, 'core/account_form.html', {'form': form})

@login_required
def account_update(request, pk):
    from .forms import AccountForm  # Import here to avoid circular dependency
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm(instance=account)
    return render(request, 'core/account_form.html', {'form': form})

@login_required
def account_delete(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        account.delete()
        return redirect('account_list')
    return render(request, 'core/account_confirm_delete.html', {'account': account})

@login_required
def bankaccount_list(request):
    accounts = BankAccount.objects.all()
    return render(request, 'core/bankaccount_list.html', {'accounts': accounts})

@login_required
def bankaccount_detail(request, pk):
    account = get_object_or_404(BankAccount, pk=pk)
    cashflows = CashFlow.objects.filter(account=account)
    return render(request, 'core/bankaccount_detail.html', {'account': account, 'cashflows': cashflows})

@login_required
def bankaccount_create(request):
    from .forms import BankAccountForm  # Import here to avoid circular dependency
    if request.method == 'POST':
        form = BankAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bankaccount_list')
    else:
        form = BankAccountForm()
    return render(request, 'core/bankaccount_form.html', {'form': form})

@login_required
def bankaccount_update(request, pk):
    from .forms import BankAccountForm  # Import here to avoid circular dependency
    account = get_object_or_404(BankAccount, pk=pk)
    if request.method == 'POST':
        form = BankAccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('bankaccount_list')
    else:
        form = BankAccountForm(instance=account)
    return render(request, 'core/bankaccount_form.html', {'form': form})

@login_required
def bankaccount_delete(request, pk):
    account = get_object_or_404(BankAccount, pk=pk)
    if request.method == 'POST':
        account.delete()
        return redirect('bankaccount_list')
    return render(request, 'core/bankaccount_confirm_delete.html', {'account': account})

from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Define the custom logout view
@login_required
def custom_logout(request):
    auth_logout(request)
    return redirect('login')
