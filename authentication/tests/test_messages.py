from django.test import TestCase
# from unittest.mock import Mock
from unittest.mock import patch
from authentication.models import Customer,Order
from authentication.message_update import send_sms_on_order


class OrderSMSTexts(TestCase):
    """THings to test:
    1.If sms is executed on order creation,
    2.If the order triggers an sms 
    3.THe response from the Api 
    """
    def setUp(self):
        # creating a customer
        self.customer = Customer.objects.create(
            username = 'Mikel',
            phone_number = '+2547123456789'
        )

    @patch('authentication.message_update.sms.send')
    def test_sms_created_on_order_creation(self,mock_send):
        # create an order
        order = Order.objects.create(
            item = 'Trench Coat',
            amount = 2000,
            customer = self.customer
        )

        self.assertTrue(mock_send.called)
        self.assertEqual(mock_send.call_count,1)

        order_message = f"Hello {self.customer.username}, a new order has been placed: {order.item} at {order.amount}. Please check your account."
        mock_send.assert_called_with(
            order_message, [str(self.customer.phone_number)])
    
    @patch('authentication.message_update.sms.send')  # Mock the send method
    def test_order_created_handler_triggers_sms(self, mock_send):
        # Simulate creating an order which should trigger the SMS
        order = Order.objects.create(
            item='Bicker Jacket', amount=2000, customer=self.customer)

        # Assert that the SMS sending logic was triggered
        self.assertTrue(mock_send.called)

    # Mock the send method
    @patch('authentication.message_update.sms.send', return_value={"SMSMessageData": {"Recipients": [{"number": "+254123456789", "status": "Success", "cost": "1.00", "errorMessage": None}]}})
    def test_sms_response_handling(self, mock_send):
        # Create a new order
        order = Order.objects.create(
            item='Test Item', amount=100, customer=self.customer)

        # Check the response handling in the send_sms_on_order function
        send_sms_on_order(order)

        mock_send.assert_called() #Ensures that you.ve called the mocked method 
