annual_salary=float(input('Enter your annual salary='))
portion_saved=float(input('Enter the percent of your salary to save, as a decimal='))
total_cost=float(input('Enter the cost of your dream home='))

portion_down_payment=0.25*total_cost
r=0.04
current_savings=0
month=0

while current_savings<(portion_down_payment):
    current_savings = current_savings + current_savings * r / 12 + portion_saved * (annual_salary / 12)
    month+=1
print(month)