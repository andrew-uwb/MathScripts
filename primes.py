primeCount = 0
maxValue = int(input("Print primes up to value: "))
dispInput = input("Display all factors and results? (Y/N): ")

if dispInput == "Y" or dispInput == "y":
    fullDisplay = True
else:
    fullDisplay = False
    

for i in range(2,maxValue):

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
print(f"Prime Density: {(primeCount/maxValue):.3f}")