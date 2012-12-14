''' Activity selection problem'''

a = [1,2,3,4,5,6,7,8,9,10,11]
# start times
s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
#finish times 
f = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] 

def activity_selection(a,s,f):
	zipped = zip(a,f)
	import operator
	sortedzipped = sorted(zipped,key=operator.itemgetter(1))
	#print zipped
	#print sortedzipped
	a = [x for x,y in sortedzipped]
	n = len(a)
	S = []
	i = 0
	S.append(a[i])
	for m in range(1,n):
		if s[m] >= f[i]:
			#print s[m] , f[i] ,i 
			S.append(a[m])
			i = m
	return S

print activity_selection(a,s,f)