savings = float(input("What are your current savings"))
interest_rate = float(input("What is the interest rate"))

new_amount = interest_rate/100 * savings
total = savings + new_amount
print("your new amount is £"+ str(round(total, 2)))
