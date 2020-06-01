class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not value:
            print('Value cannot be empty')
            return
        print('Inserting value {0}'.format(value))
        if self.root is None:
            self.root = Node(value)
        else:
            prevNode = None
            currentNode = self.root
            while(currentNode):
                if value < currentNode.value:
                    prevNode = currentNode
                    currentNode = currentNode.left
                else:
                    prevNode = currentNode
                    currentNode = currentNode.right
            node = Node(value)
            if value >= prevNode.value:
                prevNode.right = node
            else:
                prevNode.left = node
            

    def search(self, value):
        print('Searching for {0}'.format(value))
        currentNode = self.root
        while(currentNode):
            if value == currentNode.value:
                print('Value found')
                return
            elif value < currentNode.value:
                currentNode = currentNode.left
            else: 
                currentNode = currentNode.right
             


def main():
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(10)
    tree.insert(20)
    tree.insert(1)
    tree.insert(6)
    tree.insert(15)
    tree.insert(170)
    tree.search(20)


if __name__ == '__main__':
    main()
