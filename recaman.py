validChoice = False
validModes = ["1","2"]
hardStop = 100000
valStop = 0
mode = 0
maxPosition = 0
sumPositions = 0

elements = []

count = 0
position = 0

while validChoice == False:

    print("Select Option:")
    print("1: Print out first n elements of Recamán Sequence")
    print("2: Print out Recamán Sequence until n is reached")

    mode = input(" >> ")

    if mode in validModes:

        validChoice = True
        print("Input value for n:")
        n = input(" >> ")
        if mode == "1":
            hardStop = int(n)
        elif mode == "2":
            valStop = int(n)

    else:

        print("Invalid Choice, please re-enter:")

while (count < hardStop):

    print(position)
    count += 1
    elements.append(position)

    sumPositions += position
    if position > maxPosition:

        maxPosition = position
    
    if position < count or (position - count) in elements:

        position = position + count

    else:

        position = position - count

    if (mode == "2" and position == valStop):

        break

print(f"Final count is {count}")
print(f"Highest number reached is {maxPosition}")
print(f"Mean of all numbers used is {(sumPositions/count):.3f}")