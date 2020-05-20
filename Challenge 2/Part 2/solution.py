def vcmp(v1,v2):
	a1 = v1.split(".")
	a2 = v2.split(".")
	n1 = len(a1)
	n2 = len(a2)

	a1 = [int(i) for i in a1]
	a2 = [int(i) for i in a2]

	if n2 > n1:
		for i in range(n1,n2):
			a1.append(-1)
	elif n1 > n2:
		for i in range(n2,n1):
			a2.append(-1)

	for i in range(len(a1)):
		if a1[i] > a2[i]:
			return 1
		elif a2[i] > a1[i]:
			return -1
	return 0

def solution(l):
	n = len(l)
	for i in range(n):
		swapped = False
		for j in range(0,n-i-1):
			if vcmp(l[j],l[j+1]) == 1:
				l[j],l[j+1] = l[j+1],l[j]
				swapped = True
		if swapped == False:
			break
	return l


print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))