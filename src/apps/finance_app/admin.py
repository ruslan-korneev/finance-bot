from django.contrib import admin
from apps.finance_app.models import Income


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'currency', 'date_income')
    list_filter = ('date_income', 'currency', 'amount')
