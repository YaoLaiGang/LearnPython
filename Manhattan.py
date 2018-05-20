users={"LiMing":{"Football":3.5,"Basketball":2.0,"Swimming":4.0,"Running":5.0},"Chenhao":{"Football":2.0,"Basketball":3.5,"Swimming":4.0,"Running":2.0}}
def manhattan(users,name):
	l=[]
	for e in users:
		distance=0
		if e!=name:
			for m in users[e]:
				distance+=abs(users[e][m]-users[name][m])
			l.append(distance)
	return l
print(manhattan(users,"LiMing"))
