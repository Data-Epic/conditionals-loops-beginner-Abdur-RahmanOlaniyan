score = int(input("Enter your score (0 - 100): "))

if score >= 70 and score <= 100:
    grade = 'A'
elif score >= 60 and score <= 69:
    grade = 'B'
elif score >= 50 and score <= 59:
    grade = 'C'
elif score >= 40 and score <= 49:
    grade = 'D'
elif score >= 0 and score <= 39:
    grade = 'F'
else:
    grade = 'Invalid score'

print(grade)