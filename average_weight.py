student_weights = input("Input a list of students weight: ").split()
for n in range(0, len(student_weights)):
    student_weights[n] = int(student_weights[n])

total_weight = 0
for weight in student_weights:
    total_weight += weight
print(f"total weight = {total_weight}")

number_of_students = 0
for student in student_weights:
    number_of_students += 1
print(f"number of students = {number_of_students}")

average_weight = round(total_weight / number_of_students)
print(average_weight)
