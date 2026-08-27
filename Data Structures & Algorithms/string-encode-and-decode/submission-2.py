class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) +'#'+ s
    
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            
            count = ''
            i = 0
            while s[i]!='#':
                count += s[i]
                i += 1
            
            count = int(count)


            j = i+1
            temp = ''
            for _ in range(count):
                temp += s[j]
                j += 1
            res.append(temp)
        
            s = s[j:]
            

        return res
