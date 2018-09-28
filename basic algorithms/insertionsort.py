def insertionsort(input):

    for i in range(1, len(input)):

        key = input[i]
        j = i-1

        while(j >= 0 and key < input[j]):
            input[j+1] = input[j]
            j = j-1

        input[j+1] = key


A = [4, 3, 2, 10, 12, 1, 5, 6]

print "Input is"
for i in range(len(A)):
    print A[i]

insertionsort(A)

print "Sorted output is"
for i in range(len(A)):
    print A[i]