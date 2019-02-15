import math

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
		merPrimes.insert(len(merPrimes),2**prime - 1)
		print("l-length",len(s)-1);
		print("mer-prime",merPrimes[-1])
	else:
		print("false")


s=[4]
p=[3]
merPrimes=[]

for i in range(0,8):
	buf=p[-1]
	temp = False
	while(temp == False):
		buf += 2
		if trialPrime(buf) == True:
			p.insert(len(p),buf)
			print("primes",p)
			temp = True

	lucasTest(p[-1])

print(merPrimes)

