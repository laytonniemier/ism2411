"""
Reflection:
1. What is the most surprising thing about how lists work in Python compared to what you expected coming in?
 I am surprised at how easy it is to add and remove things to the same list.

2. Describe one real business situation — from a job you've had, an internship, or a class — where a Python list would have saved you time compared to doing it manually in Excel.
I perosnally did not have an issue with any of this because I worked at chick fil a for my first job but i know that in retail, it is very difficult to keep track of inventory because they have to recount inventory by hand.  The reason why is because if someone steals something, a computer cannot calculate this but it would make the overall process so much easier to count inventory. """

# ==========================================
# EXERCISE 1 · Beginner: Build the list
# ==========================================
print("--- Exercise 1 ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory, "|", len(inventory))
print()


# ==========================================
# EXERCISE 2 · Beginner: Index practice
# ==========================================
print("--- Exercise 2 ---")
first_item = inventory[0]                  # Positive index for first item
last_item = inventory[-1]                  # Negative index for last item
middle_index = len(inventory) // 2         # Compute middle index dynamically
middle_item = inventory[middle_index]

print(f"{first_item} | {last_item} | {middle_item}")
print()


# ==========================================
# EXERCISE 3 · Beginner: Slicing
# ==========================================
print("--- Exercise 3 ---")
first_three = inventory[:3]
last_two = inventory[-2:]
every_other = inventory[::2]

print(f"{first_three} | {last_two} | {every_other}")
print()


# ==========================================
# EXERCISE 4 · Intermediate: Modify
# ==========================================
print("--- Exercise 4 ---")
print("Initial:", inventory)

inventory.append("envelope")
print("After append('envelope'):", inventory)

inventory.remove("tape")
print("After remove('tape'):", inventory)

inventory.sort()
print("After sort():", inventory)
print()


# ==========================================
# EXERCISE 5 · Intermediate: Tuple comparison
# ==========================================
print("--- Exercise 5 ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as e:
    print("TypeError caught successfully:", e)
    print("Explanation: Tuples are immutable, which is useful for coordinates because it protects critical, constant data from accidental modification during program execution.")

print("Original coords unchanged:", coords)
print()


# ==========================================
# EXERCISE 6 · Intermediate: Average of a list of sales
# ==========================================
print("--- Exercise 6 ---")
sales = [100, 250, 75, 480, 200]

total_sales = sum(sales)
count_sales = len(sales)
average_sales = total_sales / count_sales
best_day = max(sales)
worst_day = min(sales)

print(f"Total: {total_sales} | Average: {average_sales} | Best: {best_day} | Worst: {worst_day}")
print()


# ==========================================
# EXERCISE 7 · Intermediate: Accumulator pattern
# ==========================================
print("--- Exercise 7 ---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted_price = round(price * 0.9, 2)
    discounted.append(discounted_price)

print("Original prices:", prices)
print("Discounted prices:", discounted)
print()


# ==========================================
# EXERCISE 8 · Advanced: Filter above threshold
# ==========================================
print("--- Exercise 8 ---")
sales_data = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales_data:
    if sale > 300:
        high_sales.append(sale)

high_count = len(high_sales)
high_avg = sum(high_sales) / high_count if high_count > 0 else 0

print(f"{high_sales} | Count: {high_count} | Avg: ~{high_avg:.2f}")