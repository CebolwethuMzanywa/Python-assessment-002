import unittest
import os
from analytics import (
    filter_sales_above_threshold,
    count_product_codes,
    calculate_moving_average,
    get_top_seller,
    merge_inventory,
    check_inventory_status
)

class TestAnalytics(unittest.TestCase):

    def test_00_tdd_file_exists(self):
        print("\nGrading Pre-Check: Looking for student test file...")
        file_exists = os.path.exists("test_inventory.py")
        
        self.assertTrue(
            file_exists, 
            msg="❌ FAILED: 'test_inventory.py' was not found. Did you create the file?"
        )
        print("✅ FOUND: 'test_inventory.py' exists.")

    # ==========================================
    # SECTION A: LIST PROCESSING
    # ==========================================

    def test_q1_filter_sales_basic(self):
        print("Grading Q1: Filter Sales Above Threshold (Basic)...")
        self.assertEqual(
            filter_sales_above_threshold([100, 250, 75, 300], 150),
            [250, 300]
        )

    def test_q1_filter_sales_edge_cases(self):
        print("Grading Q1: Filter Sales Above Threshold (Edge Cases)...")
        self.assertEqual(filter_sales_above_threshold([50, 60, 70], 100), [])
        self.assertEqual(filter_sales_above_threshold([200, 300, 400], 150), [200, 300, 400])
        self.assertEqual(filter_sales_above_threshold([], 100), [])

    def test_q2_count_product_codes_basic(self):
        print("Grading Q2: Count Product Codes (Basic)...")
        self.assertEqual(
            count_product_codes(["PROD-001", "PROD-002", "SERV-001"], "PROD"),
            2
        )

    def test_q2_count_product_codes_edge_cases(self):
        print("Grading Q2: Count Product Codes (Edge Cases)...")
        self.assertEqual(count_product_codes(["PROD-001", "PROD-002"], "SERV"), 0)
        self.assertEqual(count_product_codes([], "PROD"), 0)
        self.assertEqual(count_product_codes(["ABC", "ABD", "XYZ"], "AB"), 2)

    def test_q3_moving_average_basic(self):
        print("Grading Q3: Calculate Moving Average (Basic)...")
        self.assertEqual(calculate_moving_average([10, 20, 30, 40, 50], 3), 40.0)

    def test_q3_moving_average_edge_cases(self):
        print("Grading Q3: Calculate Moving Average (Edge Cases)...")
        self.assertEqual(calculate_moving_average([10, 20], 5), 15.0)
        self.assertEqual(calculate_moving_average([100], 1), 100.0)
        self.assertEqual(calculate_moving_average([], 3), 0.0)
        self.assertEqual(calculate_moving_average([5, 10, 15, 20], 2), 17.5)

    # ==========================================
    # SECTION B: DICTIONARY OPERATIONS
    # ==========================================

    def test_q4_top_seller_basic(self):
        print("Grading Q4: Get Top Seller (Basic)...")
        self.assertEqual(
            get_top_seller({"Alice": 5000, "Bob": 7500, "Carol": 6000}),
            "Bob"
        )

    def test_q4_top_seller_edge_cases(self):
        print("Grading Q4: Get Top Seller (Edge Cases)...")
        self.assertEqual(get_top_seller({}), "No Data")
        self.assertEqual(get_top_seller({"Alice": 5000}), "Alice")
        # Tie - should return alphabetically first
        self.assertEqual(get_top_seller({"Bob": 5000, "Alice": 5000}), "Alice")

    def test_q5_merge_inventory_basic(self):
        print("Grading Q5: Merge Inventory (Basic)...")
        warehouse_a = {"PROD-001": 50, "PROD-002": 30}
        warehouse_b = {"PROD-002": 20, "PROD-003": 40}
        expected = {"PROD-001": 50, "PROD-002": 50, "PROD-003": 40}
        self.assertEqual(merge_inventory(warehouse_a, warehouse_b), expected)

    def test_q5_merge_inventory_edge_cases(self):
        print("Grading Q5: Merge Inventory (Edge Cases)...")
        self.assertEqual(merge_inventory({}, {}), {})
        self.assertEqual(
            merge_inventory({"PROD-001": 100}, {}),
            {"PROD-001": 100}
        )
        self.assertEqual(
            merge_inventory({}, {"PROD-001": 50}),
            {"PROD-001": 50}
        )
        # No overlap
        self.assertEqual(
            merge_inventory({"PROD-001": 10}, {"PROD-002": 20}),
            {"PROD-001": 10, "PROD-002": 20}
        )

    # ==========================================
    # SECTION C: INVENTORY MANAGEMENT
    # ==========================================

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

if __name__ == '__main__':
    unittest.main(failfast=True, verbosity=2)
