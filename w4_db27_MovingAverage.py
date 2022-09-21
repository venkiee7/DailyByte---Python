# This question is asked by Microsoft. Design a class, MovingAverage, which contains a method, next that is responsible for returning the moving average from a stream of integers.
# Note: a moving average is the average of a subset of data at a given point in time.

class movingAverage:
    def __init__(self, size):
        self.nums = []
        self.capacity = size
    
    def next(self, val):
        self.nums.insert(0, val)
        print(self.nums)
        if len(self.nums)>self.capacity:
            self.nums.pop()
        return int(sum(self.nums) / len(self.nums))

ma = movingAverage(3)  #init
print(ma.next(3))
print(ma.next(5))
print(ma.next(7))
print(ma.next(6))   