def binarysearch(input, left, right, element):

    if (right >= left):
        mid = left + (right - left) / 2

        if (input[mid] == element):
            return mid

        elif (input[mid] < element):
            return binarysearch(input, mid+1, right, element)

        else:
            return binarysearch(input, left, mid-1, element)

    else:
        return -1


input = [1,2,3,4,5,6,7,8,9,10]

output = binarysearch(input, 0, len(input), 8);

if (output != -1):
    print "Binary search found element at index ", output
else:
    print "Binary search did not find the element in the input"