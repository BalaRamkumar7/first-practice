annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi-annual salary raise, as a decimal: "))
current_savings = 0
portion_down_payment = 0.25
r = 0.04
monthly_salary = ((annual_salary/12))
m = 0

while current_savings < (portion_down_payment * total_cost):
    current_savings += ((monthly_salary * portion_saved) + (current_savings*r/12))
    m += 1
    if m % 6 == 0:
        annual_salary *= (1 + semi_annual_raise)
        monthly_salary = annual_salary / 12

print("Number of months:", m)
