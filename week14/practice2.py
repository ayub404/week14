items = ["Apple", "Banana", "Cherry"]
prices = [0.50, 0.30, 0.10]
quantities = [4, 2, 10]

total = 0
for line_num, (item, price, amount) in enumerate(zip(items, prices, quantities)):
    sub_total = price * amount
    print(f"Line #{line_num}: {item} x{amount} = ${sub_total}")
    total += sub_total
print("-" * 60)
print(f"Grand Total: ${total}")