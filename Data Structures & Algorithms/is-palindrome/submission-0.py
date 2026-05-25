class Solution:
    def isPalindrome(self, s: str) -> bool:
        x , y = 0, len(s)-1
        while x <= y:
            if not (s[x].isalnum()) and not( s[y].isalnum()):
                x += 1
                y -= 1
                continue
            elif not s[x].isalnum():
                x += 1
                continue
            elif not s[y].isalnum():
                y-=1
                continue
            if s[x].lower() != s[y].lower():
                return False
            x+=1
            y-=1
        return True

            
                
               


        