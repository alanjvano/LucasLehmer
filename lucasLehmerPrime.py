import math
import sys

def trialPrime(cur):
	i=3
	while i**2 <= cur:
		if cur%i == 0:
			return False
		i += 2
	return True

def lucasTest(prime):
	# Define Lucas-Lehmer sequence until necessary value
	while len(s) <= prime - 2:
		s.insert(len(s), s[-1]**2 - 2)

	residue = divmod(s[-1],2**prime - 1)
	if residue[1] == 0:
		mp.insert(len(mp),prime)
		#print("l-length",len(s)-1);
		print("M-",mp[-1],sep="")
	else:
		print("M-",prime," false",sep="")

# Variable Definitions
s=[4]  #lucas-lehmer sequence
p=[3]  #prime number list
mp=[]  #Mersenne prime list

#note: mp only stores prime exponent values of Mersenne Primes

j = int(input("number of iterations:"))


for i in range(0,j):
	buf=p[-1]
	temp = False
	while(temp == False):
		buf += 2
		if trialPrime(buf) == True:
			p.insert(len(p),buf)
			#print("primes",p)
			temp = True

	lucasTest(p[-1])

