import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["Nth nr", "Fib nr", "Time(s)"]

def Fibonacci(n):

    if n<=1:
        return n

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


if __name__ == '__main__':
    print("Recursive method")
    nr = [5, 7, 10, 12, 15, 17, 20, 22, 25, 27, 30, 32, 35, 37, 40, 42, 45]
    times =[]
    for i in range(len(nr)
    ):
        start = time.time()
        result = Fibonacci(int(nr[i]))
        end = time.time()
        x.add_row([nr[i], result, end-start])
        times.append(end - start)

    print(x)
    plt.plot(nr, times)
    plt.xlabel('nth fibonacci number')
    plt.ylabel('time(s)')
    plt.title('Recursive method Graph')
    plt.show()
