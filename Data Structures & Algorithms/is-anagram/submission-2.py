from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        characters = defaultdict(int)
        def add_to_dict(key) -> bool:
            characters[key] += 1
            return True
        
        def remove_char(key) -> bool:
            if key not in characters:
                return False
            
            characters[key] -= 1
            if characters[key] == 0:
                characters.pop(key)
            return True
        for char in s:
            add_to_dict(char)
        
        for char in t:
            if remove_char(char) == False:
                return False
        if len(characters) > 0:
            return False
        return True
