import unittest
from models.waiter import Waiter

class TestWaiter(unittest.TestCase):
    def setUp(self):
        self.waiter = Waiter(OLEG, SEMENOV, 2)
        Waiter(f_name, l_name, table_capacity)

    def test_waiter_has_name(self):
        self.assertEqual("OLEG", self.waiter.f_name)
    def test_waiter_has_surname(self):
        self.assertEqual("Gorbunov", self.waiter.l_name)
    def test_waiter_has_table_capacity(self):
        self.assertEqual(2, self.waiter.table_capacity)
