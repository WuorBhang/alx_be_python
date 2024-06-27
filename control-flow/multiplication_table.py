def table(n):
	for i in range (1, 11): 
		
		# multiples from 1 to 10
		print ("%d * %d = %d" % (n, i, n * i))

# number for which table is evaluated
n = int(input("Enter a number to see its multiplication table: "))

table(n)