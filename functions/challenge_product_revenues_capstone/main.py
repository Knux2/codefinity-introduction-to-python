# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
revenue = []

def calculate_revenue(prices, quantities_sold):
    revenue_for_product_list = []
    for p, q in zip(prices, quantities_sold):
        revenue_for_product = p * q
        revenue_for_product_list.append(revenue_for_product)
    return revenue_for_product_list

calculated_revenue = calculate_revenue(prices, quantities_sold)
revenue.extend(calculated_revenue)

revenue_per_product = list(zip(products, revenue))

def formatted_output(products_and_revenue):
    for name, rev in sorted(products_and_revenue):
        print(f"{name} has total revenue of ${rev}")

formatted_output(revenue_per_product)
