from django.db import models

# Create your models here.


class User (models.Model):
    username = models.CharField(
        max_length=20, null=False, unique=True, default='')
    code = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self) -> str:
        return self.username


class Order(models.Model):
    item = models.CharField(max_length=20)
    amount = models.PositiveIntegerField()
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.item
