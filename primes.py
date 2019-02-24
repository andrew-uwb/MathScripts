import sys

primeCount = 0
minValue = 2
maxValue = 2

minValueInput = input("Print primes starting at value: ")
if minValueInput != "":
    minValue = int(minValueInput)

maxValueInput = input("Going up to value: ")
if maxValueInput != "":
    maxValue = int(maxValueInput)
else:
    maxValue = minValue

if minValue > maxValue or minValue < 0 or maxValue < 2:
    print("Max value must be >= min value and >= 2.")
    print("Both numbers must be positive.")
    sys.exit()

dispInput = input("Display all factors and results? (Y/N): ")

if dispInput == "Y" or dispInput == "y":
    fullDisplay = True
else:
    fullDisplay = False
    
for i in range(max(2,minValue),maxValue + 1):

    prime = True

    if fullDisplay:
        factorList = [1]
        testVal = i

    else:
        testVal = int(i**0.5) + 1

    for j in range(2,testVal):
        
        if i % j == 0:

            prime = False
            if not fullDisplay:
                break
            else:
                factorList.append(j)

    if prime:
        print(i,end="")
        primeCount += 1
        if fullDisplay:
            print(": ***PRIME***")
        else:
            print("")
    
    if not prime and fullDisplay:
        factorList.append(i)
        print(f"{i}: ",end="")
        print(*factorList, sep = ",")

print(f"Primes Found: {primeCount}")
print(f"Regional Prime Density: {(primeCount/((maxValue - minValue) + 1)):.3f}")