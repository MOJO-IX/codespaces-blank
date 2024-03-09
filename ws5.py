student_height = input("enter the list of student heights ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)

total_height = 0
for height in student_height:
    total_height += height
print((total_height))

number_students = 0
for _ in student_height:
    number_students += 1
print(number_students)



average_height =(round( total_height / number_students))
print(average_height)

#                                or or
# number_student = len(student_height)
# average_height = round(total_height / number_student)
# print(average_height)

