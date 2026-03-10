# Call the function and print the result
def calculate_total_cost(price, quantity):
    final_price = price * quantity
    return final_price

apples_total_cost = calculate_total_cost(1.50, 10)

print(f"The total cost for apples is ${apples_total_cost}")