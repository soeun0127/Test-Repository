# 새롭게 자리 배치하기 코드
# 생각해보니 몇명은 떨어져 앉아야 한다


import random

names =["강한림", "강현주", "구윤찬", "김광현", "김이안", "김주현", "노성원", "박수정", "박승준", "박진우" ,"박지민" ,"신수민" ,"신웅비", "신유빈" ,"윤장욱" ,"이도환" ,"이산", "이상도", "이서연", "이준하" ,"이하나", "이희건" ,"이효원", "장예령", "조주희", "조혜린" ,"황남주", "황동규", "황혜진" ,"김규탁"]
freshman =["남하원" ,"박가윤" ,"배정민", "손재원" ,"송예원", "여유민", "이신비", "윤현서" ,"최정하", "한지오", "홍채원"]
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
	

