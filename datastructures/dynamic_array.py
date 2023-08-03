"""
Dynamic array - It is an array that grow or shrinks dynamically 
depending on the size of the array.

Continues memory
"""

class DynamicArray:

    array = None
    count = 0
    size = 0

    def __init__(self) -> None:
        self.array = [0] * (1)
        self.head = id(self.array)
        self.count = 0 #maintains the length of the array
        self.size = 1 # maintains the memory allocated

    def add(self, element) -> None:
        """Add element to the DA
        """
        # check no of elements is equal to size of the array
        if (self.count == self.size):
            self.growSize()
        
        # insert element at end of array
        self.array[self.count] = element
        self.count += 1

    def growSize(self) ->None:
        """
        Grow the size of the array - O(N)
        """
        temp = None
        if (self.count == self.size):
            temp = [0] * (self.size * 2)
            i = 0
            while (i < self.size):
 
                # copy all array value into temp
                temp[i] = self.array[i]
                i += 1
        
        self.array = temp
        self.size = self.size * 2
    
    def shrinkSize(self) -> None:
        temp = None
        if (self.count > 0):
            temp = [0] * (self.count)
            i=0
            while(i< self.count):
                temp[i] = self.array[i]
                i+=1
            
            self.size = self.count
            self.array = temp
    
    def insert(self, index, element):

        if (self.count == self.size):
            self.growSize()
        
        i = self.count - 1
        while(i >= index):
            self.array[i+1] = self.array[i]
            i -= 1

        self.array[index] = element
        self.count += 1

    def remove(self):
        if (self.count > 0):
            self.array[self.count - 1] = 0
            self.count -= 1

    def removeAt(self, index):
        if (self.count >0):
            i = index
            while(i < self.count - 1):
                self.array[i] = self.array[i+1]
                i+=1
            self.array[self.count - 1] = 0
            self.count -= 1

    @staticmethod
    def main(args):
        da = DynamicArray()
 
        # add 9 elements in array
        da.add(1)
        da.add(2)
        da.add(3)
        da.add(4)
        da.add(5)
        da.add(6)
        da.add(7)
        da.add(8)
        da.add(9)

        # print all array elements after add 9 elements
        print("Elements of array:")
        i = 0
        while (i < da.size):
            print(str(da.array[i]) + " ", end="")
            i += 1
        print()
 
        # print size of array and no of element
        print("Size of array: " + str(da.size))
        print("No of elements in array: " + str(da.count))
 
        # shrinkSize of array
        da.shrinkSize()
 
        # print all array elements
        print("Elements of array after shrinkSize of array:")
        i = 0
        while (i < da.size):
            print(str(da.array[i]) + " ", end="")
            i += 1
        print()
 
        # print size of array and no of element
        print("Size of array: " + str(da.size))
        print("No of elements in array: " + str(da.count))
 
        # add an element at index 1
        da.insert(1, 22)
 
        # print Elements of array after adding an
        # element at index 1
        print("Elements of array after add an element at index 1:")
        i = 0
        while (i < da.size):
            print(str(da.array[i]) + " ", end="")
            i += 1
        print()
 
        # print size of array and no of element
        print("Size of array: " + str(da.size))
        print("No of elements in array: " + str(da.count))
 
        # delete last element
        da.remove()
 
        # print Elements of array after delete last
        # element
        print("Elements of array after delete last element:")
        i = 0
        while (i < da.size):
            print(str(da.array[i]) + " ", end="")
            i += 1
        print()
 
        # print size of array and no of element
        print("Size of array: " + str(da.size))
        print("No of elements in array: " + str(da.count))
 
        # delete element at index 1
        da.removeAt(1)
 
        # print Elements of array after delete
        # an element index 1
        print("Elements of array after delete element at index 1:")
        i = 0
        while (i < da.size):
            print(str(da.array[i]) + " ", end="")
            i += 1
        print()
 
        # print size of array and no of element
        print("Size of array: " + str(da.size))
        print("No of elements in array: " + str(da.count))
    
   
if __name__ == "__main__":
    DynamicArray.main([])