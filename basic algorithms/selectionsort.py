def selectionsort(input):
    for i in range(len(input)):
        min_index = i

        for j in range(i+1, len(input)):
            if(input[min_index] > input[j]):
                min_index = j

        A[i], A[min_index] = A[min_index], A[i]

A = [64, 25, 12, 22, 11]

print "Input is"
for i in range(len(A)):
    print A[i]

selectionsort(A)

print "Sorted output is"
for i in range(len(A)):
    print A[i]