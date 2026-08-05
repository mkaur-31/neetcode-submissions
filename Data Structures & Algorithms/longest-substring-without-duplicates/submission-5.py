class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        l=0 
        i,j=0,0
        seen = set()
        
        while j< len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i+=1
            seen.add(s[j])
            l =max(l,j-i+1)
            j+=1
                    
        
        return l
                    
            

        