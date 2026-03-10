prices = [29.99, 45.50, 12.75, 38.20]

for i in range(len(prices)):
    if i == 0:
        prices[i] *= 0.90   # 10% off
    elif i == 1:
        prices[i] *= 0.80   # 20% off
    elif i == 2:
        prices[i] *= 0.85   # 15% off
    elif i == 3:
        prices[i] *= 0.95   # 5% off

    print(f"Updated price for item {i + 1}: ${prices[i]:.2f}")