def func3(n):
	l = [1,1]
	a,b  = 1,1
	i = 2
	while i<n:
		fib_sum = a+b
		a,b = b, a+b
		i+=1
		l.append(b)
	return l
	
func3(10) # => count of Fibonacci numbers or Fibonacci sequence
