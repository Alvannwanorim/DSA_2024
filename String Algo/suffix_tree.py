class SuffixTreeNode:
    def __init__(self, start, end) -> None:
        self.children = {}
        self.start = start
        self.end= end
        self.suffix_link = None 

class SuffixTree:
    def __init__(self,text) -> None:
        self.text = text
        self.root = SuffixTreeNode(-1, -1)
        self.build_suffix_tree()

    def build_suffix_tree(self):
        n = len(self.text)
        for i in range(n):
            current_suffix = self.text[i:]
            self.insert_suffix(current_suffix, i)
    
    def insert_suffix(self, suffix, suffix_start):
        current_node = self.root
        i = 0
        while i < len(suffix):
            # print(i)
            char = suffix[i]
            # print(char)
            if char in current_node.children:
                child = current_node.children[char]
                j = child.start
                print(j)
                while j <= child.end and i < len(suffix) and self.text[j] == suffix[i]:
                    i += 1
                    j += 1
                    if j > child.end:
                        current_node = child
                    else:
                        split_node = SuffixTreeNode(child.start, j - 1)
                        current_node.children[char] = split_node
                        split_node.children[self.text[j]] = child
                        child.start = j 
                        split_node.children[suffix[i]] = SuffixTreeNode(suffix_start + 1, len(self.text) -1)
                        return
            else:
                current_node.children[char] = SuffixTreeNode(suffix_start + 1, len(self.text) - 1)
                return 
    def print_tree(self, node=None, indent=""):
        if node is None:
            node = self.root
        
        for key, child in node.children.items():
            label = self.text[child.start:child.end +1]
            print(indent + f"{key}: {label}")
            self.print_tree(child, indent + "   ")


text = "banana$"
tree =SuffixTree(text)
tree.print_tree()