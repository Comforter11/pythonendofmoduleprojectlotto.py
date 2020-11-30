# COMFORTER MAKWEYA CLASS-2
# Lottery Numbers

import random

# Empty list
LottoNum = []

for i in range(0, 6):
    number = random.randint(1, 49)
    # Number picked or not...
    while number in LottoNum:
        # ...if picked, pick a new one.
        number = random.randint(1, 49)

    # Append unique number to the list
    LottoNum.append(number)

# Sort the list in ascending order
LottoNum.sort()

userNumbers = []
for i in range(0, 6):
    number = int(input("Please enter a number between 1 and 49: "))
    while number in userNumbers or number < 1 or number > 49:
        print("Invalid number, please try again.")
        number = int(input("Please enter a number between 1 and 49: "))

    userNumbers.append(number)


print(">>> Today's lottery numbers are: ")
print(LottoNum)

print(">>>Your selection:")
print(userNumbers)

counter = 0
for number in userNumbers:
    if number in LottoNum:
        counter += 1

    def total_winnings():
        if counter == 0:
            message = "Won R0"
            return message
        elif counter == 1:
            message = "Won R0"
            return message
        elif counter == 2:
            message = "Won R20.00"
            return message
        elif counter == 3:
            message = "Won R100.00"
            return message
        elif counter == 4:
            message = "Won R2, 384.00"
            return message
        elif counter == 5:
            message = "Won R8, 544.00"
            return message
        elif counter == 6:
            message = "Won R10, 000 000.00"
            return message
print("You got " + str(counter) + " number(s) correctly.")
print(total_winnings())


# Empty list
LottoNum = []

for i in range(0, 6):
    number = random.randint(1, 49)
    # Number picked or not...
    while number in LottoNum:
        # ...if picked, pick a new one.
        number = random.randint(1, 49)

    # Append unique number to the list
    LottoNum.append(number)

# Sort the list in ascending order
LottoNum.sort()

userNumbers = []
for i in range(0, 6):
    number = int(input("Please enter a number between 1 and 49: "))
    while number in userNumbers or number < 1 or number > 49:
        print("Invalid number, please try again.")
        number = int(input("Please enter a number between 1 and 49: "))

    userNumbers.append(number)

print(">>> Today's lottery numbers are: ")
print(LottoNum)

print(">>>Your selection:")
print(userNumbers)

counter = 0
for number in userNumbers:
    if number in LottoNum:
        counter += 1

print("You got " + str(counter) + " number(s) correctly.")
