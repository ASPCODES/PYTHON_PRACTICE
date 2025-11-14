score = 50

if score >= 101:
    print("Kindly check and verify your grades again")
    exit()

if score >= 90:
    grade = "A"

elif score >= 80:
    grade = "B"

elif score >= 70:
    grade = "C"

elif score >= 60:
    grade = "D"

else:
    grade = "F"

print("Score ", grade)