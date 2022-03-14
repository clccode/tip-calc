print('Tip Calculator')
print('\n')

# Get user input on the amount of the check and the percentage of tip
tab = float(input('Amount of your check: '))
tip_percent = int(input('Tip percentage: '))

# Calculate the tip
tip_per = tip_percent/100
tip = round(tab * tip_per, 2)
total = round(tab + tip, 2)

# Print the tip
print(f'The tip is: {tip}')
print(f'The total plus tip is: {total}')