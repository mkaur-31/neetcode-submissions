from collections import defaultdict
import string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            #sorted_word = ''.join(sorted(word))
            sorted_word = tuple([word.count(c) for c in string.ascii_lowercase])
            res[sorted_word].append(word)
        return list(res.values())