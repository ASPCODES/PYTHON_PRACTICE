# Take 5 names as input from user and store in a list.
# Then print them in reverse order.

Names = []

for i in range(5):
    name = input("Enter name" + str(i + 1) + ": ")
    Names.append(name)

    # # print names in simple order
    # print("Names in simple order")
    # for name in Names:
    #     print(name)

    # Print names in reverse order

    print("Names in reversed order:")

    for name in reversed(Names):
        print(name)