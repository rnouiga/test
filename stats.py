import sys

for elem in sys.argv[1:]:
	mean =  mean + float(elem)

mean = mean / float(len(sys.argv)-1)
print(mean)






