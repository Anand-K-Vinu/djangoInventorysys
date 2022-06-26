from django.db import models
from django.contrib.auth.models import User

Category = (
    ('food', 'food'),
    ('sport', 'sport'),
    ('adventure', 'adventure'),
)


# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=30, choices=Category, null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f' {self.name}-{self.quantity}'


class order(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'

