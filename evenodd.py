# Odd even or invalid

try:
	val = int(input())
	if((val%2)==0):
		print("Even")
	else:
		print("Odd")
except ValueError:
	print("Invalid Input")
	