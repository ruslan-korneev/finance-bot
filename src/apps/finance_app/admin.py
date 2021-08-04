from django.contrib import admin
from apps.finance_app.models import (
    Income,
    NameIncome,
    Expense,
    NameExpense,
)


@admin.register(NameIncome)
class NameIncomeAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_income')
    list_filter = ('date_income', 'currency', 'amount')


@admin.register(NameExpense)
class NameExpenseAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_expense')
    list_filter = ('date_expense', 'currency', 'amount')

