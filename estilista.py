class Node:
    def __init__(self, content): 
        self.content = content
        self.left = None
        self.right = None

    def __str__(self):
        return self.content

class BinaryTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def interactivePath(self, node):
        if node is None:
            return
        print("\n" + node.content)
        if node.left is None and node.right is None:
            print("🌟 Fim da jornada.")
            return
        choice = input("Digite 'esquerda' ou 'direita': ").strip().lower()
        if choice == 'esquerda':
            self.interactivePath(node.left)
        elif choice == 'direita':
            self.interactivePath(node.right)
        else:
            print("Opção inválida. Tente novamente.")
            self.interactivePath(node)

