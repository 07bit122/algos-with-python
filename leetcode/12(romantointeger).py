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

        total = 0
        for x in range(len(s)):
            # cannot look back on first index, so if condition
            if (x > 0):
                # combine the current letter with previous letter and check if that exists in our keys
                appended_string = s[x-1] + s[x]
                if (appended_string in values.keys()):
                    # subtract the value of previous letter and add the combo value to total
                    total = total - values[s[x-1]]
                    total = total + values[s[x-1]+s[x]]
                    continue
            # default total add for all cases
            total = total + values[s[x]]
    
        return total

solution = Solution()
print(solution.romanToInt('MCMXCIV'))
