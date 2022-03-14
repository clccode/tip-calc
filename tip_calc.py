print('Tip Calculator')
print('\n')
tab = float(input('Amount of your check: '))
tip_percent = int(input('Tip percentage: '))
tip_per = tip_percent/100
tip = round(tab * tip_per, 2)
total = round(tab + tip, 2)
print(f'The tip is: {tip}')
print(f'The total plus tip is: {total}')