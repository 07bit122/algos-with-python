def mergesort(input, left, right):
    if(right > left):
        middle = (right + left) / 2

        mergesort(input, left, middle)
        mergesort(input, middle+1, right)

        completemerge(input, left, middle, right)

def completemerge(input, left, middle, right):
    B = []
    C = []
    D = []

    # store left subarray elements
    for x in range(left, middle+1):
        B.append(input[x])

    # store right subarray elements
    for x in range(middle+1, right+1):
        C.append(input[x])

    b = len(B)
    c = len(C)
    i = 0
    j = 0

    # compare elements in left sub array with those in right
    # to form the sorted array of the bounds given by the left and
    # right of this merge call
    while i < b and j < c:
        if (B[i] > C[j]):
            D.append(C[j])
            j = j + 1
        else:
            D.append(B[i])
            i = i + 1

    while i < b:
        D.append(B[i])
        i = i + 1

    while j < c:
        D.append(C[j])
        j = j + 1

    # update the input array with the sorted order.
    input[left:right+1] = D

A = [4, 3, 2, 10, 12, 1, 5, 6]

print "Input is : "
for x in range(len(A)):
    print A[x],

mergesort(A, 0, len(A)-1)

print "\nSorted output is : "
for x in range(len(A)):
    print A[x],
