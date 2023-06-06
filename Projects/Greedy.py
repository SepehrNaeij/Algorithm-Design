def swap(a,b):
    t = a
    a = b
    b = t    

def minimumSquare(a, b):
	main_result = 0 
	result = 0
	count = 0
	rem = 0

	if (a < b):
		swap(a,b)
	while (b > 0):
		count+=1
		result = int(a / b)
		main_result += result
		if count != 1:
			print(result," x (", b, " x ",b, ") km^2")
		rem = int(a % b)
		a = b
		b = rem

	return main_result

a = input()
b = input()   

first_number = int(a[0] + a[1])
second_number = int(b[0] + b[1])
 
print(minimumSquare(first_number, second_number))