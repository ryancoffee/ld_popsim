#!/home/coffee/envs/tensorflow/bin/python

import numpy as np
import tensorflow as tf

#def sample_population():

class Phenotype:
	ndims = 10;
	phtype = 0;

	def __init__(self,n,p):
		self.ndims = n 
		self.phtype = p 
		self.meanvec = np.zeros(n,dtype=float)

	def setmeans(self):
		if self.phtype != 0:
			self.meanvec = np.ones(self.ndims,dtype=float)
		else:
			self.meanvec = np.zeros(self.ndims,dtype=float)
		if self.phtype == 2:
			self.meanvec[1] = 0.25
			self.meanvec[3] = 1.25
		return self

	def setstds(self):
		if self.phtype !=0:
			self.stdsvec = float(2.5)*np.ones(self.ndims,dtype=float)
		else:
			self.stdsvec = float(1.5)*np.ones(self.ndims,dtype=float)
		return self

	def getmeans(self):
		return self.meanvec
	def getstds(self):
		return self.stdsvec


	def printout(self):
		print('means = ', self.meanvec)
		print('stds = ', self.stdsvec)
		return self

class Individual:
	identity = int(0);
	def __init__():
		#self.phtype = Phenotype(5,1)
		self.identity = int(0)
		return self


def main():
	NDIMS = int(5);
	mytype = Phenotype(NDIMS,0)

	mytype.setmeans().setstds().printout()

	type2 = Phenotype(NDIMS,2)
	
	type2.setmeans().setstds().printout()



if __name__ == "__main__":
	main()

