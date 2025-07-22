income = float(input("Enter your income: "))
if income <= 10000:
    tax = 0
elif income <= 20000:
    tax = (income - 10000) * 0.1
else:
    tax = 10000 * 0.1 + (income - 20000) * 0.2

print(f"Tax: ${tax:.2f}")

