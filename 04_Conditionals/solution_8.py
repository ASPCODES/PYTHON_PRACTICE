password = "112223333"
password_length = len(password)

if len(password) < 6:
    strength = "Weak"

elif len(password) <= 10:
    strength = "Medium"

else:
    strength = "strong"

print("Your password is: ", strength)