
class Methods:
        #1 - Heap Sort
        #make a heap out of a binary tree represented as an array.
        def heapify(self,arr, n, i):
            # Initialize largest as root
            largest = i
            l = 2 * i + 1  # left = 2*i + 1
            r = 2 * i + 2  # right = 2*i + 2

            # see if left child of root exists and is greater than root
            if l < n and arr[i] < arr[l]:
                largest = l

            # see if right child of root exists and is greater than root
            if r < n and arr[largest] < arr[r]:
                largest = r
            # Change root, if needed
            if largest != i:
                (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
                  # Heapify the root.
                self.heapify(arr, n, largest)

        def heapSort(self,arr):
            n = len(arr)
            # create a max heap.
            # last parent will be at ((n//2)-1) we can start at that location.

            for i in range(n // 2 - 1, -1, -1):
                self.heapify(arr, n, i)

            # one by one extract elements
            for i in range(n - 1, 0, -1):
                (arr[i], arr[0]) = (arr[0], arr[i])  # swap
                self.heapify(arr, i, 0)

        #2 - Quick Sort
        #method to find the partition position
        def partition(self,array, low, high):
            # choose the most right element as pivot
            pivot = array[high]
            # pointer for greater element
            i = low - 1
            # iterate through all elements and compare each element with pivot
            for j in range(low, high):
                if array[j] <= pivot:
                    # if element smaller than pivot is found, swap it with the greater element pointed by i
                    i = i + 1
                    # swapping element at i with element at j
                    (array[i], array[j]) = (array[j], array[i])

            # swap the pivot element with the greater element specified by i
            (array[i + 1], array[high]) = (array[high], array[i + 1])
            # return the position from where partition is done
            return i + 1

        # function to perform quicksort
        def quickSort(self, array, low, high):
            if low < high:
                # Find pivot element such that
                # element smaller than pivot are on the left
                # element greater than pivot are on the right
                pi = self.partition(array, low, high)

                # Recursive call on the left of pivot
                self.quickSort(array, low, pi - 1)

                # Recursive call on the right of pivot
                self.quickSort(array, pi + 1, high)

        # 3 - Merge Sort
        def merge(self, arr, l, m, r):
            n1 = m - l + 1
            n2 = r - m
            # create temp arrays
            L = [0] * (n1)
            R = [0] * (n2)
            # copy data to temp arrays L[] and R[]
            for i in range(0, n1):
                L[i] = arr[l + i]

            for j in range(0, n2):
                R[j] = arr[m + 1 + j]
            # merge the temp arrays back into arr[l..r]
            i = 0  # Initial index of first subarr
            j = 0  # Initial index of second subarr
            k = l  # Initial index of merged subarr

            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # copy the remaining elements of L[], if there are any
            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1

            # copy the remaining elements of R[], if there are any
            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1

        # l is for left index and r is right index of the sub-array of arr to be sorted
        def mergeSort(self, arr, l, r):
            if l < r:
                m = l + (r - l) // 2
                # sort first and second halves
                self.mergeSort(arr, l, m)
                self.mergeSort(arr, m + 1, r)
                self.merge(arr, l, m, r)

        # 4 - Selection Sort
        def selectionSort(self, array):
            # taverse through all array elements
            for i in range(len(array)):

                # find the minimum element in remaining unsorted array
                min_idx = i
                for j in range(i + 1, len(array)):
                    if array[min_idx] > array[j]:
                        min_idx = j

                # swap the found minimum element with the first element
                array[i], array[min_idx] = array[min_idx], array[i]