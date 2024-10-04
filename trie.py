from function import remove_accents

class Node:
    def __init__(self):
        self.children = [None] * 256
        self.is_terminal = False
        self.value = ''

class Trie:
    def __init__(self):
        self.root = Node()

    # Hàm void insert vào trie
    def insert(self, word):
        node = self.root
        for char in remove_accents(word):
            c = ord(char)
            if node.children[c] == None:
                node.children[c] = Node()
            node = node.children[c]
        node.is_terminal = True
        node.value = word

    # Hàm search trả về True nếu có, false nếu không
    def search(self, word):
        node = self.root
        for char in remove_accents(word):
            c = ord(char)
            if node.children[c] == None:
                return False
            node = node.children[c]
        return True

    # Hàm get trả về giá trị của từ
    def get(self, word):
        node = self.root
        for char in remove_accents(word):
            c = ord(char)
            if node.children[c] == None:
                return ''
            node = node.children[c]
        return node.value

    # Hàm delete trả về True nếu xóa thành công, false nếu không thành công
    def delete(self, word):
        node = self.root
        for char in remove_accents(word):
            c = ord(char)
            if node.children[c] == None:
                return False
            node = node.children[c]
        node.terminal = False
        node.value = ''
        return True
