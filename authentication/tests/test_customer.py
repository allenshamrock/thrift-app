from django.test import TestCase
from authentication.models import Customer


class TestCustomerModel(TestCase):
    """
    Things to test:-
    1.Can create a customer with bare minimum od fields ?(username & phone number)
    2.Is unique code automatically generated when not provided?
    3.Does the __str__ method behaves as expected?
    4.Is the username field unique?
    5.Does the username field save correctly?
    6.If code provided it should'nt be overwritten
    """
    @classmethod
    def setUpTestData(cls):
        cls.customer = Customer.objects.create(
            username='Allen',
            phone_number='+2547 577 726 01'
        )

    def test_create_customer(self):
        """Test a customer with username & phone number can be created"""
        self.assertEqual(self.customer.username, "Allen")
        self.assertEqual(self.customer.phone_number, "+2547 577 726 01")

    def test_code_is_generated_if_not_provided(self):
        """Test that the code is automatically generated if not provided"""
        self.assertIsNotNone(self.customer.code)
        self.assertEqual(len(self.customer.code), 5)

    def test_code_is_not_overridden(self):
        """Test for the event that the code is provided,it shouldn't be overwrriten"""
        customer_code = Customer.objects.create(
            username='Allen Shamrock',
            phone_number='+2547 577 726 01',
            code='XYZ10'
        )
        self.assertEqual(customer_code.code, 'XYZ10')

    def test_str_method(self):
        self.assertEqual(str(self.customer), 'Allen')

    def test_username_uniqueness(self):
        """Test that username must be unique"""
        with self.assertRaises(Exception):
            Customer.objects.create(
                username='Allen',
                phone_number='+2547 577 726 01'
            )

    def test_phone_number_is_corrcetly_saved(self):
        self.assertEqual(self.customer.phone_number, '+2547 577 726 01')
