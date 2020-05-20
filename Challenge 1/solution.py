def solution(data, n): 
    # Your code here
    result = list()
    if len(data) > 100:
    	return 0
    else:
    	for i in data:
    		if data.count(i) <= n:
    			result.append(i)
    	return result


print solution([1, 2, 3], 0)
print solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)