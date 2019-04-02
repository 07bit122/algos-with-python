class Solution(object):
    def countAndSay(self, n):
        if n == 0:
            return '0'
        elif n == 1:
            return '1'

        final_number = '1'
        counter = 2
        while(counter <= n):
            num_dict = {}
            for x in range(len(final_number)):
                num_at_index = final_number[x]
                val_in_dict = num_dict.get(num_at_index, 0)
                num_dict.update({num_at_index: val_in_dict + 1})
            y = num_dict.keys()
            y.sort()
            final_number = ''
            for z in y:
                final_number += str(num_dict[z]) + z
            counter = counter + 1
        return final_number



solution = Solution()
print(solution.countAndSay(4))