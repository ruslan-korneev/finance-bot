from django.db import models


CURRENCY_CHOICES = (
    ('RUR', 'RUR'),
    ('USD', 'USD'),
    ('EUR', 'EUR'),
    ('CZK', 'CZK'),
)


class Name(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'names'


class Income(models.Model):
    name = models.ManyToManyField(
        Name,
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
