import io
from typing import List

class Trie:
    def __init__(self, character: str, end_of_word: bool):
        self.children = {}        
        self.character = character
        self.end_of_word = end_of_word

    def add_word(self, word: str):
        c = word[0]
        eow = False
        if len(word) == 1:
            eow = True
        
        if c not in self.children: 
            self.children[c] = Trie(c, eow)
            
        if len(word) > 1:
            self.children[c].add_word(word[1:])

class Dictionary:
    def __init__(self):
        self.root = Trie('*', False)
        self.words = 0

    def load_words_from_file(self, file_path: str) -> int:
        # Load the words from a file
        with(io.open(file_path)) as f:
            lines = [line.rstrip() for line in f]

        for word in lines:
            self.root.add_word(word)

        self.words = len(lines)

        return self.words

    def load_words(self, words: List) -> int:
        for word in words:
            self.root.add_word(word)

        self.words = len(words)

        return self.words


    def check_word(self, word: str) -> bool:
        node = self.root

        c, remaining = word[0], word[1:]

        while True:
            if c in node.children:
                if node.children[c].end_of_word and len(remaining) == 0:
                    return True
                else:
                    node = node.children[c]
                if len(remaining ) > 0:
                    c, remaining = remaining[0], remaining[1:]
                else:
                    break
            else:
                break

        return False


    def get_words(self, node=None, base_word='') -> List[str]:
        if node == None:
            node = self.root

        words = []

        for c in node.children.keys():
            if node.children[c].end_of_word:
                words.append(base_word + c)

            child_words = self.get_words(node.children[c], base_word + c)
            for word in child_words:
                words.append(word)

        return words

    def complete_word(self, word: str) -> List[str]:
        node = self.root

        c, remaining = word[0], word[1:]

        words = []

        while True:
            if c in node.children:
                node = node.children[c]
                if len(remaining) > 0:
                    c, remaining = remaining[0], remaining[1:]
                else:
                    break
            else:
                return []

        child_words = self.get_words(node, word)
        for word in child_words:
            words.append(word)

        return words