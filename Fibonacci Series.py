def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

start_num = int(input("Enter the starting number: "))
num_terms = int(input("Enter how many terms you want: "))

series = []
i = 0
while len(series) < num_terms:
    fib = fibonacci(i)
    if fib >= start_num:
            series.append(fib)
    i += 1

print("Fibonacci series from", start_num, "is:")
print(series)

OUTPUT:
Enter the starting number: 4
Enter how many terms you want: 10
Fibonacci series from 4 is:
[5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
