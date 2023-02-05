#Matrix Exponentiation method
import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["Nth nr", "Time(s)","Fib nr"]


def matrix_mult(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
    return C


def matrix_power(A, n):
    if n == 1:
        return A
    elif n % 2 == 0:
        B = matrix_power(A, n // 2)
        return matrix_mult(B, B)
    else:
        B = matrix_power(A, n - 1)
        return matrix_mult(A, B)


def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        F0 = [1, 1]
        F1 = [[1, 1], [1, 0]]
        Fn = matrix_power(F1, n - 1)
        return Fn[0][0]


if __name__ == '__main__':
    print("Matrix Exponentiation method")
    nr = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
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
    plt.title('Matrix Exponentiation Method Graph')
    plt.show()
