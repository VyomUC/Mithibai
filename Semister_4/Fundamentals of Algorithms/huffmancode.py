class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

def sortByFrequency(item):
    return item[1]

def huffmanTree(node, binary=''):
    if isinstance(node.value, str):
        return {node.value: binary}
    d = {}
    if node.left: d.update(huffmanTree(node.left, binary + '0'))
    if node.right: d.update(huffmanTree(node.right, binary + '1'))
    return d

def huffmanEncode(string):
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1

    frequency = sorted(frequency.items(), key=sortByFrequency)
    nodes = [Node(value=char, left=None, right=None) for char, _ in frequency]

    while len(nodes) > 1:
        left = nodes.pop(0)
        right = nodes.pop(0)
        node = Node(value=None, left=left, right=right)
        nodes.append(node)
        nodes.sort(key=lambda x: sortByFrequency((x, sum([frequency[i][1] for i in range(len(frequency)) if frequency[i][0] == x.value]))))

    huffmanCode = huffmanTree(nodes[0])
    print('Char\tCode')
    for char, _ in frequency:
        print(f'{char}\t{huffmanCode[char]}')

huffmanEncode("hello")