import time
import matplotlib.pyplot as plt
import gmpy2
from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Nth nr", "Time(s)","Fib nr"]


def Fibonacci(n):
    sqrt_5 = gmpy2.sqrt(5)
    phi = (1 + sqrt_5) / 2
    result = (phi**n - (1-phi)**n) / sqrt_5
    return result


if __name__ == '__main__':
    print("Binet's Formula method")
    nr = [501, 631, 794, 1000,1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
    times = []
    for i in range(len(nr)):
        start = time.perf_counter()
        result = Fibonacci(int(nr[i]))
        end = time.perf_counter()
        x.add_row([nr[i], end-start, result])
        times.append(end-start)

    print(x)
    plt.plot(nr, times)
    plt.xlabel('nth fibonacci number')
    plt.ylabel('time(s)')
    plt.title("Binet's formula Method")
    plt.show()
