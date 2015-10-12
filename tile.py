#Program to calculate area in a space and cost to retile it.

width = float(input('How wide is you floor?: '))
height = float(input('How height is you floor?: '))
area = width * height
print('Your area is ',  area)
cost = float(input('How much does your tile cost per square foot?: '))

price = area * cost
print('It will cost you $' , price, ' to redo your floor.')
