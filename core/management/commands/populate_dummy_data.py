from django.core.management.base import BaseCommand
from core.models import Entity, Budget, BudgetTransaction, Account, GeneralLedger, BankAccount, CashFlow

class Command(BaseCommand):
    help = 'Populates the database with dummy data for prototyping'

    def handle(self, *args, **kwargs):
        # Populating Entity data
        entities = [
            {"name": "Department of Education", "government_level": "Federal"},
            {"name": "Department of Health", "government_level": "State"},
            {"name": "Department of Transportation", "government_level": "State"},
        ]
        for entity in entities:
            Entity.objects.create(**entity)

        # Populating Budget data
        budgets = [
            {"fiscal_year": 2024, "entity_id": 1, "amount_allocated": 5000000, "amount_spent": 1500000, "amount_remaining": 3500000},
            {"fiscal_year": 2024, "entity_id": 2, "amount_allocated": 7500000, "amount_spent": 2500000, "amount_remaining": 5000000},
            {"fiscal_year": 2024, "entity_id": 3, "amount_allocated": 6000000, "amount_spent": 2000000, "amount_remaining": 4000000},
        ]
        for budget in budgets:
            Budget.objects.create(**budget)

        # Populating BudgetTransaction data
        budget_transactions = [
            {"budget_id": 1, "date": "2024-01-15", "amount": 100000, "transaction_type": "Expenditure"},
            {"budget_id": 2, "date": "2024-02-10", "amount": 200000, "transaction_type": "Expenditure"},
            {"budget_id": 3, "date": "2024-03-05", "amount": 150000, "transaction_type": "Expenditure"},
        ]
        for transaction in budget_transactions:
            BudgetTransaction.objects.create(**transaction)

        # Populating Account data
        accounts = [
            {"name": "Cash", "account_type": "Asset", "parent_account_id": None},
            {"name": "Accounts Payable", "account_type": "Liability", "parent_account_id": None},
            {"name": "Revenue", "account_type": "Income", "parent_account_id": None},
        ]
        for account in accounts:
            Account.objects.create(**account)

        # Populating GeneralLedger data
        general_ledgers = [
            {"account_id": 1, "date": "2024-01-05", "debit": 500000, "credit": 0, "balance": 500000, "entity_id": 1},
            {"account_id": 2, "date": "2024-01-15", "debit": 0, "credit": 100000, "balance": -100000, "entity_id": 2},
            {"account_id": 3, "date": "2024-01-31", "debit": 0, "credit": 200000, "balance": 200000, "entity_id": 3},
        ]
        for ledger in general_ledgers:
            GeneralLedger.objects.create(**ledger)

        # Populating BankAccount data
        bank_accounts = [
            {"bank_name": "National Bank", "account_number": "1234567890", "balance": 1000000, "entity_id": 1},
            {"bank_name": "City Bank", "account_number": "9876543210", "balance": 500000, "entity_id": 2},
        ]
        for bank_account in bank_accounts:
            BankAccount.objects.create(**bank_account)

        # Populating CashFlow data
        cash_flows = [
            {"date": "2024-01-10", "amount": 300000, "flow_type": "Inflow", "account_id": 1, "entity_id": 1},
            {"date": "2024-01-11", "amount": 300000, "flow_type": "Outflow", "account_id": 2, "entity_id": 2},
            {"date": "2024-02-05", "amount": 50000, "flow_type": "Outflow", "account_id": 1, "entity_id": 1},
        ]
        for cash_flow in cash_flows:
            CashFlow.objects.create(**cash_flow)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with dummy data'))
