import sys

mean = 0.0

for elem in sys.argv[1:]:
	mean =  mean + float(elem)

mean = mean / float(len(sys.argv)-1)

var = 0.0
for elem in sys.argv[1:]:
	var = var + (float(elem) - mean)**2

var = var / (len(sys.argv) - 2)

print("Mean: ",  mean)
print("Variance: ", var)


print("Hello World")






