# Part 1

def calculate_meal_total():
    # Get the cost of the food from the user
    food_cost = float(input("Enter the charge for the food: $"))

    # Define tip and tax rates
    tip_rate = 0.18
    tax_rate = 0.07

    # Calculate the tip and tax amounts
    tip_amount = food_cost * tip_rate
    tax_amount = food_cost * tax_rate

    # Calculate the total amount
    total_amount = food_cost + tip_amount + tax_amount

    # Display the results
    print(f"Cost of the food: ${food_cost:.2f}")
    print(f"Tip (18%): ${tip_amount:.2f}")
    print(f"Tax (7%): ${tax_amount:.2f}")
    print(f"Total amount: ${total_amount:.2f}")

# Call the function to execute the program
calculate_meal_total()

# Part 2

def calculate_alarm_time():
    # Get the current time and the number of hours to wait
    current_time = int(input("Enter the current time (in hours, 0-23): "))
    hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

    # Calculate the alarm time
    alarm_time = (current_time + hours_to_wait) % 24

    # Display the result
    print(f"The alarm will go off at {alarm_time:02d}:00")

# Call the function to execute the program
calculate_alarm_time()
