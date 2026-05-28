class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []

       

        for br in s:
            if br in mapping.keys():
                stack.append(br)
            else:
                if not stack:
                    return False
                x = stack.pop()
                if br != mapping[x]:
                    return False
        if not stack:
            return True
        else:
            return False
 

        