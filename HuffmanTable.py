from struct import unpack
import math


class Node:
    def __init__(self, symbol, code, left=None, right=None):
        self.symbol = symbol  # символ
        self.left = left  # левый ребенок
        self.right = right  # правый ребенок
        self.code = code


class HuffmanTable:
    def __init__(self):
        self.root = Node(None, None)
        self.elements = []

    def calc_tree(self, d):
        for el in d.keys():
            bits = el
            i = 0
            curr_node = self.root
            while len(bits) > 1:
                if bits[0] == '0':
                    if curr_node.left is None:
                        curr_node.left = Node(None, None)
                        curr_node.left.code = 0
                    curr_node = curr_node.left
                if bits[0] == '1':
                    if curr_node.right is None:
                        curr_node.right = Node(None, None)
                        curr_node.right.code = 1
                    curr_node = curr_node.right
                bits = bits[1:]
            if bits[0] == '0':
                curr_node.left = Node(d.get(el), 0)
            if bits[0] == '1':
                curr_node.right = Node(d.get(el), 1)

    def find(self, code):
        r = self.root
        deep = 0
        while len(code) > 0:
            if r.left == None and r.right == None:
                return r.symbol, deep
            if code[0] == '0':
                r = r.left
                deep += 1
            else:
                r = r.right
                deep += 1
            code = code[1:]
        return r.symbol, deep
