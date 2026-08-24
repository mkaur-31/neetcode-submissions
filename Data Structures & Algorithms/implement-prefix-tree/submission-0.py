class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()    
        

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            i = (ord(ch)-ord('a')) 
            if cur.children[i] == None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.isEnd = True


    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            i = (ord(ch)-ord('a')) 
            if cur.children[i] is None:
                return False
            cur = cur.children[i]
        return cur.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            i = (ord(ch)-ord('a')) 
            if cur.children[i] is None:
                return False
            cur = cur.children[i]
        return True
        
        