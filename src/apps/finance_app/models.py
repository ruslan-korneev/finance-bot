from django.db import models


CURRENCY_CHOICES = (
    ('RUR', 'RUR'),
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('CZK', 'CZK'),
)


class Income(models.Model):
    name = models.CharField(max_length=255)
    amount = models.FloatField()
    currency = models.CharField(max_length=255,
                                choices=CURRENCY_CHOICES,
                                default='RUR')
    date_income = models.DateTimeField(auto_now_add=True,
                                       editable=False,
                                       blank=True)
