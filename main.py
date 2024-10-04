from function import *
from trie import *

# In ra danh sách các đồ ăn

list_tinh = read_file('tinh.txt')
trie = Trie()
for tinh in list_tinh:
    trie.insert(tinh)

print(trie.search("Hồ Chí Minh"))  # True
print(trie.get("Hồ Chí Minh"))
print(trie.search("ca"))   # False