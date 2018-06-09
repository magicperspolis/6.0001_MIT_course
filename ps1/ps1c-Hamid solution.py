annual_salary_original=float(input('Enter your starting annual salary='))

total_price=1000000
portion_down_payment=0.25
annual_rate=0.04
current_savings=0
month=0
semi_annual_raise=0.07
max_portion_saved=1
min_portion_saved=0
step=0
found=False


while abs(max_portion_saved-min_portion_saved)>0.001:
    current_savings=0
    annual_salary=annual_salary_original
    step+=1
    #print(step)
    portion_saved = (max_portion_saved + min_portion_saved) / 2
    print('portion_saved', portion_saved)
    for month in range(0,36,1):
        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
        current_savings = current_savings + current_savings * annual_rate / 12 + portion_saved * (annual_salary / 12)
    three_years_savings=current_savings
    print('three_years_savings',three_years_savings)
    print('36 months_savings-portion_down_payment*total_price=', three_years_savings - portion_down_payment * total_price)
    if abs(three_years_savings - portion_down_payment * total_price) < 100:
        found = True
        break
        print('found=', found)
    if three_years_savings - portion_down_payment * total_price < 0:
        min_portion_saved = portion_saved
    if three_years_savings - portion_down_payment * total_price > 0:
        max_portion_saved = portion_saved
    print('max_portion_saved', max_portion_saved)
    print('min_portion_saved', min_portion_saved)
        #print(current_savings)
        #print(current_savings)
        # max_current_savings = current_savings + current_savings * annual_rate / 12 + max_portion_saved * (annual_salary / 12)
        # min_current_savings = current_savings + current_savings * annual_rate / 12 + min_portion_saved * (annual_salary / 12)
    #print('after 36 months=',current_savings)



if found:
    print('best savings rate=', portion_saved)
    print('Steps in bisection search=', step)
else:
    print('not possible in three years')
