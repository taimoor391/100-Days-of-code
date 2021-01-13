print("welcome to the tip calculator")

bill= float(input("what was the totla bill? \n$"))
tip= float(input("what percentage tip would you like to give? 10,12 or 12?\n"))
splitby= float(input("How many people should split the bill\n"))
total= ((bill*(tip/100))+bill)
share= round(total/splitby,2)
print('Each person should pay: ${}'.format(share))