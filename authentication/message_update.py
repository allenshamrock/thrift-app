# import re
# from django.db.models.signals import post_save
# from django.dispatch import receiver
import africastalking
from dotenv import load_dotenv
import os
# import datetime
from .models import  Customer

load_dotenv()

# Africastalking credentials
username = os.getenv('USERNAME')
api_key = os.getenv('SMS_API_KEY')
sender_id = os.getenv('SENDER_ID')

# Initialize Africastalking
africastalking.initialize(username, api_key)
sms = africastalking.SMS




def send_sms_on_order(instance):
    customers = Customer.objects.all()
    for customer in customers:
        order_message = f"Hello {customer.username}, a new order has been placed: {instance.item}. Please check your account."
        response = sms.send(order_message, [str(customer.phone_number)])
        print(response)

# @receiver(post_save, sender=Order)
# def send_sms_on_order(sender, instance, created, **kwargs):
#     if created:
#         customers = Customer.objects.all()
#         for customer in customers:
#             # Validate and format phone number
#             phone_number = format_phone_number(customer.phone_number)
#             if not phone_number:
#                 print(
#                     f"Invalid phone number for {customer.username}: {customer.phone_number}")
#                 continue  # Skip to the next customer

#             message = f"Hello {customer.username}, a new order has been placed: {instance.item}. Please check your account."
#             current_time = datetime.datetime.now()

#             try:
#                 response = sms.send(
#                     message, [phone_number], sender_id=sender_id)
#                 if response['status'] == 'success':
#                     print(
#                         f"SMS sent to {phone_number} at {current_time}: {response}")
#                 else:
#                     print(
#                         f"Failed to send SMS to {phone_number} at {current_time}: {response}")
#             except Exception as e:
#                 print(f"Error sending SMS to {phone_number}: {e}")



# # Helper function to validate and format phone numbers
# def format_phone_number(phone_number):
#     # Ensure the phone number has a country code
#     if not phone_number.startswith('+'):
#         # If the number doesn't start with a country code, prepend the default country code
#         phone_number = COUNTRY_CODE + phone_number.lstrip('0')

#     # Validate the phone number (basic check for 10-12 digits with country code)
#     pattern = r'^\+\d{10,12}$'
#     if re.match(pattern, phone_number):
#         return phone_number
#     return None
