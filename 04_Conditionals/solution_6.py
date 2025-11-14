distance = 100

if distance < 3:
    transportation = "Walk"

elif distance <= 15:
    transportation = "Bike"

else:
    transportation = "car"

print("Recommended to choose the Transport: ", transportation)