def quicksort(input, left, right):

    if(left < right):
        partitionindex = partition(input, left, right)
        quicksort(input, left, partitionindex-1)
        quicksort(input, partitionindex+1, right)

def partition(input, p, q):

    i = p

    for j in range(p+1, q+1):
        if(input[i] > input[j]):
            i = i+1
            input[i], input[j] = input[j], input[i]

    input[p], input[i] = input[i], input[p]

    return i

A = [6, 10, 13, 5, 8, 3, 2]

print "Input is : "
for x in range(len(A)):
    print A[x],

quicksort(A, 0, len(A)-1)

print "\nSorted output is : "
for x in range(len(A)):
    print A[x],