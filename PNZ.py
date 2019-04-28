# Positive, Negetive or Zero

try:
	val = int(input())
	if(val>0):
		print("Positive")
	elif(val<0):
		print("Negetive")
	else:
		print("Zero")
except ValueError:
	print("Invalid Input")
	