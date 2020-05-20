#n = input()
cache = dict()
def count(height,bricks):
	if bricks == 0:
		return 1
	elif bricks < height:
		return 0
	else:
		key = "#"+str(height)+"#"+str(bricks)+"$"
		if key not in cache:
			temp = count(height+1,bricks-height)+count(height+1,bricks)
			cache[key] = temp
			return cache[key]
		else:
			 return cache[key] 

def solution(n):			
	return count(1,n)-1