from django.contrib import admin
from apps.finance_app.models import Income, Name


@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_income')
    list_filter = ('date_income', 'currency', 'amount')
