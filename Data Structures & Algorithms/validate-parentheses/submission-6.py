class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []

        for br in s:
            if br in mapping:
                if stack:
                    if stack.pop() != mapping[br]:
                        return False
                else:
                    return False
            else:
                stack.append(br)

        if not stack:
            return True
        else:
            return False
 

        