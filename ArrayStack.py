import numpy as np
from Interfaces import Stack
from Interfaces import List
 
 
class ArrayStack(Stack, List):
    '''
        ArrayStack: Implementation of the Stack interface based on Arrays. 
        All the @abstractemthods should be implemented. 
        An instance of ArrayStack has access to all the methods in ArrayStack and 
        all the methods of the base class (Stack). When executing a method, it executes
        the method of ArrayStack, if it does not exists, it executes the method in the
        Base class (Stack).
        For exmaple, 
        s = ArrayStack()
        print(s)
        print(len(s))
    '''
    def __init__(self):
        self.a = self.new_array(1)
        self.n = 0
 
    def new_array(self, n: int) ->np.array:
        return np.zeros(n, object)
    
    def resize(self):
        '''
            Resize the array
        '''
        self.b = self.new_array(max(1,2*self.n))
        #i = 0
        for i in range(self.n):
            self.b[i] = self.a[i]
            
        self.a = self.b 
        return self.a
        #for i in range(len(self.a)):
        #    self.append("")
 
        #pass 
 
    def get(self, i : int) -> object:
        #edited
        if 0<= i < self.n:
            return self.a[i]
        #pass 
    
    def set(self, i : int, x : object) -> object:
        #edited 
        if 0<= i < self.n:
            y = self.a[i]
            self.a[i] = x
            return y
        #pass 
    
    def add(self, i: int, x : object) :
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''
        #edited
        #self.insert(i,x)
        if 0 > i or i > self.n  :
            raise IndexError("Out of Range")
        if len(self.a) == self.n :
           self.resize()
        
        for k in range(self.n -i):
            self.a[k] = self.a[k-1]
        self.a[i] = x
        self.n += 1
        
        #pass 
 
    def remove(self, i : int) -> object :
        '''
            remove element i and shift all j > i one 
            position to the left
        '''
        if i < 0 or i >= self.n:
            raise IndexError("Out of Range")
        for k in range(self.n- i -1):
            self.a[k] = self.a[k+1]
        self.n -= 1
        #if (len(self.a) > 3*self.n):
        #    self.resize()
        return self.a[i]
        #pass 
 
    def push(self, x : object) :
        self.add(self.n, x)
    
    def pop(self) -> object :
        return self.remove(self.n-1)
 
    def size(self) :
        '''
            size: Returns the size of the stack
            Return: an integer greater or equal to zero representing the number
                    of elements in the stack
        '''
        return self.n
        
    def __str__(self) -> str:
        '''
            __str__: Returns the content of the string using print(s)
            where s is an instance of the ArrayStack
            Return: String with the content of the stack
        '''
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[i]
            if i  < self.n-1:
                s += ","
        return s + "]"
 
    def __iter__(self):
        '''
            Initialize the iterator. It is to be use in for loop
        '''
        self.iterator = 0
        return self
 
    def __next__(self):
        '''
            Move to the next item. It is to be use in for loop
        '''
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator +=1
        else:
             raise StopIteration()
        return x
