#A program to demonstrate the Ackermann function. It contains some extra functionality to try to 
#more clearly illustrate the relationship between the different iterations.
import time

#Print spacers for each line.
def printSpacers(numSpacers):

    spacingChars = ["|"," ","#"]

    numChars = len(spacingChars)

    for i in range(0,numSpacers):
        print(spacingChars[i % numChars],end="")

def ackermannFunction(m, n, iterNum):

    printSpacers(iterNum)
    print("Running A(%s,%s)" % (m,n))

    if m == 0:

        nextAVal = int(n + 1)
        newIterCount = iterNum

    elif m > 0 and n == 0:

        nextAVal, newIterCount = ackermannFunction(m-1,1,iterNum+1)

    elif m > 0 and n > 0:

        nVal, newIterCount = ackermannFunction(m, n-1, iterNum+1)

        printSpacers(iterNum)
        print("New n value = %s" % nVal)

        nextAVal, newIterCount = ackermannFunction(m-1, nVal, iterNum+1)

    printSpacers(iterNum)
    print("A(%s,%s) = %s" % (m,n, nextAVal))

    return int(nextAVal), int(newIterCount)

if __name__=='__main__':

    #Input arguments
    print("Ackermann Function Calculator. Calculates A(m,n).")

    mStart = int(input("m="))
    nStart = int(input("n="))

    startTime = time.time()

    iteration=0
    result, iteration = ackermannFunction(mStart,nStart,iteration)

    endTime = time.time()

    print("Time = %s seconds" % (endTime - startTime))