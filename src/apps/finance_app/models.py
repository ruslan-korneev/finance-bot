from django.db import models


CURRENCY_CHOICES = (
    ('RUR', 'RUR'),
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('CZK', 'CZK'),
)


class NameIncome(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'income_names'
        verbose_name = 'Name Income'
        verbose_name_plural = 'Names Incomes'


class Income(models.Model):
    name = models.ManyToManyField(
        NameIncome,
        blank=True)
    amount = models.FloatField()
    currency = models.CharField(max_length=255,
                                choices=CURRENCY_CHOICES,
                                default='RUR')
    date_income = models.DateTimeField(auto_now_add=True,
                                       editable=False,
                                       blank=True)

    def __str__(self):
        return f'{self.name.all()[0]} +{self.amount}{self.currency}'
    class Meta:
        db_table = 'incomes'
        verbose_name = 'Income'
        verbose_name_plural = 'Incomes'


class NameExpense(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'expense_names'
        verbose_name = 'Name Expense'
        verbose_name_plural = 'Names Expenses'


class Expense(models.Model):
    name = models.ManyToManyField(
        NameExpense,
        blank=True)
    amount = models.FloatField()
    currency = models.CharField(max_length=255,
                                choices=CURRENCY_CHOICES,
                                default='RUR')
    date_expense = models.DateTimeField(auto_now_add=True,
                                        editable=False,
                                        blank=True)

    def __str__(self):
        return f'{self.name.all()[0]} -{self.amount}{self.currency}'
    class Meta:
        db_table = 'expenses'
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'


class NameAsset(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'asset_names'
        verbose_name = 'Name Asset'
        verbose_name_plural = 'Names Assets'


class Asset(models.Model):
    name = models.ManyToManyField(
        NameAsset,
        blank=True)
    amount = models.FloatField()
    currency = models.CharField(max_length=255,
                                choices=CURRENCY_CHOICES,
                                default='RUR')
    date_purchase = models.DateTimeField(auto_now_add=True,
                                       editable=False,
                                       blank=True)

    def __str__(self):
        return f'{self.name.all()[0]} -{self.amount}{self.currency}'
    class Meta:
        db_table = 'assets'
        verbose_name = 'Asset'
        verbose_name_plural = 'Assets'


class NameLiability(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'liability_names'
        verbose_name = 'Name Liability'
        verbose_name_plural = 'Names Liabilities'


class Liability(models.Model):
    name = models.ManyToManyField(
        NameLiability,
        blank=True)
    amount = models.FloatField()
    currency = models.CharField(max_length=255,
                                choices=CURRENCY_CHOICES,
                                default='RUR')
    date_purchase = models.DateTimeField(auto_now_add=True,
                                       editable=False,
                                       blank=True)

    def __str__(self):
        return f'{self.name.all()[0]} -{self.amount}{self.currency}'
    class Meta:
        db_table = 'liabilities'
        verbose_name = 'Liability'
        verbose_name_plural = 'Liabilities'
