class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        root = TrieNode()
        
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.isWord = True
        
        def findRoot(word):
            node = root
            prefix = ""
            for ch in word:
                if ch not in node.children:
                    break
                node = node.children[ch]
                prefix += ch
                if node.isWord:
                    return prefix
            return word
        
        return " ".join(findRoot(w) for w in sentence.split())
