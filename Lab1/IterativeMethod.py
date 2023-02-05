import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["Nth nr", "Time(s)","Fib nr"]

def Fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    print("Iterative method")
    nr = [501, 631, 794, 1000,1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
    times = []
    for i in range(len(nr)):
        start = time.perf_counter()
        result = Fibonacci(int(nr[i]))
        end = time.perf_counter()
        x.add_row([nr[i], end-start, result])
        times.append(end - start)

    print(x)
    plt.plot(nr, times)
    plt.xlabel('nth fibonacci number')
    plt.ylabel('time(s)')
    plt.title('Iterative method graph')
    plt.show()
