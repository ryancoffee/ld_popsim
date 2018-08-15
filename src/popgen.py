#!/home/coffee/envs/tensorflow/bin/python

import numpy as np
import tensorflow as tf

class Phenotype:
	ndims = 10;
	phID = 0;

	def __init__(self,n,p):
		self.ndims = n 
		self.phID = p 
		self.meanvec = np.zeros(n,dtype=float)

	def setmeans(self):
		if self.phID != 0:
			self.meanvec = np.ones(self.ndims,dtype=float)
		else:
			self.meanvec = np.zeros(self.ndims,dtype=float)
		if self.phID == 2:
			self.meanvec[1] = 0.25
			self.meanvec[-1] = 1.25
		return self

	def setstds(self):
		if self.phID !=0:
			self.stdsvec = float(0.5)*np.ones(self.ndims,dtype=float)
		else:
			self.stdsvec = float(5)*np.ones(self.ndims,dtype=float)
		if self.phID == 2:
			self.stdsvec[1] = 2.0
			self.stdsvec[-1] = 1.0
		return self

	def getmeans(self):
		return self.meanvec
	def getstds(self):
		return self.stdsvec
	def getphID(self):
		return self.phID


	def printout(self):
		print('means = ', self.meanvec)
		print('stds = ', self.stdsvec)
		print('phID = ', self.phID)
		return self





class Individual:
	def __init__(self,ph):
		self.phtype = ph 
		self.phtype.setmeans().setstds()
		#self.phtype.printout()
		self.ndims = self.phtype.ndims

	def samplepheno(self):
		self.coords = np.random.normal(self.phtype.getmeans(),self.phtype.getstds());
		return self
	def getcoords(self):
		return self.coords
	def getphID(self):
		return self.phtype.getphID()

	def printout(self):
		print(self.getcoords(),self.getphID())
		return self
	





"""
**********************
**********************
*******	MAIN *********
"""


def main():
	NDIMS = int(4);

	nphenos = 3

	"""
	type0 = Phenotype(NDIMS,1)
	type1 = Phenotype(NDIMS,1)
	type2 = Phenotype(NDIMS,2)
	type0.setmeans().setstds().printout()
	type1.setmeans().setstds().printout()
	type2.setmeans().setstds().printout()

	print("OK, now copmputing individuals from statistical distributions")

	#individual = Individual(type2)
	#individual.samplepheno().printout()
	"""

	setsz = 10
	outvec = np.zeros((setsz*nphenos,NDIMS),dtype=float)
	outlbl = np.zeros((setsz*nphenos),dtype=int)
	phenoset = np.empty(setsz,dtype=object)
	for j in range(nphenos):
		phtype = Phenotype(NDIMS,j)
		phtype.setmeans().setstds()
		for i in range(phenoset.shape[0]):
			phenoset[i] = Individual(phtype)
			phenoset[i].samplepheno()
			outvec[j*setsz+i,:] = phenoset[i].getcoords()
			outlbl[j*setsz+i] = phenoset[i].getphID()
	

	np.savetxt('./data/values.dat',outvec,fmt='%.4f');
	np.savetxt('./data/labels.dat',outlbl,fmt='%i');






if __name__ == "__main__":
	main()

