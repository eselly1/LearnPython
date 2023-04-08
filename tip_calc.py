print('Welcome to the tip calculator.')

total = float(input('What was the total bill?\n'))
ppl = float(input('How many people?\n'))
x = float(input('What percentage of tip would you like to pay? 10, 12, 15, or 20?\n'))
tip = (x/100)+1

print(f"Each person should pay: ${round((total/ppl)* tip, 2)}")

