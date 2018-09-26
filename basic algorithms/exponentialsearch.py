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

def exponentialsearch(input, length, element):
    i = 1

    while i <= length and input[i] < element:
        i = i*2

    return binarysearch(input, i/2, min(i, length), element)

input = [1,2,3,4,5,6,7,8,9,10]

output = exponentialsearch(input, len(input), 10)

if (output != -1):
    print "Exponential search found element at index ", output
else:
    print "Exponential search did not find the element in the input"