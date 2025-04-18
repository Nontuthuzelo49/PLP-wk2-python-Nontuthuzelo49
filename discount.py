def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (price * discount_percent) / 100
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Test the function:
original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price after applying the discount
final_price = calculate_discount(original_price, discount_percent)
if final_price < original_price:
    print(f"The final price after applying the discount is: {final_price:.2f}")
else:
    print(f"No discount applied, The original price is: {original_price:.2f}")


