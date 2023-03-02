print("\n")
print("I'm your out-of-date BMI Calculator in th year 2023. Who uses these ... do you? Anyways")
print("\n")
height = input("Enter your height in meters (If you don't know then Google it): ")
print("\n")
weight = input("Enter your weight in kilos (If you don't know then Google it): ")
print("\n")

height_as_float = float(height)
weight_as_int = int(weight)

bmi = weight_as_int / height_as_float ** 2

bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
bmi_as_str = str(bmi_as_int)

print("Your BMI is: " + bmi_as_str)

print("\n")
