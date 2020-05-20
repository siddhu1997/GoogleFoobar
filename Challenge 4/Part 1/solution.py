import math

class raytracer:

	def __init__(self,dimensions,my_position,guard_position,distance):
		self.dimensions = dimensions
		self.my_position = my_position
		self.guard_position = guard_position
		self.distance = distance

	def getMirror(self,mirror,coordinates,dimensions):
		result = coordinates
		mirrorRotation = [2*coordinates, 2*(dimensions-coordinates)]
		if(mirror < 0):
			for i in range(mirror,0):
				result = result - mirrorRotation[(i+1)%2]
		else:
			for i in range(mirror,0,-1):
				result = result + mirrorRotation[i%2]

		return result

	def map(self,point,dimension):
		mirrored_point = list()
		for i in range(2):
			points = list()
			initial = -(self.distance/dimension[i]) - 1
			final = self.distance/dimension[i] + 2
			for j in range(initial,final):
				points.append(self.getMirror(j,point[i],dimension[i]))
			mirrored_point.append(points)
		return mirrored_point

	def solve(self):
		mirror = [self.map(self.my_position,self.dimensions),self.map(self.guard_position,self.dimensions)]
		result = set()
		dist = dict()
		for i in range(0,len(mirror)):
			for j in mirror[i][0]:
				for k in mirror[i][1]:
					beam = math.atan2((self.my_position[1]-k),(self.my_position[0]-j))
					l = math.hypot((self.my_position[0]-j),self.my_position[1]-k)
					if [j,k] != self.my_position and self.distance >= l:
						if((beam in dist and dist[beam] > l) or beam not in dist):
							if i == 0:
								dist[beam] = l
							else:
								dist[beam] = l
								result.add(beam)
		return len(result)

def solution(dimensions, my_position, guard_position, distance):
	answer = raytracer(dimensions = dimensions, my_position = my_position, guard_position = guard_position, distance = distance)
	return answer.solve()

#print(solution([3,2], [1,1], [2,1], 4))
#print(solution([300,275], [150,150], [185,100], 500))