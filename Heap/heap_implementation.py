class Heap:
    def __init__(self,arr):
        self.arr = arr
    def heapify_down(self,ind):
        n = len(self.arr)
        largest_index = ind
        left_child_ind = (2 * ind) + 1
        right_child_ind = (2 * ind) + 2

        if left_child_ind < n and self.arr[largest_index] < self.arr[left_child_ind]:
            largest_index = left_child_ind
        if right_child_ind < n and self.arr[largest_index] < self.arr[right_child_ind]:
            largest_index = right_child_ind
        if largest_index != ind:
            self.arr[largest_index],self.arr[ind] = self.arr[ind],self.arr[largest_index]
            self.heapify_down(largest_index)
    def heapify_up(self,ind):
        parent_ind = (ind-1)//2
        if ind > 0 and self.arr[ind] > self.arr[parent_ind]:
            self.arr[ind],self.arr[parent_ind] = self.arr[parent_ind],self.arr[ind]
            self.heapify_up(parent_ind)
    def heapify(self,index,val):
        old = self.arr[index]
        self.arr[index] = val
        if val < old:
            self.heapify_down(index)
        else:
            self.heapify_up(index)
        return self.arr
    def insert(self,value):
        self.arr.append(value)
        last = len(self.arr) - 1
        self.heapify_up(last)
        return self.arr
    def extract_max(self):
        if not self.arr:
            return None
        last = len(self.arr) - 1
        self.arr[0],self.arr[last] = self.arr[last],self.arr[0]
        self.arr.pop()
        self.heapify_down(0)
        return self.arr
nums = [10,7,6,4,5,4,5,3,2]
h1 = Heap(nums)
print(h1.heapify(0,1))
print(h1.insert(11))
print(h1.extract_max())