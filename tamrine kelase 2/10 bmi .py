weight = 80
height = 1.8
bmi = weight / (height * height)
print(bmi)
if bmi <= 18:
    print("you need more food")
elif bmi > 18 and bmi <= 25:
    print("you are good")
else:
    print("overload")
