file1 = open("freelancer-dot-com-jobs-by-category.txt","r")
file1_lin = file1.read()
lin_split = file1_lin.split("\n")
list1 = []
for i in lin_split:
 	a = (i.split(":"))
 	list1.append(a)
list1.sort(key=lambda x: int(x[1]))
list1.reverse()
for i in range(0,100):	
	print(list1[i])
