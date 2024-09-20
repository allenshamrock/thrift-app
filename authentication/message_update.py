import africastalking
from dotenv import load_dotenv
import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order, Customer

load_dotenv()

# Africastalking credentials
username = os.getenv('USERNAME')
api_key = os.getenv('SMS_API_KEY')
sender_id = os.getenv('SENDER_ID')

# Initialize Africastalking
africastalking.initialize(username, api_key)
sms = africastalking.SMS



def send_sms_on_order(order_instance):
    customers = Customer.objects.all()
    for customer in customers:
        order_message = f"Hello {customer.username}, a new order has been placed: {order_instance.item}. Please check your account."
        response = sms.send(order_message, [str(customer.phone_number)])
        print(response)

# Signal to trigger SMS sending after order is saved
@receiver(post_save, sender=Order)
def order_created_handler(sender, instance, created, **kwargs):
    if created:  
        send_sms_on_order(instance)
