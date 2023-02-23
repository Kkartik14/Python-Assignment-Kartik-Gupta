i=int(input("enter value of i: "))
j=int(input("Enter value of j: "))
k=int(input("enter value of k for spaces:"))
k = i - 1
for i in range(0, i):
	for j in range(0, k):
		print(end=" ")
	k = k - 1
	for j in range(0, i+1):
		print(i+1 , end="  ")
	print("\n")