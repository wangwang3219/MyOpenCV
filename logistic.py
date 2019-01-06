import numpy as np 
import scipy
import os
a =  np.array([2,23,4],dtype =np.int)
print(a)
print(a.dtype) 

b = np.linspace(0,10,11)
print(b)

c = np.ones((3,4)).reshape(2,6)
print(c)

a = np.random.random((2,4))
print(a)

A = np.arange(2,14,1).reshape((3,4))
print(A)
print(A.T.dot(A))
print(np.clip(A,5,9))

q = 10000
for i in range(30):
	q= q * 1.02
print(q)

A = np.random.random((4,2))
print(A)
print(len(A[0]))

a =  np.array([2,23,4],dtype = int)
print(a)
print(a.dtype)

print(os.getcwd())

class Potato:
		# docstring for Potself,name
		def __init__(self, name):
			self.name = 'amy'
		def pr(self):
			print('%s' % self.name)
a = Potato('as')
a.pr()

				