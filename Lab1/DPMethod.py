#Dynamic Programming Method for nth fibonacci number
import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["Nth nr", "Time(s)","Fib nr"]


def Fibonacci(n):
    # array to store intermediate values of the Fibonacci sequence
    Arr = [0] * (n + 1)

    # base cases
    Arr[0] = 0
    Arr[1] = 1

    for i in range(2, n + 1):
        Arr[i] = Arr[i - 1] + Arr[i - 2]

    return Arr[n]


if __name__ == '__main__':
    print("Dynamic Programming Method")
    nr = [501, 631, 794, 1000,1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
    times = []
    for i in range(len(nr)):
        start = time.time()
        result = Fibonacci(int(nr[i]))
        end = time.time()
        x.add_row([nr[i], end-start, result])
        times.append(end - start)

    print(x)
    plt.plot(nr, times)
    plt.xlabel('nth fibonacci number')
    plt.ylabel('time(s)')
    plt.title('Dynamic Programming Method Graph')
    plt.show()
