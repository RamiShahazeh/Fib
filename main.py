

from math import sqrt
import time

def get_nth_term_of_fib_using_calculs(n):
    sqrt_of_five = sqrt(5)
    x = 1/sqrt_of_five
    y1 = pow(((1+sqrt_of_five)/2),n)
    y2 = pow(((1-sqrt_of_five)/2),n)
    return int(x*(y1 - y2))

def get_nth_term_of_fib_using_recursion(n):
    if n <= 1:
        return n
    return get_nth_term_of_fib_using_recursion(n-1) + get_nth_term_of_fib_using_recursion(n-2)



def main():
    val = int(input("Enter your value: "))
    tic = time.perf_counter()
    fib_value = get_nth_term_of_fib_using_recursion(val)
    toc = time.perf_counter()
    print(f"Fib sequence using recursion is {toc - tic:0.4f} seconds")
    print(f"Fib value is {fib_value}")

    tic = time.perf_counter()
    fib_value = get_nth_term_of_fib_using_calculs(val)
    toc = time.perf_counter()
    print(f"Fib sequence using calculs is {toc - tic:0.4f} seconds")
    print(f"Fib value is {fib_value}")


if __name__ == "__main__":
    main()
