class Solution(object):
    def makeLargestSpecial(self, s):
        
        substrings = []
        count = 0
        start = 0

        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                count -= 1

            if count == 0:
                inner = self.makeLargestSpecial(s[start + 1:i])
                special = '1' + inner + '0'
                substrings.append(special)
                start = i + 1

        substrings.sort(reverse=True)

        return ''.join(substrings)
        