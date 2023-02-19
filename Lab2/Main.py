import time
import random
import sys
import matplotlib.pyplot as plt
from SortingMethods import Methods
from prettytable import PrettyTable
# set the maximum recursion depth to 1 million
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    method = Methods()
    #define the array of sizes of the array which will be tested
    nr = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000,3000,4000,5000,6000,7000,8000]
    #nr=[10,20,30,40,50,60,70,80,90,100]

    x1 = PrettyTable(field_names=["Length of Array", "Time(s)"], title="Heap Sort Results")
    x2 = PrettyTable(field_names=["Length of Array", "Time(s)"], title="Quick Sort Results")
    x3 = PrettyTable(field_names=["Length of Array", "Time(s)"], title="Merge Sort Results")
    x4 = PrettyTable(field_names=["Length of Array", "Time(s)"], title="Selection Sort Results")

    times1, times2, times3, times4 = [], [], [], []

    for k in range(len(nr)):
        n = nr[k]
        # define the array with random values from 0 to 1000
        arr = [random.randint(0,1000) for i in range(n)]

        # create copies of the original array
        arr1, arr2, arr3, arr4 = arr.copy(), arr.copy(), arr.copy(), arr.copy()

        print(f"\n---> Initial array: with -{n}- elements")
        for i in range(n):
            print("%d" % arr[i], end=" ")

        # heap sort
        start1 = time.perf_counter()
        method.heapSort(arr1)
        end1 = time.perf_counter()
        total1 = end1 - start1
        x1.add_row([nr[k], total1])
        times1.append(total1)
        print("\n\n==========Heap sort==========")
        print("Sorted array: ")
        for i in range(n):
            print("%d" % arr1[i], end=" ")
        print(f"\nTotal time of sorting : {total1:.6f} sec")

        # quick sort
        start2 = time.perf_counter()
        method.quickSort(arr2, 0, n - 1)
        end2 = time.perf_counter()
        total2 = end2 - start2
        x2.add_row([nr[k], total2])
        times2.append(total2)
        print("\n\n==========Quick sort==========")
        print("Sorted array: ")
        for i in range(n):
            print("%d" % arr2[i], end=" ")
        print(f"\nTotal time of sorting : {total2:.6f} sec")

        # merge sort
        start3 = time.perf_counter()
        method.mergeSort(arr, 0, n - 1)
        end3 = time.perf_counter()
        total3 = end3 - start3
        x3.add_row([nr[k], total3])
        times3.append(total3)
        print("\n\n==========Merge sort==========")
        print("Sorted array: ")
        for i in range(n):
            print("%d" % arr3[i], end=" ")
        print(f"\nTotal time of sorting : {total3:.6f} sec")

        # selection sort
        start4 = time.perf_counter()
        method.selectionSort(arr4)
        end4 = time.perf_counter()
        total4 = end4 - start4
        x4.add_row([nr[k], total4])
        times4.append(total4)
        print("\n\n==========Selection sort==========")
        print("Sorted array: ")
        for i in range(n):
            print("%d" % arr4[i], end=" ")
        print("\nTotal time of sorting : ", total4, " sec")


    # print the table with results for each method
    print("\n", x1)
    print("\n", x2)
    print("\n", x3)
    print("\n", x4)
    # single graph for each method
    plt.plot(nr, times1)
    plt.xlabel("Nr of array's elements")
    plt.ylabel('time(s)')
    plt.title(f'Heap Sort Graph')
    plt.show()

    plt.plot(nr, times2)
    plt.xlabel("Nr of array's elements")
    plt.ylabel('time(s)')
    plt.title(f'Quick Sort Graph')
    plt.show()

    plt.plot(nr, times3)
    plt.xlabel("Nr of array's elements")
    plt.ylabel('time(s)')
    plt.title(f'Merge Sort Graph')
    plt.show()

    plt.plot(nr, times4)
    plt.xlabel("Nr of array's elements")
    plt.ylabel('time(s)')
    plt.title(f'Selection Sort Graph')
    plt.show()
    #print the graph of all methods
    plt.plot(nr, times1)
    plt.plot(nr, times2)
    plt.plot(nr, times3)
    plt.plot(nr, times4)
    plt.xlabel("Nr of array's elements")
    plt.ylabel('time(s)')
    plt.legend(['Heap Sort', 'Quick Sort','Merge Sort', 'Selection Sort'])
    plt.title(f'Sorting algorithms Graphs')
    plt.show()
