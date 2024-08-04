from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    index, register,
    budget_list, budget_detail, budget_create, budget_update, budget_delete,
    account_list, account_detail, account_create, account_update, account_delete,
    bankaccount_list, bankaccount_detail, bankaccount_create, bankaccount_update, bankaccount_delete
)

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('budgets/', budget_list, name='budget_list'),
    path('budgets/<int:pk>/', budget_detail, name='budget_detail'),
    path('budgets/create/', budget_create, name='budget_create'),
    path('budgets/<int:pk>/edit/', budget_update, name='budget_update'),
    path('budgets/<int:pk>/delete/', budget_delete, name='budget_delete'),

    path('accounts/', account_list, name='account_list'),
    path('accounts/<int:pk>/', account_detail, name='account_detail'),
    path('accounts/create/', account_create, name='account_create'),
    path('accounts/<int:pk>/edit/', account_update, name='account_update'),
    path('accounts/<int:pk>/delete/', account_delete, name='account_delete'),

    path('bankaccounts/', bankaccount_list, name='bankaccount_list'),
    path('bankaccounts/<int:pk>/', bankaccount_detail, name='bankaccount_detail'),
    path('bankaccounts/create/', bankaccount_create, name='bankaccount_create'),
    path('bankaccounts/<int:pk>/edit/', bankaccount_update, name='bankaccount_update'),
    path('bankaccounts/<int:pk>/delete/', bankaccount_delete, name='bankaccount_delete'),
]

