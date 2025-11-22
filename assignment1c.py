starting_salary = float(input("Enter the starting salary: "))

semi_annual_raise = 0.07
annual_return = 0.04
total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment

low = 0
high = 10000
steps = 0

def calculate_savings(portion_saved):
    current_savings = 0.0
    annual_salary = starting_salary
    
    for month in range(36):
        current_savings += current_savings * (annual_return / 12)
        current_savings += (annual_salary / 12) * portion_saved
        
        if (month + 1) % 6 == 0:
            annual_salary *= (1 + semi_annual_raise)
    
    return current_savings

max_savings = calculate_savings(1.0)
if max_savings < (down_payment - 100):
    print("It is not possible to save for the down payment in 36 months.")
else:
    while True:
        steps += 1
        guess = (low + high) // 2
        portion_saved = guess / 10000.0
        
        current_savings = calculate_savings(portion_saved)
        
        if abs(current_savings - down_payment) <= 100:
            break
        
        if current_savings < down_payment:
            low = guess
        else:
            high = guess
    
    print("Best savings rate:", portion_saved)
    print("Steps in bisection search:", steps)