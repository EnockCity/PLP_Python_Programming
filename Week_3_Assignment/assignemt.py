#!/usr/bin/python3

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price


def main():
    # Prompt the user to enter the original price and discount percentage
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage(0-100): "))
    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percent)
    # Print final price after applying the discount
    # or original price if no discount was applied
    if final_price != original_price:
        print("Final price after applying discount: $", final_price)
    else:
        print("No discount applied. Original price: $", original_price)


if __name__ == "__main__":
    main()
