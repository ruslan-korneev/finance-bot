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


class NameExpense(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'expense_names'


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


class NameAsset(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'asset_names'


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
