import unittest
from analytics import check_inventory_status
class TestInventory(unittest.TestCase):
    def test_q6_inventory_invalid_input(self):
        print("Grading Q6: Inventory Status (Invalid Input)...")
        self.assertEqual(check_inventory_status(-10, 50, 100, 10), "Invalid Input")
        self.assertEqual(check_inventory_status(50, -10, 100, 10), "Invalid Input")
        self.assertEqual(check_inventory_status(50, 50, -100, 10), "Invalid Input")
        self.assertEqual(check_inventory_status(50, 50, 100, -10), "Invalid Input")
        self.assertEqual(check_inventory_status(150, 50, 100, 10), "Invalid Input")

    def test_q6_inventory_overstocked(self):
        print("Grading Q6: Inventory Status (Overstocked)...")
        self.assertEqual(check_inventory_status(95, 50, 100, 10), "OVERSTOCKED")
        self.assertEqual(check_inventory_status(91, 50, 100, 10), "OVERSTOCKED")

    def test_q6_inventory_critical(self):
        print("Grading Q6: Inventory Status (Critical)...")
        self.assertEqual(check_inventory_status(20, 50, 100, 10), "CRITICAL")
        self.assertEqual(check_inventory_status(10, 100, 200, 5), "CRITICAL")

    def test_q6_inventory_reorder(self):
        print("Grading Q6: Inventory Status (Reorder)...")
        self.assertEqual(check_inventory_status(50, 50, 100, 5), "REORDER")
        self.assertEqual(check_inventory_status(45, 50, 100, 5), "REORDER")

    def test_q6_inventory_low_stock(self):
        print("Grading Q6: Inventory Status (Low Stock)...")
        self.assertEqual(check_inventory_status(60, 50, 100, 10), "LOW STOCK")
        self.assertEqual(check_inventory_status(69, 50, 100, 10), "LOW STOCK")

    def test_q6_inventory_optimal(self):
        print("Grading Q6: Inventory Status (Optimal)...")
        self.assertEqual(check_inventory_status(70, 50, 100, 10), "OPTIMAL")
        self.assertEqual(check_inventory_status(80, 50, 100, 5), "OPTIMAL")
        # Zero daily sales should not trigger low stock
        self.assertEqual(check_inventory_status(60, 50, 100, 0), "OPTIMAL")