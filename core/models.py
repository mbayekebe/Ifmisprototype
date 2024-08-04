from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

class Entity(models.Model):
    name = models.CharField(max_length=100)
    government_level = models.CharField(max_length=50)  # e.g., Federal, State

    def __str__(self):
        return self.name

class Budget(models.Model):
    fiscal_year = models.IntegerField()
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    amount_allocated = models.DecimalField(max_digits=15, decimal_places=2)
    amount_spent = models.DecimalField(max_digits=15, decimal_places=2)
    amount_remaining = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f'{self.entity.name} - {self.fiscal_year}'

class BudgetTransaction(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.transaction_type} - {self.amount}'


class Account(models.Model):
    name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=50)
    parent_account = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class GeneralLedger(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField()
    debit = models.DecimalField(max_digits=15, decimal_places=2)
    credit = models.DecimalField(max_digits=15, decimal_places=2)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.account.name} - {self.date}'

class BankAccount(models.Model):
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.bank_name} - {self.account_number}'

class CashFlow(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    flow_type = models.CharField(max_length=50)
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.flow_type} - {self.amount}'
    