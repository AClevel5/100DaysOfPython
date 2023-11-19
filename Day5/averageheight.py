student_heights = [180, 124, 165, 173, 189, 169, 146]
total_height = 0

for student_height in student_heights:
    total_height = total_height + student_height

average_height = round(total_height / len(student_heights))
total_students = len(student_heights)

print("total height = " + total_height)
print("number of students = " + total_students)
print("average height = " + average_height)
