"""
Implement the RandomizedSet class:
    RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
"""
import random

class RandomizedSet:

    def __init__(self):
        # create and maintain both a dictionary and a list for most efficient operations
        self.data_list = [] # list
        self.data_map = {} # dictionary aka map

    def insert(self, val: int) -> bool:
        # checking for the value in a dictionary is on average O(1)
        # more efficient than checking the list which is on average O(n)
        if val in self.data_map:
            return False

        # add the element to the dictionary
        # len(list) is equal to the index of the last item + 1
        self.data_map[val] = len(self.data_list)

        self.data_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        # if the item is not in the data_map return False
        if not val in self.data_map:
            return False
        
        # instead of actually removing the item from memory (less efficient),
        # move the last element in the list into the location of
        # the element to be removed
        last_element = self.data_list[-1]
        remove_index = self.data_map[val]

        self.data_map[last_element] = remove_index
        self.data_list[remove_index] = last_element

        # change last element in the list to be the value
        # of the element we want to remove
        self.data_list[-1] = val

        # remove last element from list
        self.data_list.pop()

        # remove element from dictionary
        self.data_map.pop(val)
        return True

    def getRandom(self) -> int:
        # random.choice will randomly select an element from the list
        return random.choice(self.data_list)