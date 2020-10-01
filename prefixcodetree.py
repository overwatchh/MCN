 
from Node import Node

class PrefixCodeTree:
    root = None

    def __init__(self):
        self.root = Node('')

    def insert(self, codeword, symbol):
        node = self.root
        for code in codeword:
            if (code == 0):
                if (node.left is None):
                    node.left = Node('')
                    node = node.left
                else:
                    node = node.left
            else:
                if (node.right is None):
                    node.right = Node('')
                    node = node.right
                else:
                    node = node.right
        node.data = symbol

    def decode(self, code, dataLen):
        data = ''
        decodedString = ''
        node = self.root
        for byte in code:
            data += f'{byte:0>8b}'
        print(data)
        for i in range(dataLen):
            if (data[i] == '0'):
                node = node.left
            else:
                node = node.right
            if (node.isLeave()):
                decodedString += node.data
                node = self.root
        return decodedString


codeTree = PrefixCodeTree()

codebook = {
    'x1': [0],
    'x2': [1,0,0],
    'x3': [1,0,1],
    'x4': [1,1]
}

for symbol in codebook:
    codeTree.insert(codebook[symbol], symbol)

print(codeTree.decode(b'\xd2\x9f\x20', 21))