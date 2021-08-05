from django.contrib import admin
from apps.finance_app.models import (
    Income,
    NameIncome,
    Expense,
    NameExpense,
    Asset,
    NameAsset,
    Liability,
    NameLiability,
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


@admin.register(NameAsset)
class NameAssetAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_purchase')
    list_filter = ('date_purchase', 'currency', 'amount')


@admin.register(NameLiability)
class NameLiabilityAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(Liability)
class LiabilityAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_purchase')
    list_filter = ('date_purchase', 'currency', 'amount')
