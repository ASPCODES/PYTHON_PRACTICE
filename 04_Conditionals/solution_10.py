species = input("Enter your pet species ").lower()
age = float(input("Enter your pet's age "))

if species == "dog":
    if age < 2:
        print("Recommended puppy food")
    else:
        print("Recommended Dog food")

if species == "cat":
    if age > 5:
        print("Recommended senior Cat food")
    else:
        print("Recommended kitten food")

else:
    print("We only support dogs and cats")
