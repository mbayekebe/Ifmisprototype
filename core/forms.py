from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Budget, BudgetTransaction, Account, GeneralLedger, BankAccount, CashFlow

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['fiscal_year', 'entity', 'amount_allocated', 'amount_spent', 'amount_remaining']

class BudgetTransactionForm(forms.ModelForm):
    class Meta:
        model = BudgetTransaction
        fields = ['budget', 'date', 'amount', 'transaction_type']

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'account_type', 'parent_account']

class GeneralLedgerForm(forms.ModelForm):
    class Meta:
        model = GeneralLedger
        fields = ['account', 'date', 'debit', 'credit', 'balance', 'entity']

class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ['bank_name', 'account_number', 'balance', 'entity']

class CashFlowForm(forms.ModelForm):
    class Meta:
        model = CashFlow
        fields = ['date', 'amount', 'flow_type', 'account', 'entity']
