class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
        
        node.is_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.dfs(self.root, 0, word)
    
    def dfs(self, node, i, word):
        if i == len(word):
            return node.is_end

        if word[i] != '.':
            if word[i] not in node.children:
                return False

            return self.dfs(node.children[word[i]], i + 1, word)
        else:
            for child in node.children.values():
                if self.dfs(child, i + 1, word):
                    return True

            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)