# BMI Calculator with Python
# What is Body Mass Index (BMI)?
# BMI is a measure of relative weight based on an individual’s mass and height. Today, Body Mass Index is commonly used 
# to classify people as underweight, overweight, and even with obesity. Also, 
# it is adopted by countries to promote healthy eating.
# The body mass index is calculated by dividing an individual’s weight in kilograms by their height in meters, 
# then dividing the answer again by their height. Now let’s see how to create a BMI calculator with Python:

Height = float(input("Enter your height in centimeters : "))
Weight = float(input("Enter your weight in kg : "))
Height = Height/100
BMI = Weight/(Height*Height)
print('Your Body Mass Index is :', BMI)
if (BMI > 0):
    if (BMI <=16):
        print('you are severely underweight')
    elif (BMI <= 18.5):
        print('you are underweight')
    elif (BMI <=25):
        print('you are healthy')
    elif (BMI <=30):
        print('you are overweight')
    else:
        print('you are severely overweight')
else:('enter valid details')

