# Odd even or invalid

try:
	val = int(input())
	if(val>=0):
		if((val%2)==0):
			print("Even")
		else:
			print("Odd")
	else:
		print("Invalid")
except ValueError:
	print("Invalid")
	