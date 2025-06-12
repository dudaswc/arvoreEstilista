# Define a estrutura de um nó da árvore binária
class Node:
    def __init__(self, content): 
        self.content = content      # Texto da decisão ou desfecho
        self.left = None            # Caminho à esquerda (decisão 1)
        self.right = None           # Caminho à direita (decisão 2)

    def __str__(self):
        return self.content         # Permite printar o conteúdo do nó


# Define a árvore binária e o processo de navegação interativa
class BinaryTree:
    def __init__(self):
        self.root = None            # Raiz da árvore

    def getRoot(self):
        return self.root

    def interactivePath(self, node):
        """Navega pela árvore com base nas escolhas do usuário."""
        if node is None:
            return

        print("\n" + node.content)  # Mostra a situação ou decisão atual

        # Se o nó não tem filhos, chegamos a um final
        if node.left is None and node.right is None:
            print("🌟 Fim da jornada.")
            return

        # Solicita escolha do usuário
        choice = input("Digite 'esquerda' ou 'direita': ").strip().lower()

        if choice == 'esquerda':
            self.interactivePath(node.left)
        elif choice == 'direita':
            self.interactivePath(node.right)
        else:
            print("Opção inválida. Tente novamente.")
            self.interactivePath(node)  # Repete o nó atual


# Criação da árvore de decisões

tree = BinaryTree()

# NÓS FINAIS – desfechos da jornada
fim1 = Node("Você se adaptou ao mercado, mas abriu mão de vários valores. Ainda assim, é uma referência em técnica.")
fim2 = Node("Você fundou uma marca sustentável com mulheres periféricas e impactou vidas com inclusão!")
fim3 = Node("Você se esgotou tentando lutar sozinha contra o sistema. Decidiu mudar de área.")
fim4 = Node("Você liderou uma rede de estilistas feministas e hoje é reconhecida internacionalmente.")

# NÓS INTERMEDIÁRIOS – decisões importantes ao longo do caminho
n3 = Node("Você recebeu proposta de uma marca grande, mas sabe que eles são problemáticos com pautas de gênero.")
n3.left = fim1    # Aceita a proposta
n3.right = fim2   # Recusa e cria um projeto próprio

n4 = Node("Você denunciou a desigualdade salarial na empresa, mas enfrentou retaliação.")
n4.left = fim3    # Não teve apoio e acabou se afastando
n4.right = fim4   # Outras mulheres se uniram a você e criaram um coletivo

# NÓ INICIAL – ponto de partida da história
n1 = Node("Você terminou a faculdade de moda. Quer abrir sua marca ou ganhar experiência no mercado?")
n1.left = n3      # Escolhe abrir sua marca
n1.right = n4     # Decide trabalhar para ganhar experiência

# Define a raiz da árvore
tree.root = n1

# Inicia o jogo interativo
print("🎨 Caminhos da Estilista 🎨")
tree.interactivePath(tree.getRoot())
