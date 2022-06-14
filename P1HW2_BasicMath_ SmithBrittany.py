# A brief description of the project
# 6/9/2022
# CTI-110 P1HW2 - Basic Math
# Brittany Smith
#
expense = input("Enter name expense:")
charge = float(input("Enter monthly charge:"))
tax = charge*.06
monthly_charge = charge + tax
annual_charge = monthly_charge *12

print("Monthly tax",tax)
print(monthly_charge)
print(annual_charge)
