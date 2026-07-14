# ============================================================================
# SQL SELECT LAB - COMPLETE SOLUTION
# ============================================================================

# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")

# Reference: View all employee data
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")

# ============================================================================
# STEP 2
# Select employee number and last name from all employees
# ============================================================================
df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName 
FROM employees
""", conn)

# ============================================================================
# STEP 3
# Same as Step 2, but last name comes BEFORE employee number
# ============================================================================
df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber 
FROM employees
""", conn)

# ============================================================================
# STEP 4
# Same as Step 3, but alias employeeNumber as 'ID'
# ============================================================================
df_alias = pd.read_sql("""
SELECT lastName, employeeNumber AS ID 
FROM employees
""", conn)

# ============================================================================
# STEP 5
# Use CASE to classify job titles as "Executive" or "Not Executive"
# ============================================================================
df_executive = pd.read_sql("""
SELECT 
    *,
    CASE 
        WHEN jobTitle = 'President' 
             OR jobTitle = 'VP Sales' 
             OR jobTitle = 'VP Marketing' 
        THEN 'Executive'
        ELSE 'Not Executive'
    END AS role
FROM employees
""", conn)

# ============================================================================
# STEP 6
# Find the length of each employee's last name
# ============================================================================
df_name_length = pd.read_sql("""
SELECT LENGTH(lastName) AS name_length 
FROM employees
""", conn)

# ============================================================================
# STEP 7
# Return the first two letters of each person's job title
# ============================================================================
df_short_title = pd.read_sql("""
SELECT SUBSTR(jobTitle, 1, 2) AS short_title 
FROM employees
""", conn)

# ============================================================================
# Reference: View order details data
# ============================================================================
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn) 
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# ============================================================================
# STEP 8
# Find the total amount for all orders
# Use SQL SUM() directly, then extract the scalar value into a list
# so that sum_total_price[0] works in the test.
# ============================================================================
sum_total_price = pd.read_sql("""
SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total_price
FROM orderDetails
""", conn).values.flatten()

# ============================================================================
# STEP 9
# The orderDate is NOT in orderDetails — it's in the orders table.
# ============================================================================
df_day_month_year = pd.read_sql("""
SELECT 
    orderDate,
    strftime('%d', orderDate) AS day,
    strftime('%m', orderDate) AS month,
    strftime('%Y', orderDate) AS year
FROM orders
""", conn)

# ============================================================================
# Close the connection
# ============================================================================
conn.close()