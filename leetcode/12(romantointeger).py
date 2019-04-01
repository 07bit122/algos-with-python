class Solution(object):
    def romanToInt(self, s):
        # the keys are limited, so it makes sense to store them in a dictionary
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        # convert the input to a string
        listofs = list(s)
        total = 0
        for x in range(len(listofs)):
            # cannot look back on first index, so if condition
            if (x > 0):
                # combine the current letter with previous letter and check if that exists in our keys
                appended_string = listofs[x-1] + listofs[x]
                if (appended_string in values.keys()):
                    # subtract the value of previous letter and add the combo value to total
                    total = total - values[listofs[x-1]]
                    total = total + values[listofs[x-1]+listofs[x]]
                    continue
            # default total add for all cases
            total = total + values[listofs[x]]
    
        return total

solution = Solution()
print(solution.romanToInt('MCMXCIV'))
