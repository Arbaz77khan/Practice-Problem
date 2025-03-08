class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end_of_word = True

    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.end_of_word
    
    def search_prefix(self, prefix):
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True
    
    def longest_prefix(self):
        curr = self.root
        prefix = ''
        while len(curr.children) == 1 and not curr.end_of_word:
            ch = next(iter(curr.children.keys()))  # Get the only child's key
            prefix += ch
            curr = curr.children[ch]
        
        return prefix
    
class Solution:
    def __init__(self):
        self.trie = Trie()

    def longestCommonPrefix(self, strs):
        for i in strs:
            self.trie.insert(i)
        return self.trie.longest_prefix()
    

obj = Solution()

result = obj.longestCommonPrefix(["dog","racecar","car"])

print(result)


        