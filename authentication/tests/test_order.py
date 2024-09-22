from django.test import TestCase
from authentication.models import Order, Customer
from django.core.exceptions import ValidationError


class TestOrderModel(TestCase):
    """
    Things to test:
    1.Can an Order be created with minimum required fields?
    2.Does the __str__ method return the correct item name?
    3.Is the time field set correctly?
    4.Is the amount field validated as a positive integer?
    5.If a customer is deleted in the database so do their orders 
    """

    @classmethod
    def setUpTestData(cls):
        cls.customer = Customer.objects.create(
            username='Allen',
            phone_number='+25457772601',
        )

    def test_order_creation(self):
        order = Order.objects.create(
            item='Vans',
            amount=3500,
            customer=self.customer
        )
        self.assertEqual(order.item, 'Vans')
        self.assertEqual(order.amount, 3500)
        self.assertEqual(order.customer, self.customer)

    def test_str_method(self):
        order = Order.objects.create(
            item='Jordans',
            amount=2500,
            customer=self.customer
        )
        self.assertEqual(str(order), 'Jordans')

    def test_time_field_is_auto_generated(self):
        order = Order.objects.create(
            item='Oxfords',
            amount=5000,
            customer=self.customer
        )
        self.assertIsNotNone(order.time)

    def test_amount_is_positive_integer(self):
        """Test for a postive interger in the amount field"""
        order = Order.objects.create(
                item='Converse',
                amount=1500,
                customer=self.customer
            )
        self.assertEqual(order.amount, 1500)


    def test_amount_cannot_be_zero_or_negative(self):
        with self.assertRaises(ValidationError):
            order = Order(item='Test Item', amount=0, customer=self.customer)
            order.full_clean()  

        with self.assertRaises(ValidationError):
            order = Order(item='Test Item', amount=-5, customer=self.customer)
            order.full_clean() 

    def test_foreign_key_relationship(self):
        """Tests for the event a customer is deleted so does their orders"""
        order = Order.objects.create(
            item='Flannel',
            amount=800,
            customer=self.customer
        )
        self.assertEqual(Order.objects.count(), 1)
        self.customer.delete()
        self.assertEqual(Order.objects.count(), 0)
