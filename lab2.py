print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    BMI = weight/ (height*height)
    print("Your BMI is " + str(BMI))
    if (BMI <18.5):
        print("You're under weight")
    elif (BMI >25.0):
        print("You're over weight")
    else:
        print("You're normal weight")



calculate_bmi(weight=57, height=1.73)

# TypeError: can only concatenate str (not "float") to str

