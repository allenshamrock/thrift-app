import re 
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import africastalking
from dotenv import load_dotenv
import os
import datetime


load_dotenv()

# Africastalking credentials
username = os.getenv('USERNAME')
api_key = os.getenv('SMS_API_KEY')

# Initialize Africastalking
africastalking.initialize(username, api_key)
sms = africastalking.SMS


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


# Signal to send SMS when an order is created
@receiver(post_save, sender=Order)
def send_sms_on_order(sender, instance, created, **kwargs):
    if created:
        # Send SMS to all customers
        customers = Customer.objects.all()
        for customer in customers:
            # Validate phone number
            if not is_valid_phone_number(customer.phone_number):
                print(
                    f"Invalid phone number for {customer.username}: {customer.phone_number}")
                continue  # Skip to the next customer

            message = f"Hello {customer.username}, a new order has been placed: {instance.item}. Please check your account."
            current_time = datetime.datetime.now()

            try:
                response = sms.send(message, [customer.phone_number])
                print(
                    f"SMS sent to {customer.phone_number} at {current_time}: {response}")
            except Exception as e:
                print(f"Error sending SMS to {customer.phone_number}: {e}")

# Helper function to validate phone numbers (basic check for 10-12 )
def is_valid_phone_number(phone_number):
    # Basic phone number pattern: + followed by 10-12 digits 
    pattern = r'^\+?\d{10,12}$'
    return re.match(pattern, phone_number) is not None
