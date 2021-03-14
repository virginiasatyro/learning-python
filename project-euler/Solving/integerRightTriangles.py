'''
Integer right triangles
   
Problem 39

	If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
	{20,48,52}, {24,45,51}, {30,40,50}
	For which value of p ≤ 1000, is the number of solutions maximised?
'''

p = 120 
list = []

def num_solutions():
	for i in range(int(p/2)):
		for j in range(int(p/2)):
			hipo = pow(i, 2) + pow(j, 2)
			hipo = pow(hipo, 1/2)
			if (i + j + hipo) == p:
				if i not in list:
					list.append((i, j, int(hipo)))
	num_solutions = len(list)/2
	return num_solutions

def solutions_maximised(num, max):
	if num > max:
		max = num 
	return max
'''
num_solutions()		
print(list)
print(num_solutions())
solutions_maximised(num_solutions)'''

for i in range(p):
	
	