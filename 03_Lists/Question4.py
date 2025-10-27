# Write a program to count how many even and odd numbers are in a given list.

Numbers = [2, 4, 5 ,7, 14, 33, 12, 40]

even_count = 0
odd_count = 0

for num in Numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even Numbers: ", even_count)
print("Odd Numbers: ", odd_count)
