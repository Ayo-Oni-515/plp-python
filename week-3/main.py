# calculate_discount function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return (price * discount_percent) / 100
    return price


# take in user input
def main():
    price = float(input('Enter the price: '))
    discount_percent = float(input('Enter the discount percentage: '))

    if price == discount_percent == -1:
        return

    return calculate_discount(price, discount_percent)


if __name__ == "__main__":
    while True:
        print("Dicount price calculator (Enter -1 twice to quit)")
        discount = main()

        if discount:
            print(f"Discount is {discount}")
            print("\n")
        else:
            print("Bye")
            break
