def factorial(n):
	for i in range(n - 1, 0, -1):
		n *= i
	return n
userString = input("Number please: ")
userNum = int(userString)
print(factorial(userNum))