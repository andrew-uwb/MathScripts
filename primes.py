primeCount = 0
maxValue = int(input("Print primes up to value: "))
fullDisplay = input("Display all factors and results? (Y/N): ")

for i in range(2,maxValue):

    prime = True

    if fullDisplay == "Y" or fullDisplay == "y":
        factorList = [1]
        testVal = i

    else:
        testVal = int(i**0.5) + 1

    for j in range(2,testVal):
        
        if i % j == 0:

            prime = False
            if fullDisplay == "N":
                break
            else:
                factorList.append(j)

    if prime:
        print(i,end="")
        primeCount += 1
        if fullDisplay == "Y":
            print(": ***PRIME***")
        else:
            print("")
    
    if prime == False and fullDisplay == "Y":
        factorList.append(i)
        print(f"{i}: ",end="")
        print(*factorList, sep = ",")

print(f"Primes Found: {primeCount}")
print(f"Prime Density: {(primeCount/maxValue):.3f}")

            
