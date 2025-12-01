# ==========================================
# SECTION A: LIST PROCESSING
# ==========================================

def filter_sales_above_threshold(sales: list, threshold: int):
    """
    QUESTION 1
    ----------------------------------------
    Given a list of sales amounts (integers), return a NEW list containing 
    only values above the threshold.
    
    Example: filter_sales_above_threshold([100, 250, 75, 300], 150) → [250, 300]
    
    Logic:
    - Do NOT modify the original list
    - Return empty list if no values qualify
    - Use a loop or list comprehension
    """
    # TODO: Write your code here
    above_treshold = []
    if len(list) == 0:
            return above_treshold
    else:
        for i in list:
         if i > threshold:
               above_treshold.append(i)
    return above_treshold


def count_product_codes(codes: list, prefix: str):
    """
    QUESTION 2
    ----------------------------------------
    Given a list of product codes (strings) and a prefix (string),
    count how many codes START with the given prefix (case-sensitive).
    
    Example: count_product_codes(["PROD-001", "PROD-002", "SERV-001"], "PROD") → 2
    
    Logic:
    - Return 0 if no matches found
    """
    # TODO: Write your code here
    count = 0
    for string in list:
        if prefix in string:
            count += 1
    return count

def calculate_moving_average(numbers: list, window_size: int):
    """
    QUESTION 3
    ----------------------------------------
    Calculate the average of the LAST window_size elements in the list.
    
    Example: calculate_moving_average([10, 20, 30, 40, 50], 3) → 40.0
    (average of last 3: 30, 40, 50)
    
    Logic:
    - If the list has fewer elements than window_size, use all available elements
    - Return the average as a float rounded to 2 decimal places
    - Return 0.0 for empty list
    """
    # TODO: Write your code here
    count = 0
    if len(numbers) == 0:
        return 0.0
    elif len(numbers) >= 3:
        for i in range(-window_size, 0):
         count += numbers[i]
         average = count/window_size
        return f"{average:.2f}"
    else:
        for i in numbers:
            count += i
            average = count/len(numbers)
        return f"{average:.2f}"


# ==========================================
# SECTION B: DICTIONARY OPERATIONS
# ==========================================

def get_top_seller(sales_data: dict):
    """
    QUESTION 4
    ----------------------------------------
    Given a dictionary where keys are employee names and values are sales totals,
    return the NAME of the employee with the highest sales.
    
    Example: {"Alice": 5000, "Bob": 7500, "Carol": 6000} → "Bob"
    
    Logic:
    - If dictionary is empty, return "No Data"
    - If there's a tie, return the name that appears first alphabetically
    """
    # TODO: Write your code here
    max = 0
    if len(sales_data) == 0:
        return f"No Data"
    else:
        for x in sales_data:
            if sales_data[x] > max:
                max = sales_data[x]
        return max


def merge_inventory(warehouse_a: dict, warehouse_b: dict):
    """
    QUESTION 5
    ----------------------------------------
    Given two dictionaries representing product quantities in two warehouses,
    return a NEW dictionary with combined quantities for each product.
    
    Example:
    warehouse_a = {"PROD-001": 50, "PROD-002": 30}
    warehouse_b = {"PROD-002": 20, "PROD-003": 40}
    Result: {"PROD-001": 50, "PROD-002": 50, "PROD-003": 40}
    
    Logic:
    - If a product exists in only one warehouse, include it with its quantity
    - Return empty dictionary if both inputs are empty
    - Do NOT modify the original dictionaries
    """
    # TODO: Write your code here
    new_warehouse = {}
    if warehouse_a and warehouse_b:
        return new_warehouse
    else:
      for a in warehouse_a:
         for b in warehouse_b:
               if a == b:
                  new_warehouse[a] = warehouse_a[a] + warehouse_b[b]
               else:
                  new_warehouse[a] = warehouse_a[a]
                  new_warehouse[b] = warehouse_b[b]
      return new_warehouse
                


# ==========================================
# SECTION C: COMPLEX LOGIC & TDD
# ==========================================

def check_inventory_status(stock_level: int, reorder_point: int, max_capacity: int, daily_sales: int):
    """
    QUESTION 6 (THE INVENTORY MANAGER)
    ----------------------------------------
    Analyze inventory status based on multiple parameters.
    
    TODO: Using TDD, implement tests for the below functionality.
    Create `test_inventory.py` with class `TestInventory`.
    
    Parameters:
    - stock_level: Current units in stock
    - reorder_point: Threshold that triggers reorder
    - max_capacity: Maximum warehouse capacity
    - daily_sales: Average units sold per day
    
    Logic Tree:
    1. INPUT VALIDATION:
       - If ANY parameter is negative: return "Invalid Input"
       - If stock_level > max_capacity: return "Invalid Input"
       
    2. OVERSTOCKED:
       - If stock_level > (max_capacity * 0.9): return "OVERSTOCKED"
       
    3. CRITICAL (Urgent Reorder):
       - If stock_level < (reorder_point * 0.5): return "CRITICAL"
       
    4. REORDER NEEDED:
       - If stock_level <= reorder_point: return "REORDER"
       
    5. LOW STOCK (Warning):
       - If daily_sales > 0 AND stock_level / daily_sales < 7: return "LOW STOCK"
       
    6. OPTIMAL:
       - All other cases: return "OPTIMAL"
    """
    # TODO: Write your code here
    if stock_level < 0 or reorder_point < 0 or max_capacity < 0 or daily_sales < 0:
        return f"Invalid Input"
    elif stock_level > max_capacity:
        return f"Invalid Input"
    elif stock_level > (max_capacity * 0.9):
        f"OVERSTOCKED"
    elif stock_level < (reorder_point*0.5):
        return f"CRITICAL"
    elif stock_level <= reorder_point:
        return f"REORDER"
    elif (daily_sales > 0) and (stock_level < 7 or daily_sales < 7):
        return F"LOW STOCK"
    else:
        return F"OPTIMAL"
    
