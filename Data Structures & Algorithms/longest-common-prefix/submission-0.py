class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for st in strs:
            for i in range(len(prefix)):
                if i >= len(st) or st[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
        return prefix
            
         