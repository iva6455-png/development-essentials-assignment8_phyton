product = input("Product name: ")
purchase_price = float(input("Purchase price per unit: "))
sale_price = float(input("Sale price per unit: "))
quantity = int(input("Quantity: "))

revenue = sale_price * quantity
cost = purchase_price * quantity
profit = revenue - cost

print("\nProduct:", product)
print("Revenue:", round(revenue, 2))
print("Total cost:", round(cost, 2))
print("Profit:", round(profit, 2))

if revenue != 0:
    margin = profit / revenue * 100
    print("Margin:", round(margin, 2), "%")
else:
    print("Margin cannot be calculated: revenue is zero.")

print("Profitable:", profit > 0)
