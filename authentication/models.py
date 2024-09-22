from django.db import models
import random
import string
from django.core.exceptions import ValidationError

class Customer(models.Model):
    username = models.CharField(
        max_length=20, null=False, unique=True, default='')
    phone_number = models.CharField(max_length=15)
    code = models.CharField(max_length=5, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.code:  
            self.code = ''.join(random.choices(
                string.ascii_uppercase + string.digits, k=5))
        super(Customer, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.username


class Order(models.Model):
    item = models.CharField(max_length=20)
    amount = models.PositiveIntegerField()
    time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)

    def clean(self):
        if self.amount <= 0:
            raise ValidationError(
                {'amount': 'Amount must be a positive integer'})
            
    def __str__(self) -> str:
        return self.item
