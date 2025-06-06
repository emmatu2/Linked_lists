import numpy as np
from Interfaces import List
 
class ArrayList(List):
    '''
        ArrayList: Implementation of a List interface using Arrays. 
    '''
 
    def __init__(self):
        '''
        __init__: Initialize the state (array, n and j). 
        '''
        self.n = 0
        self.j = 0
        self.a = self.new_array(1)
 
    def new_array(self, n: int) -> np.array:
        '''
        new_array: Create a new array of size n
        Input:
            n: the size of the new array
        Return:
            An array of size n
        '''
        return np.zeros(n, object)
 
    def resize(self):
        '''
        resize: Create a new array and copy the old values. 
        '''
        b = self.new_array(max(1, 2 * self.n))
        for k in range(0, self.n):
            b[k] = self.a[(self.j + k) % len(self.a)]
        self.a = b
        self.j = 0
 
    def get(self, i: int) -> object:
        '''
        get: returns the element at position i
        Inputs:
            i: Index that is integer non negative and at most n
        '''
        if i < 0 or i >= self.n:
            raise IndexError()
        return self.a[(i + self.j) % len(self.a)]
 
    def set(self, i: int, x: object) -> object:
        '''
        set: Set the value x at the index i.
        Inputs:
            i: Index that is integer non negative and at most n
            x: Object type, i.e., any object 
        '''
        if i < 0 or i >= self.n:
            raise IndexError()
        y = self.a[(i + self.j) % len(self.a)]
        self.a[(i + self.j) % len(self.a)] = x
        return y
 
    def append(self, x: object):
        self.add(self.n, x)
 
    def add(self, i: int, x: object): # If inserting into the first-half "shift" every element from j to j + i one bin to the left
                                      # If inserting into the second-half "shift" every element from j + n - 1 to j + i one bin to the right
        '''
            add: shift one position all the items j>=i, insert an element 
            at position i of the list and increment the number of elements 
            in the list
            Inputs:
                i: Index that is integer non negative and at most n
                x: Object type, i.e., any object
        '''
        if i < 0 or i > self.n: # Precondiiton
            raise IndexError()
        if len(self.a) == self.n: # Invariant - amortized runtime
            self.resize()
        if i < self.n / 2: # Shift elements to the left, inserting into the first-half
            self.j = (self.j - 1) % len(self.a)
            for k in range(0, i):
                self.a[(k + self.j) % len(self.a)] = self.a[(k + self.j + 1) % len(self.a)]
        else:
            for k in range(self.n, i, -1): # Shift elements to the right, inserting into the second-half
                self.a[(k + self.j) % len(self.a)] = self.a[(k + self.j - 1) % len(self.a)]
        self.a[(i + self.j) % len(self.a)] = x
        self.n += 1
 
    def remove(self, i: int) -> object:
        if i < 0 or i >= self.n: # Precondition
            raise IndexError()
        x = self.a[(i + self.j) % len(self.a)] # Temporary variable to store the value to be removed
        if i < self.n / 2: # Shift elements to the right, removing from the first-half
            for k in range(i, 0, -1):
                self.a[(k + self.j) % len(self.a)] = self.a[(k + self.j - 1) % len(self.a)]
            self.j = (self.j + 1) % len(self.a)
        else: # Shift elements to the left, removing from the second-half
            for k in range(i, self.n - 1): 
                self.a[(k + self.j) % len(self.a)] = self.a[(k + self.j + 1) % len(self.a)]
        self.n -= 1
        if len(self.a) >= 3 * self.n: # Invariant
            self.resize()
        return x
 
    def size(self) -> int:
        return self.n
 
    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n - 1:
                s += ","
        return s + "]"
 
    def __iter__(self):
        self.iterator = 0
        return self
 
    def __next__(self):
        if self.iterator < self.n:
            x = self.a[(self.iterator + self.j) % len(self.a)]
            self.iterator += 1
        else:
            raise StopIteration()
        return x
