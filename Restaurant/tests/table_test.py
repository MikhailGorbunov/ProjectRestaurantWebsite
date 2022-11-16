import unittest
from models.table import Table

class TestTable(unittest.TestCase):
    def setUp(self):
        self.table = Table(4, "Mikhail","OLEG")

    def test_table_has_capacity(self):
        self.assertEqual(4, self.table.capacity)
    def test_table_has_customer_name(self):
        self.assertEqual("Mikhail", self.table.customer)
    def test_table_has_waiters_name(self):
        self.assertEqual("OLEG", self.table.waiter)

