









import numpy as np

income = float(input("Enter your income: "))

bracket1 = np.where(income <= 10000, 0, 0)
bracket2 = np.where((income > 10000) & (income <= 20000), (income - 10000) * 0.1, 0)
bracket3 = np.where(income > 20000, 10000 * 0.1 + (income - 20000) * 0.2, 0)

tax = bracket1 + bracket2 + bracket3

print(f"Tax: ${tax:.2f}")





 





