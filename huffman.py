import heapq
from collections import Counter, namedtuple

class HuffmanNode(namedtuple("HuffmanNode", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq
    
def huffman_tree(text):
    frequency = Counter(text)

    heap = [HuffmanNode(char, freq, None, None) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)
    
    return heap[0] if heap else None

def huffman_coding(node, prefix="", codebook=None):
    if codebook is None:
        codebook = {}

    if node:
        if node.char:
            codebook[node.char] = prefix

        huffman_coding(node.left, prefix + '0', codebook)
        huffman_coding(node.right, prefix + '1', codebook)

    return codebook

def huffman_encode(text):
    root = huffman_tree(text)
    if not root:
        return "", None

    code = huffman_coding(root)
    encoded_text = ''.join(code[char] for char in text)

    return encoded_text, root

def huffman_decode(encoded_text, root):
    if not root:
        return ""

    decoded_chars = []
    node = root

    for bit in encoded_text:
        node = node.left if bit == '0' else node.right

        if node.char:
            decoded_chars.append(node.char)
            node = root

    return ''.join(decoded_chars)
