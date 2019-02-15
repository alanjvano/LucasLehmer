# LucasLehmer

The purpose of this program is to demonstrate the use of Lucas-Lehmer Test for 
large prime numbers.

The Lucas-Lehmer test can be consisely described as follows:
Let M_p be a Mersenne number of the form 2^p-1, where p is an odd prime.  
Define the Lucas-Lehmer sequence, {s_i}, for all i in **N** such that s_0 = 4, 
and s_n = [(S_(n-1))^2]-2.  The Mersenne number M_p is prime iff s_p-2(%M_p) = 
0.  

Notice that checking the primality of p can be quickly checked using a simpler 
method as its size is exponentially smaller than the Mersenne number is 
defines.
