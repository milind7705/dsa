# Create a data structure that can store a list of integers that can change in size over time
# and find the median from this dynamically growing list in constant time, O(1).
# Implement a class, MedianOfStream, which should support the following operations:
# Constructor(): This initializes the object of this class, which in turn creates the max and the min heap.
# Insert Num(num): This adds an integer, num, to the data structure.
# Find Median(): This finds the median of all elements seen so far.
# If there are an even number of elements, return the average of the two middle values.


from heapq import *

class MedianOfStream:

    def __init__(self):
        self.max_heap_for_smallnum = []
        self.min_heap_for_largenum = []

    def insert_num(self, num):
        if not self.max_heap_for_smallnum or -self.max_heap_for_smallnum[0] >= num:
            heappush(self.max_heap_for_smallnum, -num)
        else:
            heappush(self.min_heap_for_largenum, num)

        if len(self.max_heap_for_smallnum) > len(self.min_heap_for_largenum) + 1:
            heappush(self.min_heap_for_largenum, -heappop(self.max_heap_for_smallnum))
        elif len(self.max_heap_for_smallnum) < len(self.min_heap_for_largenum):
            heappush(self.max_heap_for_smallnum, -heappop(self.min_heap_for_largenum))

    def find_median(self):
        if len(self.max_heap_for_smallnum) == len(self.min_heap_for_largenum):

            # we have even number of elements, take the average of middle two elements
            # we divide both numbers by 2.0 to ensure we add two floating point numbers
            return -self.max_heap_for_smallnum[0] / 2.0 + self.min_heap_for_largenum[0] / 2.0

        # because max-heap will have one more element than the min-heap
        return -self.max_heap_for_smallnum[0] / 1.0


# Driver code
def main():
    median_num = MedianOfStream()
    nums = [35, 22, 30, 25, 1]
    numlist = []
    x = 1
    for i in nums:
        numlist.append(i)
        print(x, ".\tData stream: ", numlist, sep="")
        median_num.insert_num(i)
        print("\tThe median for the given numbers is: " +
              str(median_num.find_median()), sep="")
        print(100*"-"+"\n")
        x += 1


if __name__ == "__main__":
    main()
