print("Welcome to the dopest rollercoaster ride ever!")
height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
    print("Ok! You're cool to ride the dopest rollercoaster ride ever.")
    age = int(input("What is your age? "))
    if age <12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        print("You'll be alright. Have a free ride on us!")
    else:
        bill = 12
        print("Please pay $12.")
    
    wants_photo = input("Do you want a photo taken? Y or N. ").lower()
    if wants_photo == "y":
        bill += 3
    
    print(f"your bill is ${bill}")

else:
    print("Sorry, you have be a little bit taller, a little bit of a baller like the 1995 Skee-Lo rap song says ... know what I mean.")
