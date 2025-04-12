from sympy import nextprime, gcd
from random import getrandbits
from Crypto.Util.number import *

original = b"LKSJ{flag_palsu_jangan_di_submit_ya}"
flag = bytes_to_long(original)

# Don't want you to brute force so I created a long flag !
assert len(original) == 63

# A helper for you ;)
def gcd(a, b):
	while b:	  
		a, b = b, a % b
	return a

def randNum(bit_size, n):
	numbers = []
	while len(numbers) < n:
		candidate = nextprime(getrandbits(bit_size))
		if all(gcd(candidate, num) == 1 for num in numbers):
			numbers.append(candidate)

	return numbers

bit_size = 128
n = 5
bignums = randNum(bit_size, n)
for i, num in enumerate(bignums, start=1):
	print(f"{num}")

# 195795056012403052943844326592056957213
# 81249814900027049976092340496610122213
# 80984165775487123479120833077668849193
# 309337385473132401888492109711088483327
# 275829293927639368369068739507593205483

a = 195795056012403052943844326592056957213
b = 81249814900027049976092340496610122213
c = 80984165775487123479120833077668849193
d = 309337385473132401888492109711088483327
e = 275829293927639368369068739507593205483

for x in bignums:
    print(flag % x)

# 52201052332699446254733677573005102748
# 35470972400879853259573227401307711072
# 35516689791584552989173655725202865770
# 123654823608634217707578590322996506392
# 207384680682575272409860998894294921290