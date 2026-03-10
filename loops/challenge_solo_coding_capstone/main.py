# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

for item in inventory:
    current_stock = inventory[item][0]
    regular_price = inventory[item][1]
    discounted_price = inventory[item][2]
    if current_stock < 30:
        print(f"{item} need restocking.")
    if current_stock > 100:
        print(f"{item} should be sold at the discounted price of {discounted_price}.")
    if current_stock in range(30, 100):
        print(f"{item} should be sold at the regular price of {regular_price}.")