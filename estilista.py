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

# Criando a árvore de decisões da estilista
tree = BinaryTree()

# Níveis mais profundos (finais)
fim1 = Node("Você se adaptou ao mercado, mas abriu mão de vários valores. Ainda assim, é uma referência em técnica.")
fim2 = Node("Você fundou uma marca sustentável com mulheres periféricas e impactou vidas com inclusão!")
fim3 = Node("Você se esgotou tentando lutar sozinha contra o sistema. Decidiu mudar de área.")
fim4 = Node("Você liderou uma rede de estilistas feministas e hoje é reconhecida internacionalmente.")

# Nível intermediário
n3 = Node("Você recebeu proposta de uma marca grande, mas sabe que eles são problemáticos com pautas de gênero.")
n3.left = fim1  # aceita
n3.right = fim2  # recusa e segue com projeto próprio

n4 = Node("Você denunciou a desigualdade salarial na empresa, mas enfrentou retaliação.")
n4.left = fim3  # não teve apoio
n4.right = fim4  # outras mulheres se juntaram e vocês criaram um coletivo

# Nível inicial
n1 = Node("Você terminou a faculdade de moda. Quer abrir sua marca ou ganhar experiência no mercado?")
n1.left = n3  # abrir
n1.right = n4  # ganhar experiência

# Definindo raiz
tree.root = n1

# Iniciar o caminho interativo
print("🎨 Caminhos da Estilista 🎨")
tree.interactivePath(tree.getRoot())

