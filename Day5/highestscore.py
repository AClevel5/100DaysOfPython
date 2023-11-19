# for loop to find highest score.
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
high_score = 0

for student in student_scores:
    if student > high_score:
        high_score = student

print(f"The highest score in the class is: {high_score}")
