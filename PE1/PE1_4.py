price = 99.99
discount = 25.0
markdown = discount / 100.0
price *= (1 - markdown)
print("Price =", price)