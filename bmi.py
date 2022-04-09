weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meter:"))
bmi = weight / (height ** 2)


def body():
    if bmi < 25:
        print("Your weight is good")
    else:
        print("your body weight is overloaded")
body()