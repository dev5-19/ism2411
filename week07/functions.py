# --- Self-Assessment ---
# 1. The first bug I found was a missing colon in the for loop. I saw it in the error message. This taught me to check the error messages first when my code does not work.
# 2. apply_discount takes a price and a customer tier. It checks the tier and gives the correct discount. Then it returns the new price. Someone else could use it if they know what the inputs mean.
# 3. I used ChatGPT to help me write and understand the code, fix errors, and check my answers. It helped me learn how functions work, but it also made the lab easier to finish.

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate
print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price
print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")

# --- Exercise 3 ---
discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
total = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${total:.2f}")
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax
print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# --- Exercise 5 ---
# Bug 1: Changed total = sale to total += sale so it adds everything.
# Bug 2: Added the missing colon after the for loop.
# Bug 3: Changed <= to < so the loop does not go past the list.
sales = [120, 80, 250, 175, 90]
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")
i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# --- Exercise 6 ---
x = 100
def double_it():
    x = 999
    return x * 2
print(x)
print(double_it())
print(x)
# The x inside the function is different from the x outside.
# Changing x inside the function does not change the original x.

