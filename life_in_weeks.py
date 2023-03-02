age = input("Yo! How old are you? ")

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left unitl you are 90 years old ... make it count!")