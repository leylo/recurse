
def convert(height, weight):
    height = height / 39.37008
    print(' ', height)
    weight = weight * .45 
    print(' ', weight)
    bmi(height, weight)

def bmi(height, weight):
    bmi = (weight)/(height*height)
    print("Your BMI is %.2f." % bmi)

print("What is your height?: ")
height = float(input())
print("What is your weight?: ")
weight = float(input())
print ("Are you using metric or imperial units?")
unit = input()

if unit == 'metric':
  bmi(height, weight)
else:
  convert(height, weight)
