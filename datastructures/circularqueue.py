from typing import Any

from datastructures.array import Array
from datastructures.iqueue import IQueue, T

from copy import deepcopy

class CircularQueue(IQueue[T]):
    """ Represents a fixed-size circular queue. The queue
        is circular in the sense that the front and rear pointers wrap around the
        array when they reach the end. The queue is full when the rear pointer is
        one position behind the front pointer. The queue is empty when the front
        and rear pointers are equal. This implementation uses a fixed-size array.
    """

    def __init__(self, maxsize: int = 0, data_type=object) -> None:
        ''' Initializes the CircularQueue object with a maxsize and data_type.
        
            Arguments:
                maxsize: The maximum size of the queue
                data_type: The type of the elements in the queue
        '''
        self.__max_size = maxsize
        self.__dt = data_type
        self.__arr = Array(starting_sequence= [data_type() for i in range(maxsize + 1)], data_type=data_type)
        self.__front = 0
        self.__rear = 0

    def enqueue(self, item: T) -> None:
        ''' Adds an item to the rear of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.front
                1
                >>> q.rear
                3
                >>> q.enqueue(4)
                >>> q.enqueue(5)
                >>> q.full
                True
                >>> q.enqueue(6)
                IndexError('Queue is full')
            
            Arguments:
                item: The item to add to the queue
                
            Raises:
                IndexError: If the queue is full
        '''
        if self.full:
            raise IndexError("Queue is full, cannot enqueue")
        if not isinstance(item, self.__dt):
            raise TypeError("Item type does not match Queue data type")
        self.__arr[self.__rear] = item
        self.__rear = (self.__rear + 1) % (self.__max_size + 1)

    def dequeue(self) -> T:
        ''' Removes and returns the item at the front of the queue

            Examples:
                >>> q = CircularQueue(maxsize=5, data_type=int)
                >>> q.enqueue(1)
                >>> q.enqueue(2)
                >>> q.enqueue(3)
                >>> q.dequeue()
                1
                >>> q.dequeue()
                2
                >>> q.dequeue()
                3
                >>> q.dequeue()
                IndexError('Queue is empty')
                >>> q.dequeue()
                IndexError('Queue is empty')

            Returns:
                The item at the front of the queue

            Raises:
                IndexError: If the queue is empty
        '''
        front_item = self.__arr[self.__front]
        self.__front = (self.__front + 1) % (self.__max_size + 1)
        return front_item

    def clear(self) -> None:
        ''' Removes all items from the queue '''
        self.__front = 0
        self.__rear = 0
        self.__arr[0] = self.__dt()

    @property
    def front(self) -> T:
        ''' Returns the item at the front of the queue without removing it

            Returns:
                The item at the front of the queue

            Raises:
                IndexError: If the queue is empty
        '''
        if self.empty:
            raise IndexError("Queue is Empty")
        return self.__arr[self.__front]
            

    @property
    def full(self) -> bool:
        ''' Returns True if the queue is full, False otherwise 
        
            Returns:
                True if the queue is full, False otherwise
        '''
        if (self.__rear + 1) % (self.__max_size + 1) == self.__front:
            return True
        return False

    @property
    def empty(self) -> bool:
        ''' Returns True if the queue is empty, False otherwise
        
            Returns:
                True if the queue is empty, False otherwise
        '''
        if self.__front == self.__rear:
            return True
        return False
    
    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the queue
        
            Returns:
                The maximum size of the queue
        '''
        return self.__max_size

    def __eq__(self, other: object) -> bool:
        ''' Returns True if this CircularQueue is equal to another object, False otherwise
        
            Equality is defined as:
                - The front and rear pointers are equal
                - The elements between the front and rear pointers are equal, even if they are in different positions
                
            Arguments:
                other: The object to compare this CircularQueue to
                
            Returns:
                True if this CircularQueue is equal to another object, False otherwise
        '''
        if not isinstance(other, CircularQueue):
            return False
        if len(self) != len(other):
            return False

        self_copy = deepcopy(self)
        other_copy = deepcopy(other)

        self_items = []
        other_items = []
        for i in range(len(self)):
            self_items.append(self_copy.dequeue())
            other_items.append(other_copy.dequeue())
        for item in other_items:
            if item not in self_items:
                return False
        return True
          
    
    def __len__(self) -> int:
        ''' Returns the number of items in the queue
        
            Returns:
                The number of items in the queue
        '''
        return (self.__rear - self.__front + self.__max_size + 1) % (self.__max_size + 1)

    def __str__(self) -> str:
        ''' Returns a string representation of the CircularQueue
        
            Returns:
                A string representation of the queue
        '''
        stringlist = []
        i = self.__front
        for j in range(len(self)):
            stringlist.append(self.__arr[i])
            i = (i + 1) % (self.__max_size + 1)
        return str(stringlist)

    def __repr__(self) -> str:
        ''' Returns a developer string representation of the CircularQueue object
        
            Returns:
                A string representation of the CircularQueue object
        '''
        return f"CircularQueue({self.__max_size}): items: {str(self)}"
                                  
