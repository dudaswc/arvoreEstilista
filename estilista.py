class Node:
    def __init__(self, content): 
        self.content = content
        self.left = None
        self.right = None

    def __str__(self):
        return self.content
