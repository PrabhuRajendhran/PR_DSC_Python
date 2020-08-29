import sys
n=len(sys.argv)
print(sys.argv)
sum=0
for i in range(1,n):
	try:
		sum+=int(sys.argv[i])
	except:
		print("Enter Valid input")
print(sum)