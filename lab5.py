# CS3
# Angel Rodriguez II
# Lab 5
# Diego Aguirre
# 11-19-2019
# Purpose: The purpose of this lab is to implement a LRUCache data structure that supports a few methods
#           and to be able to find the K most freqent words from a given list>

import heapq

class ListNode(object): # this is a standard node class for a doubly linked list
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LinkedList(object): # Linked list class
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        node.next, node.prev = None, None
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
            node.next, node.prev = None, None

class LRUCache(object):
    def __init__(self, capacity):
        self.list = LinkedList()
        self.dict = {}
        self.capacity = capacity

    def _insert(self, key, val):
        node = ListNode(key, val)
        self.list.insert(node)
        self.dict[key] = node

    def get(self, key):
        if key in self.dict:
            val = self.dict[key].val
            self.list.delete(self.dict[key])
            self._insert(key, val)
            return val
        return -1

    def put(self, key, val):
        if key in self.dict:
            self.list.delete(self.dict[key])
        elif len(self.dict) == self.capacity:
            del self.dict[self.list.head.key]
            self.list.delete(self.list.head)
        self._insert(key, val)

    def max_cap(self):
        print(len(self.dict))

    def size(self):
        len(self.dictt


list_with_duplicates = ["dog", "cat", "rat", "cat", "dog", "dog", "dog", "cat", "elephant", "elephant", "giraffe"]
count = {}

dict = {}

for item in list_with_duplicates:
   if item in dict: # You can assume this operation takes O(1)
       dict[item] = dict[item] + 1
   else:
       dict[item] = 1

wordFreqDict = {}

for each in dict:
    # print(each + ": " + str(dict[each]))
    wordFreqDict.update({each:dict[each]})

def with_heapq(the_dict):
    items = [(-value, key) for key, value in the_dict.items()]
    smallest = heapq.nsmallest(3, items)
    print([-value for value, key in smallest])

with_heapq(wordFreqDict)



