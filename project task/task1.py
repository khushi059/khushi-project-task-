def get_positive_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            if num <= 0:
                print("Please enter a positive number.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_y_or_n(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input == 'y' or user_input == 'n':
            return user_input
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            
def calculate_total_price(num_pizzas, is_tuesday, is_delivery, is_app_order):
    pizza_price = 12.00
    delivery_cost = 2.50
    discount_tuesday = 0.50
    discount_app_order = 0.25

    total_pizza_price = num_pizzas * pizza_price
    
    if is_tuesday == "y":
        total_pizza_price *= (1 - discount_tuesday)

    if num_pizzas >= 5:
        delivery_cost = 0.00
    if is_delivery == "y":
        total_delivery_cost = delivery_cost
    else:
        total_delivery_cost = 0.00
    
    total_price = total_pizza_price + total_delivery_cost
    
    if is_app_order == "y":
        total_price *= (1 - discount_app_order)

    return total_price


def main():
    print("BPP Pizza Price Calculator")
    print("==========================")
    num_pizzas = get_positive_number("How many pizzas ordered? ")
    is_tuesday = get_y_or_n("Is it Tuesday? ")
    is_delivery = get_y_or_n("Is delivery required? ")
    is_app_order = get_y_or_n("Did the customer use the app? ")

    total_price = calculate_total_price(num_pizzas, is_tuesday, is_delivery, is_app_order)
    print("\n")
    print(f"Total price: £{total_price:.2f}")


if __name__ == "__main__":
    main()
