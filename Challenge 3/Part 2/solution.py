import numpy as np
from fractions import Fraction,gcd
from functools import reduce

def get_lcm(list):
	x = reduce(lambda x,y: x*y/gcd(x,y),list)
	return x
#function to convert a matrix to its stochastic form
def smatrix(m):
	_smatrix = list()
	tlist = list()
	count = 0
	for i in m:
		len_ = sum(i)
		if len_ == 0:
			tlist.append(count)
			len_ = 1	
		temp = list()
		for j in i:
			temp.append(float(j)/float(len_))
		_smatrix.append(temp)
		count = count + 1		
	return _smatrix,tlist

def solution(m):
	#m is a matrix and len_m contains length of matrix m
	len_m = len(m)
	#Step 1 now m needs to converted into a transition matrix
	transitionmatrix_ , count = smatrix(m)

	#Step 2 create an identity matrix 'I' of size len_m and perform I-transitionmatrix_ and store the result in Q
	I = np.identity(len_m)
	Q = np.subtract(I,transitionmatrix_)

	#Step 3 find inverse of Q and store it in Q_inv
	Q_inv = np.linalg.inv(Q)

	#Step 4 Create a Matrix R of size 1xlen_m with first element as 1
	R = np.zeros(len_m)
	R[0] = 1

	#Step 5 compute R x Q_inv	
	result = R.dot(Q_inv)
	result = [result[g] for g in count]
	ans = list()

	for i in range(len(result)):
		ans.append(Fraction(result[i]).limit_denominator())

	denom_list = [i.denominator for i in ans]
	num_list = [i.numerator for i in ans]
	lcm = get_lcm(denom_list)

	multiplier = list()
	for i in denom_list:
		multiplier.append(lcm/i)

	for i in range(len(num_list)):
		num_list[i] = int(num_list[i] * multiplier[i])

	num_list.append(int(lcm))
	return num_list
	
print(solution(m))
