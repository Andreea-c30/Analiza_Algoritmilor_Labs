import math
import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
x1 = PrettyTable(field_names=["N", "Time(s)"], title="Algorithm_1")
x2 = PrettyTable(field_names=["N", "Time(s)"], title="Algorithm_2")
x3 = PrettyTable(field_names=["N", "Time(s)"], title="Algorithm_3")
x4 = PrettyTable(field_names=["N", "Time(s)"], title="Algorithm_4")
x5 = PrettyTable(field_names=["N", "Time(s)"], title="Algorithm_5")

def algorithm_1():
        c = [True] * (n + 1)
        c[1] = False
        i = 2
        while i <= n:
            if c[i]:
                j = 2 * i
                while j <= n:
                    c[j] = False
                    j += i
            i += 1
        for i in range(2, n + 1):
            if c[i]:
                print(i, end=' ')

def algorithm_2():
    c = [True] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        j = 2 * i
        while j <= n:
            c[j] = False
            j += i
        i += 1
    for i in range(2, n+1):
        if c[i]:
            print(i, end=' ')

def algorithm_3():
    c = [True] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        if c[i] == True:
            j = i + 1
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j = j + 1
        i += 1
    for i in range(2, n+1):
        if c[i]:
            print(i, end=' ')


def algorithm_4():
    c = [True] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        j=2
        while j < i:
                if i % j == 0:
                    c[i] = False
                j += 1
        i += 1
    for i in range(2, n + 1):
        if c[i]:
            print(i, end=' ')

def algorithm_5():
    c = [True] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        j=2
        while j<=math.sqrt(i):
            if i % j == 0:
                c[i] = False
            j += 1
        i += 1
    for i in range(2, n+1):
        if c[i]:
            print(i, end=' ')

if __name__ == '__main__':
    times1, times2, times3, times4, times5 = [], [], [], [], []
    nr = [1000, 1700, 2000,3000,4000,5000,6000,7000,8000,9000,10000]
   # initialize all values in the c array to True
    for n in nr:

        print("\n1-")
        start1 = time.perf_counter()
        algorithm_1()
        end1 = time.perf_counter()
        total1 = end1 - start1
        x1.add_row([n, total1])
        times1.append(total1)
        print(f"\nTotal time of execution : {total1:.6f} sec")

        print("\n2-")
        start2 = time.perf_counter()
        algorithm_2()
        end2 = time.perf_counter()
        total2 = end2 - start2
        x2.add_row([n, total2])
        times2.append(total2)
        print(f"\nTotal time of execution : {total2:.6f} sec")

        print("\n3-")
        start3 = time.perf_counter()
        algorithm_3()
        end3 = time.perf_counter()
        total3 = end3 - start3
        x3.add_row([n, total3])
        times3.append(total3)
        print(f"\nTotal time of execution : {total3:.6f} sec")

        print("\n4-")
        start4 = time.perf_counter()
        algorithm_4()
        end4 = time.perf_counter()
        total4 = end4 - start4
        x4.add_row([n, total4])
        times4.append(total4)
        print(f"\nTotal time of execution : {total4:.6f} sec")
        print("\n5-")
        start5 = time.perf_counter()
        algorithm_5()
        end5 = time.perf_counter()
        total5 = end5 - start5
        x5.add_row([n, total5])
        times5.append(total5)
        print(f"\nTotal time of execution : {total5:.6f} sec")

    # print the table with results for each method
    print("\n", x1)
    print("\n", x2)
    print("\n", x3)
    print("\n", x4)
    print("\n", x5)
    #print the graph of all methods
    plt.plot(nr, times1)
    plt.plot(nr, times2)
    plt.plot(nr, times3)
    plt.plot(nr, times4)
    plt.plot(nr, times5)
    plt.xlabel("N")
    plt.ylabel('time(s)')
    plt.legend(['1', '2','3', '4','5' ])
    plt.title(f'Graph')
    plt.show()

