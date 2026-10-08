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

print("\n--- Additional analysis by zucksa ---")

profit_per_unit = sale_price - purchase_price
print("Profit per unit:", round(profit_per_unit, 2))

if purchase_price != 0:
    markup = profit_per_unit / purchase_price * 100
    print("Markup:", round(markup, 2), "%")
else:
    print("Markup cannot be calculated: purchase price is zero.")
