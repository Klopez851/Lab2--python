# Author: Keidy Lopez
# Inputs: total meal charge
# Outputs: meal cost, tax,suggested top, and total bill

mealTotal = float(input("What is your total meal charge? "))
mealCost = mealTotal
tax = ((mealCost) * 0.09)
tip = ((mealTotal) * 0.18)
totalBill = (mealTotal + tax + tip)

print("Meal Cost: ", mealTotal)
print("tax: ", tax)
print("Suggested Tip: ", tip)
print("Totall Bill: ", totalBill)
