def solution(x, y):
   	n = ((x+y-1)*(x+y-2))/2 +x
   	return str(n)

print(solution(3,2))
print(solution(2,3))
print(solution(5,10))