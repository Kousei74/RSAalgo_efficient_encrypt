'''The approach used here is of modular exponentiation which
computes (ab)%c efficiently. 
The naive approach would be to iteratively multiply the result 
with a and take remainder with c.
(It is valid because (a*b)%c=((a%c)*(b%c))%c)) 
However the algo would take O(n) and not very efficient. 
It can be done in log(n) time complexity by exponentiation of squaring.

After i iterations, k becomes k/(2i) and m becomes (m(2i))%c
If we multiply num with m is same as adding 2i to overall power.
We only do this if the righmost bit is 1 in binary form of k

So simply put, while loop runs k times and reducing by half
after each step gives us the complexity of O(logn).'''

import sys 

def power_modulo(m, k, n):
	num=1
	# running while loop for k times 
	while k: 
		if (k%2 == 1):
			# multiply with the base
			num = num*m % n 
		# right shift k by 1 bit meaning divide k by 2  
		k >>= 1 
		# squaring the base
		m= m*m % n    
	return(num)


num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    m, k, n = a[0], a[1], a[2]
    print(power_modulo(m, k, n))
