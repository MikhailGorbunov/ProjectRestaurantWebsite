import unittest
from models.customer import Customer
import datetime

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Mikhail", "Gorbunov", "mikhail@gmail.com", 4, "2022-12-01 12:00:00")


    def test_customer_has_first_name(self):
        self.assertEqual("Mikhail", self.customer.first_name)
    def test_customer_has_last_name(self):
        self.assertEqual("Gorbunov", self.customer.last_name)
    def test_customer_has_email(self):
        self.assertEqual("mikhail@gmail.com", self.customer.email)
    def test_customer_has_number_of_people(self):
        self.assertEqual(4, self.customer.number)
    def test_customer_has_time_slot(self):
        self.assertEqual("2022-12-01 12:00:00", self.customer.time_slot)