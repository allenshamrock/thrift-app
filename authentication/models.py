from django.db import models

class Customer(models.Model):
    username = models.CharField(
        max_length=20, null=False, unique=True, default='')
    phone_number = models.CharField(max_length=15)
    code = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self) -> str:
        return self.username


class Order(models.Model):
    item = models.CharField(max_length=20)
    amount = models.PositiveIntegerField()
    time = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.item
