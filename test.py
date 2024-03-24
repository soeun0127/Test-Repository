# 새롭게 자리 배치하기 코드
# 생각해보니 몇명은 떨어져 앉아야 한다


import random

names =[기밀]
freshman =[신입]
random.shuffle(names)
random.shuffle(freshman)
g=[]
f=[]
g_size = [4,4,4,5,8,8,8]
f_size = [1,1,1,1,2,3,3]

for size in g_size:
	gr =names[:size]
	names =names[size:]
	g.append(gr)
for size in f_size:
	gr =freshman[:size]
	freshman =freshman[size:]
	f.append(gr)
	
	
for i in range(len(f)):
	print(f[i]+g[i])
	

