from heapq import heapify, heappop, heappush

class MedianHeap():
    def __init__(self, arr=[]):
        sorted_arr = sorted(arr);
        self.median = sorted_arr[len(arr) / 2]
        lower = sorted_arr[:len(arr) / 2]
        grater = sorted_arr[len(arr) / 2 + 1:]

        self.lower_max_heap = map(lambda x: -x, lower)
        heapify(self.lower_max_heap)
        self.grater_min_heap = grater
        heapify(self.grater_min_heap)


    def pop(self):
        median = self.median
        self.median = self._get_sapply_heap_pop()
        return median

    def push(self, x):
        if x < self.median:
            if x < self.lower_max_heap[0]:
                self._push_lower(x)
            else:
                if self._count_lower() < self._count_grater():
                    self._push_lower(x)
                else:
                    self._push_grater(self.median)
                    self.median = x
        else:
            if x > self.grater_min_heap[0]:
                heappush(self.grater_min_heap, x)
            else:
                if self._count_lower() < self._count_grater():
                    self._push_lower(self.median)
                    self.median = x
                else:
                    self._push_grater(x)

    def _push_lower(self, x):
        heappush(self.lower_max_heap, self.median)

    def _push_grater(self, x):
        heappush(self.grater_min_heap, self.median)

    def _count_lower(self):
        return len(self.lower_max_heap)

    def _count_grater(self):
        return len(self.grater_min_heap)

    def _get_sapply_heap_pop(self):
        if self._count_lower() == 0 and self._count_grater() == 0:
            return None
        if self._count_lower() < self._count_grater():
            return heappop(self.grater_min_heap)
        else:
            return -heappop(self.lower_max_heap)

if __name__ == '__main__':
    median_heap = MedianHeap([10, 5, 1, 3, 6])
    print [median_heap.pop() for i in range(5)]

