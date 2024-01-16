def fibonacciSeries(i):
 if i <= 1:
    return i
 else:
    return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))

n=int(input("enter the number of terms you want??"))
if n <=0:
  print("Please enter a Positive Number")
else:
  print("Fibonacci Series:", end=" ")
for i in range(n):
  print(fibonacciSeries(i), end=" ")