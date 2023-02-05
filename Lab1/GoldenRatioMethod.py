import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["Nth nr", "Time(s)","Fib nr"]

# the value of golden ratio
PHI = 1.6180339

# Fibonacci numbers up to n = 5
f = [0, 1, 1, 2, 3, 5]

def fib(n):
    # Fibonacci numbers for n < 6
    if n < 6:
        return f[n]

    #start counting from 5th term
    t = 5
    fn = 5

    while t < n:
        fn = round(fn * PHI)
        t += 1

    return fn


if __name__ == '__main__':
    print("Golden Ratio method")
    nr = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
    times = []
    for i in range(len(nr)):
        start = time.perf_counter()
        result = fib(int(nr[i]))
        end = time.perf_counter()
        x.add_row([nr[i], end-start, result])
        times.append(end - start)

    print(x)
    plt.plot(nr, times)
    plt.xlabel('nth fibonacci number')
    plt.ylabel('time(s)')
    plt.title('Golden Ratio Method Graph')
    plt.show()
